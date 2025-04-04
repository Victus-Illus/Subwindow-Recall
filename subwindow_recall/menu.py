import os
from krita import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QCheckBox, QListWidget, QPushButton
from .menu_actions import MenuActions

class Menu(QDialog):
    def __init__(self, isToggled: bool, toggle_callback):
        krita_window = Krita.instance().activeWindow().qwindow()
        super().__init__(krita_window)
        self.setWindowTitle("Subwindow Recall")
        main_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        save_button = QCheckBox("Auto-save layouts")
        save_button.setCheckable(True)
        save_button.setChecked(isToggled)
        save_button.toggled.connect(toggle_callback)
        button_layout.addWidget(save_button)
        self.file_list = QListWidget()
        self.menu_actions = MenuActions(self.file_list)

        save_as_button = QPushButton("Save current layout as...")
        save_as_button.clicked.connect(self.menu_actions.save_as)
        button_layout.addWidget(save_as_button)

        load_button = QPushButton("Load selected layout")
        load_button.clicked.connect(lambda: self.menu_actions.load_selected_layout(self.file_list.currentItem()))
        button_layout.addWidget(load_button)

        search_layout_button = QPushButton("Search layout...")
        search_layout_button.clicked.connect(self.menu_actions.search_layout)
        button_layout.addWidget(search_layout_button)

        rename_layout = QPushButton("Rename layout to...")
        rename_layout.clicked.connect(lambda: self.menu_actions.rename(self.file_list.currentItem()))
        button_layout.addWidget(rename_layout)

        delete_layout = QPushButton("Delete selected layout")
        delete_layout.clicked.connect(lambda: self.menu_actions.delete(self.file_list.currentItem() if self.file_list.currentItem() else None))
        button_layout.addWidget(delete_layout)

        layout_folder = QPushButton("Set layout folder to...")
        layout_folder.clicked.connect(self.menu_actions.set_layout_folder)
        button_layout.addWidget(layout_folder)

        #self.file_list.itemClicked.connect(self.menu_actions.load_selected_layout)
        self.menu_actions.load_layout_folder()

        main_layout.addWidget(self.file_list)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.show()

        self.setup()

    def setup(self):
        self.notifier = Application.notifier()
        self.notifier.setActive(True)
        self.notifier.applicationClosing.connect(self.auto_close)

    def file_selected(self, item):
        layout_directory = Application.readSetting("subwindowRecall", "layoutDirectory", "")
        full_path = os.path.join(layout_directory, item.text())
        print(f"selected layout: {item.text()}")

    def auto_close(self):
        self.close()
