import os
from krita import *
from PyQt5.QtWidgets import QFileDialog, QListWidget, QInputDialog, QMessageBox
from .window_info import WindowInfo
from .organizer import Organizer

def show_window(title, message):
    QMessageBox.information(QWidget(), title, message)

class MenuActions():
    organizer = Organizer()

    def __init__(self, file_list):
        self.file_list = file_list  # Use the list passed from Menu
        self.layout_path = Application.readSetting("subwindowRecall", "layoutDirectory", "")

    def selected_item_path(self, item):
        if item is None:  # Prevent error if no item is selected
            return ""

        item_text = item.text().strip()
        selected_item = os.path.join(self.layout_path, item_text)
        return selected_item

    def save_as(self):
        subwindow_sizes = WindowInfo.find_sizes(self)
        subwindow_positions = WindowInfo.find_positions(self)
        file_name, _ = QFileDialog.getSaveFileName(None, "Save file as", self.layout_path, "Text file (*.txt);;All Files (*)")

        if not file_name:
            print("No directory selected")
            return
        base_name, ext = os.path.splitext(file_name)
        file_path = base_name + ".txt"
        backup_file_path = file_path + "~"
        if os.path.exists(file_path):
            try:
                os.replace(file_path, backup_file_path)
            except OSError as e:
                print(f"Error renaming file for backup: {e}")
        try:
            with open (file_path, "w", encoding="utf-8") as f:

                for item in subwindow_sizes:
                    f.write("%s\n" % item)
                for item in subwindow_positions:
                    f.write("%s\n" % item)
        except OSError as e:
            print(f"Error writing file: {e}")
        self.load_layout_folder()

    def load_selected_layout(self, item):
        selected_path = self.selected_item_path(item)

        if os.path.exists(selected_path):
            Application.writeSetting("subwindowRecall", "currentLayout", selected_path)
            self.organizer.resize_windows()
        else:
            show_window("File does not exist", "The selected file does not exist, please make sure you have written the file name correctly")

    def search_layout(self):
        path, _ = QFileDialog.getOpenFileName(None, "Open layout", self.layout_path, "Text file (*.txt);;All Files (*)")

        if not path:
            print("No file selected.")
            return

        base_name, ext = os.path.splitext(path)
        searched_path = base_name + ".txt"
        if searched_path:
            Application.writeSetting("subwindowRecall", "currentLayout", searched_path)
            self.organizer.resize_windows()

    def rename(self, item):
        old_name = self.selected_item_path(item)
        # ask the user for the new name
        user_input, ok = QInputDialog().getText(None, "Rename file", "New name:")
        if not ok or not user_input.strip():
            return

        base_name = os.path.splitext(user_input)[0]

        new_name = os.path.join(self.layout_path, user_input + ".txt")

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            self.load_layout_folder()

    def delete(self, item):
        if item is None or item.text().strip() == "":  # Ensure an item is selected
            print("No file selected")
            return

        selected_item = self.selected_item_path(item)
        if not selected_item or not os.path.exists(selected_item):  # Double-check path validity
            print("Invalid file path or file does not exist")
            return

        reply = QMessageBox.question(
            None,
            "Confirm deletion",
            f"Are you sure you want to delete '{item.text()}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
            )

        if reply == QMessageBox.Yes:
            os.remove(selected_item)
            self.load_layout_folder()
        else:
            print("Deletion canceled")

    def set_layout_folder(self):
        path = QFileDialog.getExistingDirectory(None, "Open directory", "/", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if path:
            Application.writeSetting("subwindowRecall", "layoutDirectory", path)
            self.load_layout_folder()

    def load_layout_folder(self):
        self.file_list.clear()
        path = Application.readSetting("subwindowRecall", "layoutDirectory", "")
        if os.path.exists(path):
            files = [f for f in os.listdir(path) if f.endswith(".txt")]
            self.file_list.addItems(files)


