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

  def showSeries(self, item, column=0):
    data = item.json()
    print data['id']

class SeriesSearchItem(QtGui.QTreeWidgetItem):
  def __init__(self, data):
    super(SeriesSearchItem, self).__init__()
    label = '%s (%s) [%s]' % (res['name'], res['start_year'], res['publisher']['name'])
    self.setText(0, label)
    self.setData(1, Qt.UserRole, data)
    self.addChild( self.__loadingItem() )

  def json(self):
    return self.data(1, Qt.UserRole)

  def __loadingItem(self):
    item = QtGui.QTreeWidgetItem()
    item.setText(0, "Loading...")
    return item

# Create the application object
app = QtGui.QApplication(sys.argv)
search = ComicVine.Series.search('Walking Dead')

tree = SearchTree()
items = [SeriesSearchItem(res) for res in search['results']]
tree.insertTopLevelItems(0, items)
tree.show()

sys.exit( app.exec_() )


# import json
# results = ComicVine.Series.search('Walking Dead')
# results = ComicVine.Issue.search('Walking Dead')
# results = ComicVine.Series.show(18166) # Walking Dead
# results = ComicVine.Issue.show(115705) # Walking Dead #3
# print json.dumps(results, indent=4)
