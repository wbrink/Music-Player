# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music_player2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.playButton = QtWidgets.QPushButton(self.tab)
        self.playButton.setGeometry(QtCore.QRect(660, 100, 89, 25))
        self.playButton.setObjectName("playButton")
        self.prevButton = QtWidgets.QPushButton(self.tab)
        self.prevButton.setGeometry(QtCore.QRect(660, 10, 89, 25))
        self.prevButton.setObjectName("prevButton")
        self.songPlayingLabel = QtWidgets.QLabel(self.tab)
        self.songPlayingLabel.setGeometry(QtCore.QRect(0, 320, 231, 17))
        self.songPlayingLabel.setObjectName("songPlayingLabel")
        self.songSlider = QtWidgets.QSlider(self.tab)
        self.songSlider.setGeometry(QtCore.QRect(50, 290, 541, 20))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.endLabel = QtWidgets.QLabel(self.tab)
        self.endLabel.setGeometry(QtCore.QRect(600, 290, 31, 17))
        self.endLabel.setObjectName("endLabel")
        self.volumeLabel = QtWidgets.QLabel(self.tab)
        self.volumeLabel.setGeometry(QtCore.QRect(680, 230, 67, 17))
        self.volumeLabel.setObjectName("volumeLabel")
        self.nextButton = QtWidgets.QPushButton(self.tab)
        self.nextButton.setGeometry(QtCore.QRect(660, 170, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.songTableWidget = QtWidgets.QTableWidget(self.tab)
        self.songTableWidget.setGeometry(QtCore.QRect(0, 0, 631, 281))
        self.songTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.songTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.songTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.songTableWidget.setRowCount(0)
        self.songTableWidget.setColumnCount(6)
        self.songTableWidget.setObjectName("songTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget.setHorizontalHeaderItem(4, item)
        self.startLabel = QtWidgets.QLabel(self.tab)
        self.startLabel.setGeometry(QtCore.QRect(0, 290, 41, 17))
        self.startLabel.setObjectName("startLabel")
        self.volumeSlider = QtWidgets.QSlider(self.tab)
        self.volumeSlider.setGeometry(QtCore.QRect(700, 250, 20, 81))
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 771, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.playlists = QtWidgets.QWidget()
        self.playlists.setObjectName("playlists")
        self.search_label_2 = QtWidgets.QLabel(self.playlists)
        self.search_label_2.setGeometry(QtCore.QRect(550, 10, 67, 17))
        self.search_label_2.setObjectName("search_label_2")
        self.searchEdit_2 = QtWidgets.QLineEdit(self.playlists)
        self.searchEdit_2.setGeometry(QtCore.QRect(540, 30, 201, 25))
        self.searchEdit_2.setObjectName("searchEdit_2")
        self.playlistTableWidget_2 = QtWidgets.QTableWidget(self.playlists)
        self.playlistTableWidget_2.setGeometry(QtCore.QRect(0, 0, 511, 351))
        self.playlistTableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlistTableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlistTableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.playlistTableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.playlistTableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.playlistTableWidget_2.setRowCount(0)
        self.playlistTableWidget_2.setColumnCount(3)
        self.playlistTableWidget_2.setObjectName("playlistTableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.playlistTableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlistTableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlistTableWidget_2.setHorizontalHeaderItem(2, item)
        self.deleteButton_2 = QtWidgets.QRadioButton(self.playlists)
        self.deleteButton_2.setGeometry(QtCore.QRect(580, 170, 141, 51))
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.finaldeleteButton_2 = QtWidgets.QPushButton(self.playlists)
        self.finaldeleteButton_2.setGeometry(QtCore.QRect(600, 240, 89, 25))
        self.finaldeleteButton_2.setObjectName("finaldeleteButton_2")
        self.finalDeleteLabel_2 = QtWidgets.QLabel(self.playlists)
        self.finalDeleteLabel_2.setGeometry(QtCore.QRect(596, 290, 101, 20))
        self.finalDeleteLabel_2.setText("")
        self.finalDeleteLabel_2.setObjectName("finalDeleteLabel_2")
        self.stackedWidget.addWidget(self.playlists)
        self.playlist_songs = QtWidgets.QWidget()
        self.playlist_songs.setObjectName("playlist_songs")
        self.songTableWidget_2 = QtWidgets.QTableWidget(self.playlist_songs)
        self.songTableWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 281))
        self.songTableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.songTableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.songTableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.songTableWidget_2.setRowCount(0)
        self.songTableWidget_2.setColumnCount(6)
        self.songTableWidget_2.setObjectName("songTableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_2.setHorizontalHeaderItem(4, item)
        self.endLabel_2 = QtWidgets.QLabel(self.playlist_songs)
        self.endLabel_2.setGeometry(QtCore.QRect(600, 290, 31, 17))
        self.endLabel_2.setObjectName("endLabel_2")
        self.volumeLabel_2 = QtWidgets.QLabel(self.playlist_songs)
        self.volumeLabel_2.setGeometry(QtCore.QRect(680, 230, 67, 17))
        self.volumeLabel_2.setObjectName("volumeLabel_2")
        self.songPlayingLabel_2 = QtWidgets.QLabel(self.playlist_songs)
        self.songPlayingLabel_2.setGeometry(QtCore.QRect(0, 320, 231, 17))
        self.songPlayingLabel_2.setObjectName("songPlayingLabel_2")
        self.playButton_2 = QtWidgets.QPushButton(self.playlist_songs)
        self.playButton_2.setGeometry(QtCore.QRect(660, 100, 89, 25))
        self.playButton_2.setObjectName("playButton_2")
        self.prevButton_2 = QtWidgets.QPushButton(self.playlist_songs)
        self.prevButton_2.setGeometry(QtCore.QRect(660, 10, 89, 25))
        self.prevButton_2.setObjectName("prevButton_2")
        self.volumeSlider_2 = QtWidgets.QSlider(self.playlist_songs)
        self.volumeSlider_2.setGeometry(QtCore.QRect(700, 250, 20, 81))
        self.volumeSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider_2.setObjectName("volumeSlider_2")
        self.songSlider_2 = QtWidgets.QSlider(self.playlist_songs)
        self.songSlider_2.setGeometry(QtCore.QRect(50, 290, 541, 20))
        self.songSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider_2.setObjectName("songSlider_2")
        self.nextButton_2 = QtWidgets.QPushButton(self.playlist_songs)
        self.nextButton_2.setGeometry(QtCore.QRect(660, 170, 89, 25))
        self.nextButton_2.setObjectName("nextButton_2")
        self.startLabel_2 = QtWidgets.QLabel(self.playlist_songs)
        self.startLabel_2.setGeometry(QtCore.QRect(0, 290, 41, 17))
        self.startLabel_2.setObjectName("startLabel_2")
        self.playlist_button_2 = QtWidgets.QPushButton(self.playlist_songs)
        self.playlist_button_2.setGeometry(QtCore.QRect(280, 320, 211, 25))
        self.playlist_button_2.setObjectName("playlist_button_2")
        self.playlist_name_2 = QtWidgets.QLabel(self.playlist_songs)
        self.playlist_name_2.setGeometry(QtCore.QRect(0, 340, 101, 17))
        self.playlist_name_2.setObjectName("playlist_name_2")
        self.stackedWidget.addWidget(self.playlist_songs)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.songTableWidget_tab3 = QtWidgets.QTableWidget(self.tab_3)
        self.songTableWidget_tab3.setGeometry(QtCore.QRect(0, 0, 511, 351))
        self.songTableWidget_tab3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget_tab3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songTableWidget_tab3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.songTableWidget_tab3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.songTableWidget_tab3.setGridStyle(QtCore.Qt.SolidLine)
        self.songTableWidget_tab3.setRowCount(0)
        self.songTableWidget_tab3.setColumnCount(6)
        self.songTableWidget_tab3.setObjectName("songTableWidget_tab3")
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_tab3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_tab3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_tab3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_tab3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.songTableWidget_tab3.setHorizontalHeaderItem(4, item)
        self.searchEdit_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.searchEdit_tab3.setGeometry(QtCore.QRect(540, 30, 201, 25))
        self.searchEdit_tab3.setObjectName("searchEdit_tab3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(550, 10, 67, 17))
        self.label.setObjectName("label")
        self.playlistNameEdit_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.playlistNameEdit_tab3.setGeometry(QtCore.QRect(550, 160, 191, 25))
        self.playlistNameEdit_tab3.setObjectName("playlistNameEdit_tab3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(550, 130, 111, 17))
        self.label_2.setObjectName("label_2")
        self.saveButton_tab3 = QtWidgets.QPushButton(self.tab_3)
        self.saveButton_tab3.setGeometry(QtCore.QRect(600, 200, 89, 25))
        self.saveButton_tab3.setObjectName("saveButton_tab3")
        self.playlist_verifier_tab3 = QtWidgets.QLabel(self.tab_3)
        self.playlist_verifier_tab3.setGeometry(QtCore.QRect(546, 239, 191, 51))
        self.playlist_verifier_tab3.setText("")
        self.playlist_verifier_tab3.setObjectName("playlist_verifier_tab3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MP3 Player"))
        self.tab.setToolTip(_translate("Form", "<html><head/><body><p>All Songs</p><p><br/></p></body></html>"))
        self.playButton.setText(_translate("Form", "Play"))
        self.prevButton.setText(_translate("Form", "Prev"))
        self.songPlayingLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">song</span></p></body></html>"))
        self.endLabel.setText(_translate("Form", "end"))
        self.volumeLabel.setText(_translate("Form", "Volume"))
        self.nextButton.setText(_translate("Form", "Next"))
        item = self.songTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Song"))
        item = self.songTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Artist"))
        item = self.songTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Album"))
        item = self.songTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Length"))
        item = self.songTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Path"))
        self.startLabel.setText(_translate("Form", "start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Libary"))
        self.search_label_2.setText(_translate("Form", "Search"))
        item = self.playlistTableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Playlist"))
        item = self.playlistTableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Songs"))
        item = self.playlistTableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date"))
        self.deleteButton_2.setText(_translate("Form", "Delete Playlists"))
        self.finaldeleteButton_2.setText(_translate("Form", "Delete"))
        item = self.songTableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Song"))
        item = self.songTableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Artist"))
        item = self.songTableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Album"))
        item = self.songTableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Length"))
        item = self.songTableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Path"))
        self.endLabel_2.setText(_translate("Form", "end"))
        self.volumeLabel_2.setText(_translate("Form", "Volume"))
        self.songPlayingLabel_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">song</span></p></body></html>"))
        self.playButton_2.setText(_translate("Form", "Play"))
        self.prevButton_2.setText(_translate("Form", "Prev"))
        self.nextButton_2.setText(_translate("Form", "Next"))
        self.startLabel_2.setText(_translate("Form", "start"))
        self.playlist_button_2.setText(_translate("Form", "Playlists"))
        self.playlist_name_2.setText(_translate("Form", "Playlistname"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Playlists"))
        item = self.songTableWidget_tab3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Song"))
        item = self.songTableWidget_tab3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Artist"))
        item = self.songTableWidget_tab3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Album"))
        item = self.songTableWidget_tab3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Length"))
        item = self.songTableWidget_tab3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Path"))
        self.label.setText(_translate("Form", "Search"))
        self.label_2.setText(_translate("Form", "Playlist Name"))
        self.saveButton_tab3.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Create Playlist"))
