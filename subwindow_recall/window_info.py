import os
import re
from krita import *
from PyQt6.QtCore import QSize, QPoint, QPointF

class WindowInfo():

    #Save function, shared by autosave and Save As
    @staticmethod
    def write_layout(
        file_path,
        subwindow_sizes,
        subwindow_positions,
        views
    ):
        backup_file_path = file_path + "~"

        if os.path.exists(file_path):
            try:
                os.replace(file_path, backup_file_path)
            except OSError as e:
                print(f"Error renaming file for backup: {e}")

        try:
            with open(file_path, "w", encoding="utf-8") as f:

                # sizes
                for item in subwindow_sizes:
                    f.write(f"{item}\n")

                # positions
                for item in subwindow_positions:
                    f.write(f"{item}\n")

                # settings
                for view in views:
                    canvas = view.canvas()
                    if not canvas:
                        continue
                    f.write(f"mirror={canvas.mirror()}\n")

                for view in views:
                    canvas = view.canvas()
                    if not canvas:
                        continue
                    c = canvas.preferredCenter()
                    f.write(
                        f"center=PyQt6.QtCore.QPointF({c.x()}, {c.y()})\n"
                    )

                for view in views:
                    canvas = view.canvas()
                    if not canvas:
                        continue
                    f.write(f"rotation={canvas.rotation()}\n")

                for view in views:
                    canvas = view.canvas()
                    if not canvas:
                        continue
                    f.write(f"zoom={canvas.zoomLevel()}\n")

        except Exception as e:
            import traceback
            traceback.print_exc()

    #Function to find the size of all currently open subwindows from Krita

    def find_sizes(self):
        sizes = []
        window = Application.activeWindow()
        main = window.qwindow()
        mdi = main.centralWidget().currentWidget()
        subwindow = mdi.currentSubWindow()
        subwindows = mdi.subWindowList()

        for i, subwindow in enumerate(subwindows):
            sizes.append(subwindow.size())
        return sizes

    #Function to find the position of all currently open subwindows from Krita

    def find_positions(self):
        positions = []
        window = Application.activeWindow()
        main = window.qwindow()
        mdi = main.centralWidget().currentWidget()
        subwindow = mdi.currentSubWindow()
        subwindows = mdi.subWindowList()

        for i, subwindow in enumerate(subwindows):
            positions.append(subwindow.pos())
        return positions

    #Function to find the settings of all currently open subwindows from Krita

    def find_settings(self):
        states = []
        window = Application.activeWindow()

        for view in window.views():
            canvas = view.canvas()
            states.append(
                ViewState(
                    canvas.mirror(),
                    canvas.preferredCenter(),
                    canvas.rotation(),
                    canvas.zoomLevel()
                    )
                )
        return states

    #Functions to recall size/position from a existing .txt stored in the same directory as the .kra file

    def get_sizes(self):
        sizes = []
        pattern = re.compile(r"PyQt6\.QtCore\.QSize\((\d+), (\d+)\)")
        doc = Application.activeDocument()

        currentLayout = Application.readSetting("subwindowRecall", "currentLayout", "")
        base_name, ext = os.path.splitext(doc.fileName())
        #If currentLayout is not set, search for the .txt in the file directory
        if currentLayout == "":
            file_path = base_name + ".txt"
        #Else, use the currentLayout
        else:
            file_path = currentLayout

        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    lines = f.read().splitlines()
                    for line in lines:
                        match = pattern.match(line)
                        if match:
                            width, height = map(int, match.groups())
                            sizes.append(QSize(width, height))

            except Exception as e:
                print(f"Error reading file: {e}")
        return sizes

    def get_positions(self):
        positions = []
        pattern = re.compile(r"PyQt6\.QtCore\.QPoint\((\d+), (\d+)\)")
        doc = Application.activeDocument()

        currentLayout = Application.readSetting("subwindowRecall", "currentLayout", "")
        base_name, ext = os.path.splitext(doc.fileName())
        #If currentLayout is not set, search for the .txt in the file directory
        if currentLayout == "":
            file_path = base_name + ".txt"
        #Else, use the currentLayout
        else:
            file_path = currentLayout

        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    lines = f.read().splitlines()
                    for line in lines:
                        match = pattern.match(line)
                        if match:
                            width, height = map(int, match.groups())
                            positions.append(QPoint(width, height))
                        elif line =="PyQt6.QtCore.QPoint()":
                            positions.append(QPoint(0, 0))
            except Exception as e:
                print(f"Error reading file: {e}")
        return positions

    def get_settings(self):
        mirrors = []
        centers = []
        rotations = []
        zooms = []

        mirror_pattern = re.compile(r"mirror=(True|False)")
        center_pattern = re.compile(r"center=PyQt6\.QtCore\.QPointF\(([-\d.]+), ([-\d.]+)\)")
        rotation_pattern = re.compile(r"rotation=([-\d.]+)")
        zoom_pattern = re.compile(r"zoom=([-\d.]+)")

        doc = Application.activeDocument()

        currentLayout = Application.readSetting("subwindowRecall", "currentLayout", "")
        base_name, ext = os.path.splitext(doc.fileName())
        #If currentLayout is not set, search for the .txt in the file directory
        if currentLayout == "":
            file_path = base_name + ".txt"
        #Else, use the currentLayout
        else:
            file_path = currentLayout

        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    lines = f.read().splitlines()
                    settings_start = next(
                        (i for i, l in enumerate(lines) if l.startswith("mirror=")), None
                    )
                    if settings_start is None:
                        return mirrors, centers, rotations, zooms

                    for line in lines[settings_start:]:
                        if m := mirror_pattern.match(line):
                            mirrors.append(m.group(1) == "True")

                        elif m := center_pattern.match(line):
                            x, y = map(float, m.groups())
                            centers.append(QPointF(x, y))

                        elif m := rotation_pattern.match(line):
                            rotations.append(float(m.group(1)))

                        elif m := zoom_pattern.match(line):
                            zooms.append(float(m.group(1)))

            except Exception as e:
                print(f"Error reading settings: {e}")

            return [
                ViewState(m, c, r, z)
                for m, c, r, z in zip(mirrors, centers, rotations, zooms)
            ]

class ViewState:

    def __init__(self, mirror, center, rotation, zoom):
        self.mirror = mirror
        self.center = center
        self.rotation = rotation
        self.zoom = zoom
