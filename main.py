import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from interfaceProj import Ui_MainWindow
from PySide2.QtWidgets import QFileDialog

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        # Set a fixed initial size of the window once we run it
        self.setFixedSize(1100, 700)

        # Connect the Exit button to the close slot
        self.Exit.clicked.connect(self.close)

        # Connect the Expand button to the toggleFullScreen slot
        self.Expand.clicked.connect(self.toggleFullScreen)

        # Connect the Minimize button to the showMinimized slot
        self.minimizeBtn.clicked.connect(self.showMinimized)

        # Connect the menuList button to show or hide the sideMenuContainer
        self.menuList.clicked.connect(self.toggleSideMenu)

        # Connect buttons to switch pages
        self.About.clicked.connect(lambda: self.switchToPage(0, "About"))
        self.Developers.clicked.connect(lambda: self.switchToPage(1, "Developers"))
        self.New.clicked.connect(lambda: self.switchToPage(2, "newPage"))
        self.History.clicked.connect(lambda: self.switchToPage(3, "historyPage"))

        # Set the initial page (Home page)
        initial_page_index = 0
        self.stackedWidget.setCurrentIndex(initial_page_index)

        self.uploadBtn.clicked.connect(self.openFileDialog)

      
        #for side drawer to, to make it work
    def toggleSideMenu(self):
        new_width = 250
        self.sideMenuContainer.setFixedWidth(new_width)
        self.sideMenuContainer.setVisible(not self.sideMenuContainer.isVisible())

    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    #for stackedwidget switchpages
    def switchToPage(self, index, page_name):
        self.stackedWidget.setCurrentIndex(index)
        
    def openFileDialog(self):
        # Open a file dialog to select a video file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("MP3/MP4 (*.mp3 *.mp4)")
        selected_file, _ = file_dialog.getOpenFileName(self, "Select File", "", "MP3/MP4 (*.mp3 *.mp4)", options=options)

        # If a file is selected, update the fileName label
        if selected_file:
            self.fileName.setText(f'Selected File: {selected_file}')

    

   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
