import os

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
