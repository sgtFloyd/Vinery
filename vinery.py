#!/usr/bin/python
import sys
import ComicVine
from PySide import QtGui
from PySide.QtCore import Qt

ComicVine.set_debug(True)

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

class SearchTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(SearchTree, self).__init__(parent)
    self.header().setVisible(False)
    self.__previousSearch = None

  def load(self, query):
    if self.__previousSearch != query:
      search = ComicVine.Series.search(query)
      items = [SearchResult(obj) for obj in search]
      self.clear()
      self.insertTopLevelItems(0, items)
      self.__previousSearch = query

class SearchBox(QtGui.QLineEdit):
  def __init__(self, searchResults):
    super(SearchBox, self).__init__()
    self.searchResults = searchResults
    self.returnPressed.connect(self.doSearch)
    self.setFocus()

  def doSearch(self):
    query = self.text()
    if query:
      self.searchResults.load(query)

class SearchResult(QtGui.QTreeWidgetItem):
  def __init__(self, series):
    super(SearchResult, self).__init__()
    self.setText(0, series.label())
    self.setData(1, Qt.UserRole, series)

    if series.publisher and series.publisher.name:
      publisher = QtGui.QTreeWidgetItem()
      publisher.setText(0, 'Publisher: %s' % series.publisher.name)
      self.addChild(publisher)

    if series.count_of_issues:
      issues = QtGui.QTreeWidgetItem()
      issues.setText(0, '%s issues' % series.count_of_issues)
      self.addChild(issues)

  def json(self):
    return self.data(1, Qt.UserRole)

class MainWindow(QtGui.QWidget):
  def __init__(self):
    super(MainWindow, self).__init__()
    layout = QtGui.QGridLayout()
    layout.addWidget(SearchGroup(), 0, 0)
    self.setLayout(layout)
    self.setWindowTitle("Vinery")

# Create the application object
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit( app.exec_() )
