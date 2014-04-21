import copymanager
import hd44780

screen = hd44780.HD44780()
screen.clear()
copy_mgr = copymanager.CopyManager("/root/code/sdcard", "/root/code/hdd", screen)
copy_mgr.copy_files()
