import os
from krita import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QCheckBox, QListWidget, QPushButton
from .menu_actions import MenuActions

class Menu(QDialog):
    def __init__(self, isToggled: bool, toggle_callback, last_layout_callback):
        krita_window = Krita.instance().activeWindow().qwindow()
        super().__init__(krita_window)
        self.setWindowTitle("Subwindow Recall")

        vertical_layout = QVBoxLayout()
        main_horizontal_box_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        secondary_horizontal_box_layout = QHBoxLayout()
        rename_delete_layout = QHBoxLayout()

        save_button = QCheckBox("Auto-save layouts")
        save_button.setCheckable(True)
        save_button.setChecked(isToggled)
        save_button.toggled.connect(toggle_callback)
        button_layout.addWidget(save_button)
        self.file_list = QListWidget()
        self.menu_actions = MenuActions(self.file_list, self.update_current_layout_label)
        self.current_layout_label = QLabel()
        self.update_current_layout_label()

        vertical_layout.addWidget(self.current_layout_label)

        save_as_button = QPushButton("Save current layout as...")
        save_as_button.clicked.connect(self.menu_actions.save_as)
        button_layout.addWidget(save_as_button)

        load_current_layout = QPushButton("Load current layout")
        load_current_layout.clicked.connect(last_layout_callback)
        button_layout.addWidget(load_current_layout)

        load_button = QPushButton("Load selected layout")
        load_button.clicked.connect(lambda: self.menu_actions.load_selected_layout(self.file_list.currentItem()))
        button_layout.addWidget(load_button)

        search_layout_button = QPushButton("Search layout...")
        search_layout_button.clicked.connect(self.menu_actions.search_layout)
        button_layout.addWidget(search_layout_button)

        rename_layout = QPushButton("Rename layout to...")
        rename_layout.clicked.connect(lambda: self.menu_actions.rename(self.file_list.currentItem()))
        rename_delete_layout.addWidget(rename_layout)

        delete_layout = QPushButton("Delete selected layout")
        delete_layout.clicked.connect(lambda: self.menu_actions.delete(self.file_list.currentItem() if self.file_list.currentItem() else None))
        rename_delete_layout.addWidget(delete_layout)

        layout_folder = QPushButton("Set layout folder to...")
        layout_folder.clicked.connect(self.menu_actions.set_layout_folder)

        self.menu_actions.load_layout_folder()

        main_horizontal_box_layout.addWidget(self.file_list)
        main_horizontal_box_layout.addLayout(button_layout)
        secondary_horizontal_box_layout.addLayout(rename_delete_layout)
        secondary_horizontal_box_layout.addWidget(layout_folder)
        vertical_layout.addLayout(main_horizontal_box_layout)
        vertical_layout.addLayout(secondary_horizontal_box_layout)
        self.setLayout(vertical_layout)
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

    def update_current_layout_label(self):
        current_layout = Application.readSetting("subwindowRecall", "currentLayout", "")
        base_name = os.path.splitext(current_layout)[0]
        layout_name = os.path.basename(base_name)

        self.current_layout_label.setText("The current layout is: " + layout_name)
