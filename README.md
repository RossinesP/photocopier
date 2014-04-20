photocopier
===========

A very simple project aimed to run on a raspberry pi.

The raspberry pi should be connected to an sdcard and a hard drive. It should also
be connected to a HD44780 screen through GPIO to display some messages.

The goal is to copy the content of the sdcard to the hard drive.


hd44780.py file originally copied from https://github.com/lrvick/raspi-hd44780/blob/master/hd44780.py
custom_shutil.py file copied from the Python sources and modified to handle copy progress updates
