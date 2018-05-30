# PyQt5 Music Player
Small music player that is meant to go on a touch screen on a raspberry pi
There is a class variable set to the path of the computer name.

```python
with open("path.txt", 'r') as f:
      home_dir = f.read()
      home_dir = home_dir.rstrip()
```
This is found in *path.txt* which is located in the same directory as the player's code files.
The only information that is needed in the file is the path. An example of the contents of this file is made below.

> home/name-of-computer


This project relied on the use of QDesigner to make the user interface file. This can be adjusted with *music_player2.ui*
