#!/usr/bin/python
import sys
from PySide import QtGui

# Create the application object
app = QtGui.QApplication(sys.argv)

label = QtGui.QLabel("<font color=red size=40>Hello World</font>")
label.show()

sys.exit( app.exec_() )
