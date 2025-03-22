import os
from krita import *
from .window_info import window_info
from .organizer import organizer

class SubwindowState(Extension):
    #Save subwindows states
    isToggled = False

    def __init__(self, parent):
        super(SubwindowState, self).__init__(parent)
        self.setup()
        
    def setup(self):
        self.isToggled = Application.readSetting("SubwindowState", "subwindowSaveToggled", "false") == "true"

        self.notifier = Application.notifier()
        self.notifier.setActive(True)
        self.notifier.viewCreated.connect(self.on_window_created)
        
        self.saveAction = self.notifier.imageSaved
         
    def on_window_created(self, window):
        
        if self.saveAction and self.isToggled:
            self.saveAction.connect(self.save_action_triggered)
        
    def save_action_triggered(self):
        doc = Krita.instance().activeDocument()
        if not self.isToggled or doc.fileName() == "":
            return  # Do nothing if the toggle is off, or the document hasn't being saved yet

        subwindow_sizes = window_info.find_sizes(self)
        subwindow_positions = window_info.find_positions(self)

       
        base_name, ext = os.path.splitext(doc.fileName())

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

    def save_event_catcher(self, toggled):
        Application.writeSetting("SubwindowState", "subwindowSaveToggled", str(toggled).lower())
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
        organizer.resizeWindows()
        
    def createActions(self, window):
        saveSubwindowAction = window.createAction("saveSubwindows", "Save Subwindows Layout", "tools/scripts")
        saveSubwindowAction.setCheckable(True)
        saveSubwindowAction.blockSignals(True)
        saveSubwindowAction.setChecked(self.isToggled)
        saveSubwindowAction.blockSignals(False)
        saveSubwindowAction.toggled.connect(self.save_event_catcher)

        loadSubwindowsAction = window.createAction("loadSubwindows", "Load Subwindows Layout", "tools/scripts")
        loadSubwindowsAction.triggered.connect(self.load_subwindows)
        
instance = SubwindowState(Application)
Scripter.addExtension(instance)
