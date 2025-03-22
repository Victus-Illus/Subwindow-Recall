import os
import re
from krita import *
from PyQt5.QtCore import QSize, QPoint



class window_info():

    #Functions to grab the size/position of all currently opened subwindows
    
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

    #Functions to recall size/position from a existing .txt stored in the same directory as the .kra file

    def get_sizes(self):
        sizes = []
        pattern = re.compile(r"PyQt5\.QtCore\.QSize\((\d+), (\d+)\)")
        doc = Application.activeDocument()
        base_name, ext = os.path.splitext(doc.fileName())
        file_path = base_name + ".txt"
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
        pattern = re.compile(r"PyQt5\.QtCore\.QPoint\((\d+), (\d+)\)")
        doc = Application.activeDocument()
        base_name, ext = os.path.splitext(doc.fileName())
        file_path = base_name + ".txt"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    lines = f.read().splitlines()
                    for line in lines:
                        match = pattern.match(line)
                        if match:
                            width, height = map(int, match.groups())
                            positions.append(QPoint(width, height))                  
                        elif line =="PyQt5.QtCore.QPoint()":
                            positions.append(QPoint(0, 0))
            except Exception as e:
                print(f"Error reading file: {e}")
        return positions
