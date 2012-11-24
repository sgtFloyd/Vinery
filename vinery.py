#!/usr/bin/python
import sys
import ComicVine
from PySide import QtGui
from PySide.QtCore import Qt

ComicVine.set_debug(True)

# Create the application object
app = QtGui.QApplication(sys.argv)

tree = QtGui.QTreeWidget()
tree.setWindowTitle("Simple Tree Model")
tree.header().setVisible(False)

search = ComicVine.Series.search('Walking Dead')

items = []
for res in search['results']:
  label = '%s (%s) [%s]' % (res['name'], res['start_year'], res['publisher']['name'])

  item = QtGui.QTreeWidgetItem()
  item.setText(0, label)
  item.setData(1, Qt.UserRole, res)
  items.append(item)

tree.insertTopLevelItems(0, items)
tree.show()

sys.exit( app.exec_() )


# import json
# results = ComicVine.Series.search('Walking Dead')
# results = ComicVine.Issue.search('Walking Dead')
# results = ComicVine.Series.show(18166) # Walking Dead
# results = ComicVine.Issue.show(115705) # Walking Dead #3
# print json.dumps(results, indent=4)
