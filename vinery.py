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
    self.itemExpanded.connect(self.showSeries)

  def loadSearch(self, query):
    search = ComicVine.Series.search(query)
    items = [SeriesSearchItem(result) for result in search['results']]
    self.insertTopLevelItems(0, items)

  def showSeries(self, item, column=0):
    if not item.loadedIssues:
      series_id = item.json()['id']
      search = ComicVine.Series.show(series_id)
      issues = [IssueSearchItem(issue) for issue in search['results']['issues']]
      item.takeChildren()
      item.addChildren(issues)
      item.loadedIssues = True

class SeriesSearchItem(QtGui.QTreeWidgetItem):
  def __init__(self, data):
    super(SeriesSearchItem, self).__init__()
    label = '%s (%s) [%s]' % (data['name'], data['start_year'], data['publisher']['name'])
    self.setText(0, label)
    self.setData(1, Qt.UserRole, data)
    self.addChild(QtGui.QTreeWidgetItem())
    self.loadedIssues = False

  def json(self):
    return self.data(1, Qt.UserRole)

class IssueSearchItem(QtGui.QTreeWidgetItem):
  def __init__(self, data):
    super(IssueSearchItem, self).__init__()
    label = '#%s' % data['issue_number'].strip().rstrip("0").rstrip('.')
    if data['name'].strip():
      label += ' - %s' % data['name'].strip()
    self.setText(0, label)
    self.setData(1, Qt.UserRole, data)

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
      self.tree.loadSearch(query)


  def searchGroup(self):
    group = QtGui.QGroupBox('')
    label = QtGui.QLabel("Search:")

    self.searchBox = QtGui.QLineEdit()
    self.searchBox.returnPressed.connect(self.doSearch)
    self.searchBox.setFocus()

    self.tree = SearchTree()

    layout = QtGui.QGridLayout()
    layout.addWidget(label, 0, 0)
    layout.addWidget(self.searchBox, 0, 1)
    layout.addWidget(self.tree, 1, 0, 2, 2)
    group.setLayout(layout)
    return group

# Create the application object
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()

#tree = SearchTree()
#tree.loadSearch("Walking Dead")
#tree.show()

sys.exit( app.exec_() )


# import json
# results = ComicVine.Series.search('Walking Dead')
# results = ComicVine.Issue.search('Walking Dead')
# results = ComicVine.Series.show(18166) # Walking Dead
# results = ComicVine.Issue.show(115705) # Walking Dead #3
# print json.dumps(results, indent=4)
