from lib.data_manager import DataManager
from tkinter import Tk
from time import sleep
from lib.tiktok_utils import download_video, download_videos
from lib.auto_utils import copy_paste_enter, toggle_console
from pyautogui import hotkey, click, press


class TitokDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Tiktok Downloader")

        self.dm = DataManager(root)

        self.dm.create_entry("Output", "output_folder", isFolder=True, isBrowse=True)
        self.dm.create_entry("URL", "url")
        self.dm.create_button("Download Video", self.download_by_url, self.load_data)

        self.dm.create_button(
            "Get video Urls", self.get_video_urls_in_screen, self.load_data
        )

        self.dm.create_entry("File", "file_path", isBrowse=True)
        self.dm.create_button("Download Videos", self.download_by_file, self.load_data)

    def load_data(self):
        self.url = self.dm.get_entry_data("url")
        self.file_path = self.dm.get_entry_data("file_path")
        self.output_folder = self.dm.get_entry_data("output_folder")

        return

    async def download_by_url(self):
        if await download_video(self.url, self.output_folder):
            self.dm.clear_entry_data("url")
        return

    async def download_by_file(self):
        if await download_videos(self.file_path, self.output_folder):
            self.dm.clear_entry_data("file_path")
        return

    async def get_video_urls_in_screen(self):
        hotkey("alt", "tab")
        sleep(0.5)

        toggle_console()
        sleep(0.5)

        with open(r"lib\getTiktokUrls.js", "r") as file:
            js_content = file.read()
            copy_paste_enter(js_content)

        toggle_console()


def main():
    root = Tk()
    app = TitokDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
