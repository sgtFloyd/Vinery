#!/usr/bin/python
import ComicVine
from main_window import *

ComicVine.set_debug(True)

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)
  window = MainWindow()
  window.setMinimumSize(800, 400)
  window.show()
  sys.exit( app.exec_() )
