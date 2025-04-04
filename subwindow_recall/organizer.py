from krita import *
from .window_info import WindowInfo
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QTimer

def show_window(title, message):
    QMessageBox.information(QWidget(), title, message)

class Organizer():
    def process_subwindows(self, mdi, sizes, positions, window, doc):
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
                self.resize_and_move_subwindows(mdi, sizes, positions)
                return

            # Call this function again after 250ms
            QTimer.singleShot(250, check_and_update)

        # Start the process
        check_and_update()

    def resize_windows(self):
        sizes = WindowInfo().get_sizes()
        positions = WindowInfo().get_positions()
        doc = Application.activeDocument()
        window = Application.activeWindow()
        main = window.qwindow()
        mdi = main.centralWidget().currentWidget()
        subwindow = mdi.currentSubWindow()
        subwindows = mdi.subWindowList()

        if not subwindows:
            show_window("No initial subwindow created", "Please start a document to create a subwindow first")
            return

        if subwindow.isMaximized():
            subwindow.showNormal()

        self.process_subwindows(mdi, sizes, positions, window, doc)

    def resize_and_move_subwindows(self, mdi, sizes, positions):
        subwindows = mdi.subWindowList()
        for i, subwindow in enumerate(subwindows):
            subwindow.resize(sizes[i])
            subwindow.move(positions[i])
