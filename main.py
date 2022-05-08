import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow



class FuncPlotterUI(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Function Plotter")
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(QHBoxLayout())



def main():
    app = QApplication(sys.argv)
    ui = FuncPlotterUI()
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()