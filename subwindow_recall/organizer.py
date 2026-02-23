from krita import *
from .window_info import WindowInfo, ViewState
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import QTimer

def show_window(title, message):
    QMessageBox.information(QWidget(), title, message)

class Organizer():
    def process_subwindows(self, mdi, sizes, positions, settings, window, doc):
        def check_and_update():
            current_count = len(mdi.subWindowList())

            if current_count < len(sizes):
                # Add one subwindow
                window.addView(doc)
            elif current_count > len(sizes):
                # Remove one subwindow
                mdi.closeActiveSubWindow()
            else:
                # Stop when the count matches `sizes`
                self.resize_and_move_subwindows(mdi, sizes, positions, settings)
                return

            # Call this function again after a timer to avoid freezing the UI
            QTimer.singleShot(250, check_and_update)

        # Start the process
        check_and_update()

    def resize_windows(self):

        doc = Application.activeDocument()
        window = Application.activeWindow()
        main = window.qwindow()
        mdi = main.centralWidget().currentWidget()
        try:
            mdi.subWindowList()
        except AttributeError:
            show_window("No initial subwindow created", "Please start a document to create a subwindow first")
            return

        subwindow = mdi.currentSubWindow()
        subwindows = mdi.subWindowList()
        views = window.views()
        sizes = WindowInfo().get_sizes()
        positions = WindowInfo().get_positions()
        settings = WindowInfo().get_settings()

        if subwindow.isMaximized():
            subwindow.showNormal()

        self.process_subwindows(mdi, sizes, positions, settings, window, doc)

    def resize_and_move_subwindows(self, mdi, sizes, positions, settings):
        subwindows = mdi.subWindowList()
        views = Application.activeWindow().views()

        for i, subwindow in enumerate(subwindows):
            subwindow.resize(sizes[i])
            subwindow.move(positions[i])

        for i, view in enumerate(views):
            state = settings[i]
            canvas = view.canvas()
            canvas.setMirror(state.mirror)
            canvas.setPreferredCenter(state.center)
            canvas.setRotation(state.rotation)
            canvas.setZoomLevel(state.zoom)
