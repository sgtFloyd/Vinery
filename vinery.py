#!/usr/bin/python
import sys
import ComicVine
import json
from PySide import QtGui

ComicVine.set_debug(True)

# Create the application object
# app = QtGui.QApplication(sys.argv)

# label = QtGui.QLabel("<font color=red size=40>"+ComicVine.search_series('Walking Dead')+"</font>")
# label.show()

# sys.exit( app.exec_() )
results = ComicVine.search_series('Walking Dead')
# results = ComicVine.search_issues('Walking Dead')
# results = ComicVine.get_series(18166) # Walking Dead
# results = ComicVine.get_issue(115705) # Walking Dead #3
print json.dumps(results, indent=4)
