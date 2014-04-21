__author__ = 'pierrerossines'

import os
import custom_shutil as shutil
import time
import progressbar
import errno

class CopyManager:
    def __init__(self, sdcard, hdd, screen):
        if os.path.exists(sdcard) and os.path.isdir(sdcard):
            self.sdcard = sdcard
        else:
            print("The folder " + sdcard + " doesn't exist")
            return

        if os.path.exists(hdd) and os.path.isdir(hdd):
            self.hdd = hdd
        else:
            print("The folder " + hdd + " doesn't exist")
            return

        self.screen = screen
        self.total_size = self.get_sdcard_content_size()
        self.available_size = self.get_hdd_free_space()

        self.copied_size = 0
        self.progress_bar = progressbar.ProgressBar(0, self.total_size)

    def copy_files(self):
        if self.total_size > self.available_size:
            self.screen.clear()
            self.screen.message("Disk full")
            return
        i = 0
        path = os.path.join(self.hdd, str(i))
        while os.path.exists(path):
            i = i+1
            path = os.path.join(self.hdd, str(i))
        folder = os.path.join(self.hdd, path)
        try:
            shutil.copytree(self.sdcard, folder, self.update_copy)
        except EnvironmentError as error:
            self.screen.clear()
            self.screen.message("Copy error")
            print("Error while copying the files: " + error.message)
        self.screen.clear()
        self.screen.message("Finished")


    def update_copy(self, file_size):
        self.copied_size = self.copied_size + file_size
        progres = self.progress_bar.get_progress(self.copied_size)
        self.screen.clear()
        self.screen.message("Pending copy\n" + progres)

    def get_sdcard_content_size(self):
        "Returns the size of the files in the sdcard"
        return self.get_size(self.sdcard)

    def get_hdd_free_space(self):
        "Returns the free space left on the hdd"
        return self.get_fs_freespace(self.sdcard)

    def get_size(self, start_path = '.'):
        "Get the recursive size of a folder"
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def get_fs_freespace(self, pathname):
        "Get the free space of the filesystem containing pathname"
        stat= os.statvfs(pathname)
        # use f_bfree for superuser, or f_bavail if filesystem
        # has reserved space for superuser
        return stat.f_bfree*stat.f_bsize
