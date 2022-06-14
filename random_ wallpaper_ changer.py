"""
this program is setting  random wallpapers according to time to beautify screen
"""

import subprocess
import os.path
import os
import fnmatch
import random
import sys
import time
from tkinter import Tk
from tkinter import filedialog


class WallPaperChanger:
    """
    class for setting random wallpaper according to time
     """

    def __init__(self, directory_path, img_ext) -> None:
        """
        constructor for initializing variables
        :param directory_path:
        :param img_ext:
        """
        self.path = directory_path
        self.files = []
        self.image_ext = img_ext

    @staticmethod
    def set_wallpaper(picture_path):
        """
        this function is setting wallpaper
        :param picture_path:
        :return: None
        """
        subprocess.Popen(
            "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri "
            "file://{0}".format(
                picture_path), shell=True)

    def get_files(self, ext='*.'):
        """
        this function is getting files/wallpaper from the directory
        :param ext:
        :return: list of objects
        """
        matches = []
        for current_path, _, filenames in os.walk(self.path):
            for filename in fnmatch.filter(filenames, ext):
                matches.append(os.path.join(current_path, filename))
        return matches

    def change_wallpaper(self):
        """
        this function is changing wallpaper according to time if wallpaper exists

       """

        for ext in image_ext:
            self.files += self.get_files(ext)
        index = random.randint(0, len(self.files) - 1)
        obj.set_wallpaper(r'"' + self.files[index] + '"')
        print('Wallpaper Set!')
        time.sleep(10)
        while True:
            self.change_wallpaper()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    try:
        target_folder = filedialog.askdirectory()
        image_ext = ['*.jpeg', '*.jpg', '*.JPG', '*.png', '*.PNG']
        obj = WallPaperChanger(target_folder, image_ext)
        try:
            obj.change_wallpaper()
        except KeyboardInterrupt:
            exit(1)
    except TypeError:
        sys.exit()
