import os
from krita import *
from .window_info import WindowInfo
from .organizer import Organizer
from .menu import Menu

class SubwindowRecall(Extension):
    #Save subwindows states
    isToggled = False

    def __init__(self, parent):
        super(SubwindowRecall, self).__init__(parent)
        self.setup()
        self.menu_window = None
    def setup(self):
        self.isToggled = Application.readSetting("subwindowRecall", "subwindowSaveToggled", "false") == "true"

        self.notifier = Application.notifier()
        self.notifier.setActive(True)
        self.notifier.viewCreated.connect(self.on_window_created)
        
        self.saveAction = self.notifier.imageSaved
         
    def on_window_created(self, window):
        #If the documented has saved AND the auto-save toggle is ON
        if self.saveAction and self.isToggled:
            self.saveAction.connect(self.save_action_triggered)
        
    def save_action_triggered(self):
        doc = Krita.instance().activeDocument()
        if not self.isToggled or doc.fileName() == "":
            return

        subwindow_sizes = WindowInfo.find_sizes(self)
        subwindow_positions = WindowInfo.find_positions(self)


        layout_path = Application.readSetting("subwindowRecall", "layoutDirectory", "")
        base_name, ext = os.path.splitext(doc.fileName())
        #If layout_path is not set, use the same directory as the .kra file
        if layout_path == "":
            default_file_path = base_name + ".txt"
        #Else, save the file in the layout_path with the name of the .kra file
        else:
            default_file_path = os.path.join(layout_path, os.path.basename(base_name) + ".txt")

        current_layout = Application.readSetting("subwindowRecall", "currentLayout", "")

        if current_layout and os.path.exists(current_layout):
            file_path = current_layout
        else:
            file_path = default_file_path

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
        Application.writeSetting("subwindowRecall", "currentLayout" , file_path)


    def save_event_catcher(self, toggled):
        Application.writeSetting("subwindowRecall", "subwindowSaveToggled", str(toggled).lower())
        self.isToggled = toggled

        if self.saveAction:
            try:
            # Avoid multiple instances of save_action_triggered
                self.saveAction.disconnect(self.save_action_triggered) 
               
            except TypeError:
                pass  # Ignore if it wasn't connected yet

            if self.isToggled:  #  Only connect when toggled ON
                self.saveAction.connect(self.save_action_triggered)

        
    def load_subwindows(self):
        organizer = Organizer()
        organizer.resize_windows()

    def subwindow_menu(self):
        #Avoid multiple instances of the menu
        if self.menu_window and self.menu_window.isVisible():
            self.menu_window.raise_()
            self.menu_window.activateWindow()
            return

        self.menu_window = Menu(self.isToggled, self.save_event_catcher, self.load_subwindows)
        self.menu_window.exec_()

        # When menu is closed, reset the reference
        self.menu_window = None
    #Krita naming convention requires this function to be called this name and not create_actions
    def createActions(self, window):
        saveSubwindowAction = window.createAction("saveSubwindows", "Save Subwindows Layout", "")
        saveSubwindowAction.setCheckable(True)
        saveSubwindowAction.blockSignals(True)
        saveSubwindowAction.setChecked(self.isToggled)
        saveSubwindowAction.blockSignals(False)
        saveSubwindowAction.toggled.connect(self.save_event_catcher)

        loadSubwindowsAction = window.createAction("loadSubwindows", "Load Current Layout", "")
        loadSubwindowsAction.triggered.connect(self.load_subwindows)

        SubwindowMenu = window.createAction("subwindowMenu", "SubWindow Recall", "tools/scripts")
        SubwindowMenu.triggered.connect(self.subwindow_menu)

Krita.instance().addExtension(SubwindowRecall(Krita.instance()))
