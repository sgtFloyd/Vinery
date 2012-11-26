#!/usr/bin/python
import sys
import ComicVine
from PySide import QtGui
from PySide.QtCore import Qt

ComicVine.set_debug(True)

class SearchTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(SearchTree, self).__init__(parent)
    self.header().setVisible(False)
    self.setWindowTitle("Search")

  def loadSearch(self, query):
    search = ComicVine.Series.search(query)
    items = [SeriesSearchItem(result) for result in search['results']]
    self.insertTopLevelItems(0, items)

class SeriesSearchItem(QtGui.QTreeWidgetItem):
  def __init__(self, data):
    super(SeriesSearchItem, self).__init__()
    label = '%s (%s)' % (data['name'], data['start_year'])
    self.setText(0, label)
    self.setData(1, Qt.UserRole, data)

    publisher = QtGui.QTreeWidgetItem()
    publisher.setText(0, 'Publisher: %s' % data['publisher']['name'])
    issues = QtGui.QTreeWidgetItem()
    issues.setText(0, '%s issues' % data['count_of_issues'])
    self.addChildren([publisher, issues])

  def json(self):
    return self.data(1, Qt.UserRole)

class MainWindow(QtGui.QWidget):
  def __init__(self):
    super(MainWindow, self).__init__()
    layout = QtGui.QGridLayout()
    layout.addWidget(self.searchGroup(), 0, 0)
    self.setLayout(layout)
    self.setWindowTitle("Vinery")

  def doSearch(self):
    query = self.searchBox.text()
    if query:
      self.searchResults.loadSearch(query)

  def searchGroup(self):
    self.searchBox = QtGui.QLineEdit()
    self.searchBox.returnPressed.connect(self.doSearch)
    self.searchBox.setFocus()

    self.searchResults = SearchTree()

    layout = QtGui.QGridLayout()
    layout.addWidget(QtGui.QLabel("Search:"), 0, 0)
    layout.addWidget(self.searchBox, 0, 1)
    layout.addWidget(self.searchResults, 1, 0, 2, 2)

    group = QtGui.QGroupBox('')
    group.setLayout(layout)
    return group

# Create the application object
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit( app.exec_() )


# import json
# results = ComicVine.Series.search('Walking Dead')
# results = ComicVine.Issue.search('Walking Dead')
# results = ComicVine.Series.show(18166) # Walking Dead
# results = ComicVine.Issue.show(115705) # Walking Dead #3
# print json.dumps(results, indent=4)
