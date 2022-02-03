import sys

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navBar = QToolBar()
        self.addToolBar(navBar)

        backBtn = QAction("< Back", self)
        backBtn.triggered.connect(self.browser.back)
        navBar.addAction(backBtn)

        forwardBtn = QAction("Forward >", self)
        forwardBtn.triggered.connect(self.browser.forward)
        navBar.addAction(forwardBtn)

        refreshBtn = QAction("Refresh", self)
        refreshBtn.triggered.connect(self.browser.reload)
        navBar.addAction(refreshBtn)

        homeBtn = QAction("Home", self)
        homeBtn.triggered.connect(self.home)
        navBar.addAction(homeBtn)


        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navBar.addWidget(self.searchBar)

        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com"))

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl("https://" + url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())

PyBrowser = QApplication(sys.argv)

QApplication.setApplicationName("PyBrowser")

window = Window()

PyBrowser.exec_()
