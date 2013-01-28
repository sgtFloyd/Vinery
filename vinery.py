#!/usr/bin/python
import lib.ComicVine
from app.views.main_window import *
from app.views.library import *

lib.ComicVine.set_debug(True)

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)

  # window = MainWindow()
  # window.setMinimumSize(800, 400)
  # window.show()

  library = LibraryView()
  library.setMinimumSize(800, 400)
  library.show()

  sys.exit( app.exec_() )
