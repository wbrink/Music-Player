#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QScroller, QAbstractItemView
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
from design import Ui_Form
import sys
import os
import eyed3
import datetime



"""
app = QApplication(sys.argv)
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
"""

if not os.path.exists('playlists'):
    os.makedirs("playlists")



class Music_Player(QWidget, Ui_Form):

    with open("path.txt", 'r') as f:
        home_dir = f.read()
        home_dir = home_dir.rstrip()


    def __init__(self):
        #super(Music_Player, self).__init__()
        super().__init__()
        #set up the user interface from Designer
        self.setupUi(self)


        # this gets the inforation needed for the table
        lib = []
        directory = os.path.join(Music_Player.home_dir, "Music")

        walk = os.walk(directory)
        for root, dirs, files in walk:
            for file in files:
                path = os.path.join(root, file)
                if file.endswith('.mp3'): # then we should add file to library\
                    song = os.path.splitext(file)[0]
                    song = song.replace('_', ' ')

                    # using eyed3 to get song info
                    audiofile = eyed3.load(path)
                    artist = audiofile.tag.artist
                    album = audiofile.tag.album
                    length_secs = audiofile.info.time_secs # seconds
                    length_formatted = seconds_to_minutes(length_secs)

                    # list of lists with information
                    lib.append([song, artist, album, length_formatted, path, str(length_secs)]) # length shows seconds

        # usedfor the functions
        self.library = lib



        self.songTableWidget_tab3.setRowCount(len(lib))
        self.songTableWidget_2.setRowCount(len(lib))
        self.songTableWidget.setRowCount(len(lib))
        self.songTableWidget.setColumnHidden(4, True) #hide path column
        self.songTableWidget.setColumnHidden(5, True) #hide length column that shows seconds
        self.songTableWidget_2.setColumnHidden(4, True) #hide path column
        self.songTableWidget_2.setColumnHidden(5, True) #hide length column that shows seconds
        self.songTableWidget_tab3.setColumnHidden(4, True) #hide path column
        self.songTableWidget_tab3.setColumnHidden(5, True) #hide length column that shows seconds
        self.songTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # no way to edit items
        self.songTableWidget_tab3.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # setting the column widths
        self.songTableWidget.setColumnWidth(0, 220)
        self.songTableWidget.setColumnWidth(1, 160)
        self.songTableWidget.setColumnWidth(2, 165)
        self.songTableWidget.setColumnWidth(3, 60)

        # setting up touch scrolling for the songTableWidget
        scroller = QScroller.scroller(self.songTableWidget)
        QScroller.grabGesture(self.songTableWidget, QScroller.LeftMouseButtonGesture)

        # setting up touch scrolling for the playlistTableWidget_2
        scroller_playlist_2 = QScroller.scroller(self.playlistTableWidget_2)
        QScroller.grabGesture(self.playlistTableWidget_2, QScroller.LeftMouseButtonGesture)

        # setting up touch scrolling for the songTableWidget_2
        scroller_2 = QScroller.scroller(self.songTableWidget_2)
        QScroller.grabGesture(self.songTableWidget_2, QScroller.LeftMouseButtonGesture)

        # setting up touch scrolling for the songTableWidget_tab3
        scroller_3 = QScroller.scroller(self.songTableWidget_tab3)
        QScroller.grabGesture(self.songTableWidget_tab3, QScroller.LeftMouseButtonGesture)

        # populating the table
        for i in range(len(lib)): #number of rows
            for k in range(6): # there are 6 columns
                item = QTableWidgetItem(lib[i][k])
                item2 = QTableWidgetItem(lib[i][k])
                item3 = QTableWidgetItem(lib[i][k])
                self.songTableWidget.setItem(i, k, item)
                self.songTableWidget_tab3.setItem(i,k,item2) # for tab3
                self.songTableWidget_2.setItem(i,k,item3)

        self.songTableWidget.sortItems(0, Qt.AscendingOrder)
        self.songTableWidget_tab3.sortItems(0, Qt.AscendingOrder) # tab 3


        # add the check mark boxes so they don't only appear when the song is played for the first time
        for i in range(self.songTableWidget.rowCount()):
            self.songTableWidget.item(i, 0).setCheckState(Qt.Unchecked)
            self.songTableWidget_2.item(i, 0).setCheckState(Qt.Unchecked)

        # setting up media Player
        self.player = QMediaPlayer(None)


        if  not os.path.exists("log.txt"):
            with open("log.txt", 'w') as f:
                pass
        # the time doesn't work but the row does
        # this will load the last song played into the media player, though time will start from 0
        with open("log.txt", 'r') as f:
            info = f.read()

        if info:
            row = int(info.split(',')[0])
            self.time = int(info.split(',')[1]) # used in mediaStatusChanged to allow for the startup time
            song_path = self.songTableWidget.item(row,4).text()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(song_path)))
            #self.player.play()

            # used by mediaStatusChanged to load in the correct place the player left off from
            #self.startup = 1

        else:
            row = 0
            default_song_path = self.songTableWidget.item(0, 4).text()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(default_song_path)))


        # make adjustments
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSliderPosition(100)
        self.volumeLabel.setText(str(100))

        self.songSlider.setMinimum(0)
        self.songSlider.setMaximum(int(self.songTableWidget.item(row, 5).text()))


        self.endLabel.setText(self.songTableWidget.item(row, 3).text())
        self.songPlayingLabel.setText(self.songTableWidget.item(row, 0).text())

        # tab 3 signals and slots
        self.saveButton_tab3.clicked.connect(self.save_click)
        self.searchEdit_tab3.textChanged.connect(self.search_edit)

        #conncect buttons
        self.volumeSlider.valueChanged.connect(self.volume_change)
        self.playButton.clicked.connect(self.play_click)
        self.songTableWidget.cellDoubleClicked.connect(self.double_click)
        self.player.stateChanged.connect(self.state_changed) # playing, paused, no media
        self.player.positionChanged.connect(self.position_changed)
        self.player.mediaStatusChanged.connect(self.media_status) # #loading media, end of media, etc.
        self.player.currentMediaChanged.connect(self.song_changed) # when the song changes
        self.songSlider.sliderMoved.connect(self.slider_moved)
        self.songSlider.sliderReleased.connect(self.slider_released)
        self.nextButton.clicked.connect(self.next)
        self.prevButton.clicked.connect(self.prev)


##################################################################
###########################################################
#################### tab 2 #############################\

        self.finaldeleteButton_2.setVisible(False)

        self.player_2 = QMediaPlayer(None)
        self.player_2.setVolume(100)

        # make adjustments
        self.volumeSlider_2.setMaximum(100)
        self.volumeSlider_2.setSliderPosition(100)
        self.volumeLabel_2.setText(str(100))


        self.endLabel_2.setText(self.songTableWidget_2.item(0, 3).text())
        self.songPlayingLabel_2.setText(self.songTableWidget_2.item(0, 0).text())



        self.playlistTableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.songTableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #conncect buttons
        self.volumeSlider_2.valueChanged.connect(self.volume_change_2)
        self.playButton_2.clicked.connect(self.play_click_2)
        self.songTableWidget_2.cellDoubleClicked.connect(self.double_click_2)
        self.player_2.stateChanged.connect(self.state_changed_2) # playing, paused, no media
        self.player_2.positionChanged.connect(self.position_changed_2)
        self.player_2.mediaStatusChanged.connect(self.media_status_2) # #loading media, end of media, etc.
        self.player_2.currentMediaChanged.connect(self.song_changed_2) # when the song changes
        self.songSlider_2.sliderMoved.connect(self.slider_moved_2)
        self.songSlider_2.sliderReleased.connect(self.slider_released_2)
        self.nextButton_2.clicked.connect(self.next_2)
        self.prevButton_2.clicked.connect(self.prev_2)


        # if there are playlists present on the system we want to list them
        files = os.listdir(Music_Player.home_dir+"/Desktop/music_player/playlists")
        if files:
            self.playlistTableWidget_2.setRowCount(len(files))
            playlist_names = [os.path.splitext(file)[0] for file in files]

            x = 0
            for file in files:
                with open(Music_Player.home_dir+'/Desktop/music_player/playlists/{}'.format(file), 'r') as f:
                    lines = f.readlines()
                    amount_of_songs = lines[-2]
                    date_added = lines[-1]
                playlist_name = os.path.splitext(file)[0]
                item_1 = QTableWidgetItem(playlist_name)
                item_2 = QTableWidgetItem(amount_of_songs)
                item_3 = QTableWidgetItem(date_added)
                self.playlistTableWidget_2.setItem(x, 0, item_1)
                self.playlistTableWidget_2.setItem(x, 1, item_2)
                self.playlistTableWidget_2.setItem(x, 2, item_3)
                x = x + 1


        self.playlistTableWidget_2.cellDoubleClicked.connect(self.choose_playlist)
        self.playlist_button_2.clicked.connect(self.back_to_playlists)
        self.deleteButton_2.clicked.connect(self.delete_button_2)
        self.finaldeleteButton_2.clicked.connect(self.finaldelete_clicked_2)

    def delete_button_2(self):
        if self.deleteButton_2.isChecked():
            self.playlistTableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
            # show delete button
            self.finaldeleteButton_2.setVisible(True)
        if self.deleteButton_2.isChecked() == False:
            self.playlistTableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
            self.finaldeleteButton_2.setVisible(False)

    def finaldelete_clicked_2(self):
        items = self.playlistTableWidget_2.selectedItems() # will have many duplicates in the list that is returned
        if items: # if list is not empty
            pass
        else:
            self.finalDeleteLabel_2.setText("Must Select Playlist[s]")



    def back_to_playlists(self):
        self.stackedWidget.setCurrentIndex(0)

    def choose_playlist(self, row, column): # when the playlist is clicked
        ## get back to neutral so we don't keep removing songs from table

        self.songTableWidget_2.sortItems(0, Qt.AscendingOrder)
        count = self.songTableWidget_2.rowCount()
        for k in range(count):
            self.songTableWidget_2.setRowHidden(k, False)


        playlist_name = self.playlistTableWidget_2.item(row, 0).text()
        self.stackedWidget.setCurrentIndex(1)
        self.playlist_name_2.setText(playlist_name)
        with open(Music_Player.home_dir+'/Desktop/music_player/playlists/{}.txt'.format(playlist_name), 'r') as f:
            songs = f.readlines()[:-2] # the last two lines are amount of songs in the playlist and the date the playlist was created
            songs = [song.rstrip() for song in songs]

        items = []
        for song in songs:
            items.append(self.songTableWidget_2.findItems(song, Qt.MatchContains))
        items  = [item[0] for item in items]
        rows = { i.row() for i in items}

        # hiding the songs not in playlist
        for k in range(count):
            if k not in rows:
                self.songTableWidget_2.setRowHidden(k, True)



    def prev_2(self):
        path = self.player_2.currentMedia().canonicalUrl().path()
        item = self.songTableWidget_2.findItems(path, Qt.MatchExactly)
        row = item[0].row() # gives the index starting at 0
        #print(row, self.songTableWidget.rowCount())


        if self.player_2.position() >= 2000:
            self.player_2.setPosition(0)
            return True


        if row == 0:
            print("row==0")
            for i in range(1, self.songTableWidget_2.rowCount()):
                next_row = self.songTableWidget_2.rowCount() - i # row count starts counting at 1 so index = rowCount -1
                if self.songTableWidget_2.isRowHidden(next_row):
                    continue
                else:
                    break
            new_song_path = self.songTableWidget_2.item(next_row, 4).text()
        else:
            for i in range(1, self.songTableWidget_2.rowCount()): # 1 to the row count
                next_row = row - i # all you need is 1 minus the row count to make the list full circle
                if next_row < 0:
                    next_row = self.songTableWidget_2.rowCount()+ next_row # then we need be back at the last index

                if self.songTableWidget_2.isRowHidden(next_row):
                    continue
                else:
                    break
            new_song_path = self.songTableWidget_2.item(next_row, 4).text()



        if self.player_2.state() == QMediaPlayer.PlayingState:
            self.player_2.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))
            self.player_2.play()
        else:
            self.player_2.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))



    def next_2(self):
        path = self.player_2.currentMedia().canonicalUrl().path()
        item = self.songTableWidget_2.findItems(path, Qt.MatchExactly)
        row = item[0].row() # gives the index starting at 0


        if self.songTableWidget_2.rowCount() == (row + 1): # then we are at end of table
            next_row = 0
            if self.songTableWidget_2.isRowHidden(next_row):
                for i in range(1, self.songTableWidget_2.rowCount()):
                    next_row = next_row + i
                    if self.songTableWidget_2.isRowHidden(next_row):
                        continue
                    else:
                        break

            new_song_path = self.songTableWidget_2.item(next_row, 4).text()


        else:
            for i in range(1, self.songTableWidget_2.rowCount()):
                next_row = row + i
                if next_row >= self.songTableWidget_2.rowCount(): # then the index is out of range
                    next_row = next_row - self.songTableWidget_2.rowCount()
                if self.songTableWidget_2.isRowHidden(next_row):
                    continue
                else:
                    break
            new_song_path = self.songTableWidget_2.item(next_row, 4).text()


        if self.player_2.state() == QMediaPlayer.PlayingState:
            self.player_2.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))
            self.player_2.play()
        else:
            self.player_2.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))



    def slider_moved_2(self, value): # signal when slider is pressed down
        if self.songSlider_2.isSliderDown():
            time = seconds_to_minutes(value)
            self.startLabel_2.setText(time)

    def slider_released_2(self):
        seconds = self.songSlider_2.sliderPosition()
        self.player_2.setPosition(seconds*1000)

    def song_changed_2(self, song): # takes QMediaContent
        path = (song.canonicalUrl().path()) # path of song used to locate row in table
        item = self.songTableWidget_2.findItems(path, Qt.MatchExactly)
        row = item[0].row() # there can only be one match in the list

        self.songPlayingLabel_2.setText(self.songTableWidget_2.item(row, 0).text())
        self.endLabel_2.setText(self.songTableWidget_2.item(row, 3).text())
        self.songSlider_2.setMaximum(int(self.songTableWidget_2.item(row, 5).text()))



        # now need to setup how the slider will work
        # when slider is pressed down song still plays at normal pace but start label adjusts to where the slider is
        # shen slider is released then move the song to that position



    def media_status_2(self, status): # takes QMediaPlayer.MediaStatus
        if status == QMediaPlayer.BufferedMedia:
            # get rid of all the check marks on the songs that have been played
            for i in range(self.songTableWidget_2.rowCount()):
                self.songTableWidget_2.item(i, 0).setCheckState(Qt.Unchecked)
            path = self.player_2.currentMedia().canonicalUrl().path()
            item = self.songTableWidget_2.findItems(path, Qt.MatchExactly) #qtbalewidgetitem
            row = item[0].row() # this finds the row that the qtablewidgetitem originates
            self.songTableWidget_2.item(row, 0).setCheckState(Qt.Checked)
        elif status == QMediaPlayer.EndOfMedia:
            path = self.player_2.currentMedia().canonicalUrl().path()
            item = self.songTableWidget_2.findItems(path, Qt.MatchExactly) #qtbalewidgetitem
            row = item[0].row() # this finds the row that the qtablewidgetitem originates
            self.songTableWidget_2.item(row, 0).setCheckState(Qt.Unchecked)
            print("end of media")


    def position_changed_2(self, position): # position is expressed in milleseconds
        seconds = int(position / 1000) # now its in seconds
        if self.songSlider_2.isSliderDown() == False:
            self.songSlider_2.setSliderPosition(seconds)
            time = seconds_to_minutes(seconds)
            self.startLabel_2.setText(time)

    def state_changed_2(self, state):
        if self.player_2.state() == QMediaPlayer.PlayingState:
            self.playButton_2.setText("Pause")
            # turns the library player off
            self.player.pause()
        if self.player_2.state() == QMediaPlayer.PausedState or self.player_2.state() == QMediaPlayer.StoppedState :
            self.playButton_2.setText("Play")

    def play_click_2(self):
        if self.player_2.state() == 1: # playing state
            self.player_2.pause()
        elif self.player_2.state() == 2: # paused state
            self.player_2.play()
        else: # stopped state which = 0
            self.player_2.play()


    def volume_change_2(self, value):
        self.volumeLabel_2.setText(str(value))
        self.player_2.setVolume(value)

    def double_click_2(self, row, column): #row and column are ints
        song = self.songTableWidget_2.item(row, 0).text() # this is the cell with song name
        # returns the qtablewidgetitem need to change it to text
        path = self.songTableWidget_2.item(row, 4).text()
        self.songPlayingLabel_2.setText(song)
        self.player_2.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.player_2.play()



#####################################################################################
#####################################################################################
#################################### tab 3 ###########################################
#####################################################################################
#####################################################################################

    def search_edit(self, text):
        # reset at the beginnning so that everything shows up
        count = self.songTableWidget_tab3.rowCount()
        for k in range(count):
            self.songTableWidget_tab3.setRowHidden(k, False)

        items = self.songTableWidget_tab3.findItems(text, Qt.MatchContains)
        rows = { i.row() for i in items}

        count = self.songTableWidget_tab3.rowCount()
        for k in range(count):
            if k not in rows:
                self.songTableWidget_tab3.setRowHidden(k, True)



    def save_click(self):
        playlist_name = self.playlistNameEdit_tab3.text()
        if playlist_name: # will need to check that there is no other playlist name that has the same Name
            if self.songTableWidget_tab3.selectedItems():
                rows_selected = {i.row() for i in self.songTableWidget_tab3.selectedItems()}
                songs_selected = [self.songTableWidget_tab3.item(i,4).text() for i in rows_selected]
                print(rows_selected)
                print(songs_selected)

                with open(Music_Player.home_dir+'/Desktop/music_player/playlists/{}.txt'.format(playlist_name), 'w') as f:
                    for i in songs_selected:
                        f.write(i+'\n')
                    f.write(str(len(songs_selected))+'\n')
                    f.write(str(datetime.datetime.now()))

                # update the playlist table in tab2
                files = os.listdir(Music_Player.home_dir+'/Desktop/music_player/playlists')
                if files:
                    self.playlistTableWidget_2.setRowCount(len(files))
                    playlist_names = [os.path.splitext(file)[0] for file in files]

                    x = 0
                    for file in files:
                        with open(Music_Player.home_dir+'/Desktop/music_player/playlists/{}'.format(file), 'r') as f:
                            lines = f.readlines()
                            amount_of_songs = lines[-2]
                            date_added = lines[-1]
                        playlist_name = os.path.splitext(file)[0]
                        item_1 = QTableWidgetItem(playlist_name)
                        item_2 = QTableWidgetItem(amount_of_songs)
                        item_3 = QTableWidgetItem(date_added)
                        self.playlistTableWidget_2.setItem(x, 0, item_1)
                        self.playlistTableWidget_2.setItem(x, 1, item_2)
                        self.playlistTableWidget_2.setItem(x, 2, item_3)
                        x = x + 1

            else:
                self.playlist_verifier_tab3.setText("Need to Select Songs")

        else:
            self.playlist_verifier_tab3.setText("Not a Valid Name")



    ##############################################################
    ###########################################################
    #################### tab 1 #############################

    def prev(self):
        path = self.player.currentMedia().canonicalUrl().path()
        item = self.songTableWidget.findItems(path, Qt.MatchExactly)
        row = item[0].row() # gives the index starting at 0
        #print(row, self.songTableWidget.rowCount())


        if self.player.position() >= 2000:
            self.player.setPosition(0)
            return True


        if row == 0:
            next_row = self.songTableWidget.rowCount() - 1 # row count starts counting at 1 so index = rowCount -1
            new_song_path = self.songTableWidget.item(next_row, 4).text()
        else:
            next_row = row - 1
            new_song_path = self.songTableWidget.item(next_row, 4).text()



        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))
            self.player.play()
        else:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))



    def next(self):
        path = self.player.currentMedia().canonicalUrl().path()
        item = self.songTableWidget.findItems(path, Qt.MatchExactly)
        row = item[0].row() # gives the index starting at 0


        if self.songTableWidget.rowCount() == (row + 1): # then we are at end of table
            next_row = 0
            new_song_path = self.songTableWidget.item(next_row, 4).text()


        else:
            next_row = row + 1
            new_song_path = self.songTableWidget.item(next_row, 4).text()


        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))
            self.player.play()
        else:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(new_song_path)))



    def slider_moved(self, value): # signal when slider is pressed down
        if self.songSlider.isSliderDown():
            time = seconds_to_minutes(value)
            self.startLabel.setText(time)

    def slider_released(self):
        seconds = self.songSlider.sliderPosition()
        self.player.setPosition(seconds*1000)

    def song_changed(self, song): # takes QMediaContent
        path = (song.canonicalUrl().path()) # path of song used to locate row in table
        item = self.songTableWidget.findItems(path, Qt.MatchExactly)
        row = item[0].row() # there can only be one match in the list

        self.songPlayingLabel.setText(self.songTableWidget.item(row, 0).text())
        self.endLabel.setText(self.songTableWidget.item(row, 3).text())
        self.songSlider.setMaximum(int(self.songTableWidget.item(row, 5).text()))



        # now need to setup how the slider will work
        # when slider is pressed down song still plays at normal pace but start label adjusts to where the slider is
        # shen slider is released then move the song to that position



    def media_status(self, status): # takes QMediaPlayer.MediaStatus
        if status == QMediaPlayer.BufferedMedia:
            # get rid of all the check marks on the songs that have been played
            for i in range(self.songTableWidget.rowCount()):
                self.songTableWidget.item(i, 0).setCheckState(Qt.Unchecked)
            path = self.player.currentMedia().canonicalUrl().path()
            item = self.songTableWidget.findItems(path, Qt.MatchExactly) #qtbalewidgetitem
            row = item[0].row() # this finds the row that the qtablewidgetitem originates
            self.songTableWidget.item(row, 0).setCheckState(Qt.Checked)
        elif status == QMediaPlayer.EndOfMedia:
            path = self.player.currentMedia().canonicalUrl().path()
            item = self.songTableWidget.findItems(path, Qt.MatchExactly) #qtbalewidgetitem
            row = item[0].row() # this finds the row that the qtablewidgetitem originates
            self.songTableWidget.item(row, 0).setCheckState(Qt.Unchecked)
            print("end of media")


    def position_changed(self, position): # position is expressed in milleseconds
        seconds = int(position / 1000) # now its in seconds
        if self.songSlider.isSliderDown() == False:
            self.songSlider.setSliderPosition(seconds)
            time = seconds_to_minutes(seconds)
            self.startLabel.setText(time)

    def state_changed(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Pause")
            self.player_2.pause()

        if self.player.state() == QMediaPlayer.PausedState or self.player.state() == QMediaPlayer.StoppedState :
            self.playButton.setText("Play")

    def play_click(self):
        if self.player.state() == 1: # playing state
            self.player.pause()
        elif self.player.state() == 2: # paused state
            self.player.play()
        else: # stopped state which = 0
            self.player.play()


    def volume_change(self, value):
        self.volumeLabel.setText(str(value))
        self.player.setVolume(value)

    def double_click(self, row, column): #row and column are ints
        song = self.songTableWidget.item(row, 0).text() # this is the cell with song name
        # returns the qtablewidgetitem need to change it to text
        path = self.songTableWidget.item(row, 4).text()
        self.songPlayingLabel.setText(song)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.player.play()
        #self.songTableWidget.



    def closeEvent(self, event):
        path = self.player.currentMedia().canonicalUrl().path()
        item = self.songTableWidget.findItems(path, Qt.MatchExactly) #qtbalewidget item
        row = item[0].row() # this finds the row that the qtablewidgetitem originates
        time = int(self.player.position()/1000) - 1 # saves the milliseconds from the beginning of the song
        with open('log.txt', 'w') as f:
            info = "{},{}".format(str(row), str(time))
            f.write(info)
        event.accept()


def seconds_to_minutes(length):
    minutes, seconds = divmod(length, 60)
    #if minutes < 10:
        #minutes = str(0) + str(minutes)
    if seconds < 10:
        seconds = str(0) + str(seconds)
    return "{}:{}".format(str(minutes), str(seconds))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Music_Player()
    window.show()
    sys.exit(app.exec_())
