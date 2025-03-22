from krita import *
from .window_info import window_info


class organizer():
    def resizeWindows():
        # [print([a.objectName(), a.text()]) for a in Krita.instance().actions()]
        sizes = window_info().get_sizes()
        positions = window_info().get_positions()
        doc = Application.activeDocument()
        window = Application.activeWindow()
        main = window.qwindow()
        mdi = main.centralWidget().currentWidget()
        doc.save
        subwindow = mdi.currentSubWindow()
        subwindows = mdi.subWindowList()

        if len(subwindows) > len(sizes):
            raise ValueError("Not enough sizes provided for all subwindows, please reduce the amount of subwindows or create a new save for the current subwindow count")
            
        if len(subwindows) < len(sizes):
            raise ValueError("Not enough subwindows provided for all sizes, please increase the amount of subwindows or create a new save for the current subwindow count")

        for i, subwindow in enumerate(subwindows):
            index = i
            subwindow.resize(sizes[index])
            subwindow.move(positions[index])

