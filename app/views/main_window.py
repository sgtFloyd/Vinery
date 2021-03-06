import os
import lib.ComicVine
from PySide import QtGui
from PySide.QtCore import Qt

class SearchGroup(QtGui.QGroupBox):
  def __init__(self):
    super(SearchGroup, self).__init__('')
    self.searchResults = SearchTree()
    self.searchBox = SearchBox(self.searchResults)

    layout = QtGui.QGridLayout()
    layout.addWidget(QtGui.QLabel("Search:"), 0, 0)
    layout.addWidget(self.searchBox, 0, 1)
    layout.addWidget(self.searchResults, 1, 0, 2, 2)
    self.setLayout(layout)

class SearchBox(QtGui.QLineEdit):
  def __init__(self, searchResults):
    super(SearchBox, self).__init__()
    self.searchResults = searchResults
    self.returnPressed.connect(self.doSearch)

  def doSearch(self):
    query = self.text()
    if query:
      self.searchResults.load(query)

class SearchTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(SearchTree, self).__init__(parent)
    self.header().setVisible(False)
    self.__previousSearch = None

  def load(self, query):
    if self.__previousSearch != query:
      search = lib.ComicVine.Series.search(query)
      items = [SearchResult(obj) for obj in search]
      self.clear()
      self.insertTopLevelItems(0, items)
      self.__previousSearch = query

class SearchResult(QtGui.QTreeWidgetItem):
  def __init__(self, series):
    super(SearchResult, self).__init__()
    self.series = series
    self.setText(0, series.label())

    desc = QtGui.QTreeWidgetItem()
    desc.setText(0, series.description())
    self.addChild(desc)

class FileGroup(QtGui.QGroupBox):
  def __init__(self):
    super(FileGroup, self).__init__('')
    self.fileTree = FileTree()
    self.filePathBox = FilePathBox(self.fileTree)
    self.browseButton = FileBrowse(self.filePathBox)

    layout = QtGui.QGridLayout()
    layout.addWidget(self.browseButton, 0, 0)
    layout.addWidget(self.filePathBox, 0, 1)
    layout.addWidget(self.fileTree, 1, 0, 2, 2)
    self.setLayout(layout)

class FileBrowse(QtGui.QPushButton):
  def __init__(self, filePathBox):
    super(FileBrowse, self).__init__('Browse')
    self.filePathBox = filePathBox
    self.clicked.connect(self.filePathBox.browseDirectory)

class FilePathBox(QtGui.QLineEdit):
  def __init__(self, fileTree):
    super(FilePathBox, self).__init__()
    self.fileTree = fileTree
    self.returnPressed.connect(self.openPath)

  def browseDirectory(self):
    options = QtGui.QFileDialog.ShowDirsOnly
    directory = QtGui.QFileDialog.getExistingDirectory(self, "Browse", self.text(), options)
    if directory:
      self.setText(directory)
      self.openPath()

  def openPath(self):
    path = self.text()
    if path:
      self.fileTree.load(path)

class FileTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(FileTree, self).__init__(parent)
    self.header().setVisible(False)
    self.itemExpanded.connect(self.openDirectory)

  def load(self, path):
    items = [FileEntry(path, fname) for fname in os.listdir(path)]
    self.insertTopLevelItems(0, items)

  def openDirectory(self, item, column=0):
    item.expand()

class FileEntry(QtGui.QTreeWidgetItem):
  def __init__(self, path, filename):
    super(FileEntry, self).__init__()
    self.filename = filename
    self.fullPath = os.path.join(path, filename)
    self.isDirectory = os.path.isdir(self.fullPath)

    self.setText(0, filename)
    if self.isDirectory:
      self.addChild(QtGui.QTreeWidgetItem())

  def expand(self):
    items = [FileEntry(self.fullPath, fname) for fname in os.listdir(self.fullPath)]
    self.takeChildren()
    self.addChildren(items)

class MainWindow(QtGui.QWidget):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle("Vinery")

    layout = QtGui.QGridLayout()
    layout.addWidget(SearchGroup(), 0, 0)
    layout.addWidget(FileGroup(), 0, 1)
    self.setLayout(layout)
