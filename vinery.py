#!/usr/bin/python
import sys
import ComicVine
from PySide import QtGui

ComicVine.set_debug(True)

# Create the application object
# app = QtGui.QApplication(sys.argv)

# label = QtGui.QLabel("<font color=red size=40>"+ComicVine.search_series('Walking Dead')+"</font>")
# label.show()

# sys.exit( app.exec_() )
print ComicVine.search_series('Walking Dead')
