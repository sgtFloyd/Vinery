#!/usr/bin/python
import lib.ComicVine
from app.views.main_window import *

lib.ComicVine.set_debug(True)

class LibraryWindow(QtGui.QWidget):
  def __init__(self):
    super(LibraryWindow, self).__init__()
    self.setWindowTitle("Library")

    layout = QtGui.QGridLayout()
    layout.addWidget(LibraryTree(), 0, 0)
    layout.addWidget(FileGroup(), 0, 1)
    self.setLayout(layout)

class LibraryTree(QtGui.QTreeWidget):
  def __init__(self, parent=None):
    super(LibraryTree, self).__init__(parent)
    self.header().setVisible(False)
    self.loadLibrary()

  def loadLibrary(self):
    print("loading vinery_library.json")

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)

  window = MainWindow()
  window.setMinimumSize(800, 400)
  window.show()

  library = LibraryWindow()
  library.setMinimumSize(800, 400)
  library.show()

  sys.exit( app.exec_() )
