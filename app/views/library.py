import os
from PySide import QtGui

class LibraryView(QtGui.QWidget):
  def __init__(self):
    super(LibraryView, self).__init__()
    self.setWindowTitle("Library")

    self.libraryTree = LibraryTree()
    self.filePathBox = FilePathBox(self.libraryTree)
    self.openButton = OpenButton(self.filePathBox)

    layout = QtGui.QGridLayout()
    layout.addWidget(QtGui.QLabel("Library:"), 0, 0)
    layout.addWidget(self.filePathBox, 0, 1)
    layout.addWidget(self.openButton, 0, 2)
    layout.addWidget(self.libraryTree, 1, 0, 1, 3)
    self.setLayout(layout)

class FilePathBox(QtGui.QLineEdit):
  def __init__(self, libraryTree):
    super(FilePathBox, self).__init__()
    self.libraryTree = libraryTree
    self.returnPressed.connect(self.openPath)

  def browseDirectory(self):
    options = QtGui.QFileDialog.ShowDirsOnly
    directory = QtGui.QFileDialog.getExistingDirectory(self, 'Open', self.text(), options)
    if directory:
      self.path = directory
      self.setText(directory)
      self.openPath()

  def openPath(self):
    if self.path:
      self.libraryTree.load(self.path)

class OpenButton(QtGui.QPushButton):
  def __init__(self, filePathBox):
    super(OpenButton, self).__init__('Open')
    self.filePathBox = filePathBox
    self.clicked.connect(self.filePathBox.browseDirectory)

class LibraryTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(LibraryTree, self).__init__(parent)
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
