import sys

from main_windows import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel("O meu texto")
    label1.setStyleSheet("font-size: 160px; color: blue;")
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()

    window.show()
    app.exec()
