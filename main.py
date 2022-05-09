import sys

from PyQt5.QtWidgets import  (
    QApplication,
    QLabel,
    QWidget,
    QHBoxLayout,
    QMainWindow,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
    QPushButton
)

from QMatPlot import QMatPlot

class FuncPlotterUI(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Function Plotter")
        self._centralWidget = QWidget(self)
        self._generalLayout = QHBoxLayout()
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self._generalLayout)

        self._createInputs()
        self._createPlot()

    def _createInputs(self):

        inputsLayout = QVBoxLayout()
        # Setting up Expression input
        self._exprInput = QLineEdit()
        exprInputFont = self._exprInput.font()
        exprInputFont.setPointSize(17)
        self._exprInput.setFont(exprInputFont)
        self._exprInput.setPlaceholderText(" F(x) to plot")
        inputsLayout.addWidget(self._exprInput)

        # Setting up Range of x inputs
        self._min_x_Input = QSpinBox()
        self._min_x_Input.setRange(-1000000, 1000000)
        minSpinBoxLayout = QHBoxLayout()
        minSpinBoxLayout.addWidget(QLabel("Minimum x:"))
        minSpinBoxLayout.addWidget(self._min_x_Input)
        inputsLayout.addLayout(minSpinBoxLayout)

        self._max_x_Input = QSpinBox()
        self._max_x_Input.setRange(-1000000, 1000000)
        self._max_x_Input.setValue(1)
        maxSpinBoxLayout = QHBoxLayout()
        maxSpinBoxLayout.addWidget(QLabel("Maximum x:"))
        maxSpinBoxLayout.addWidget(self._max_x_Input)
        inputsLayout.addLayout(maxSpinBoxLayout)

        self_plotButton = QPushButton("Plot")
        self_plotButton.clicked.connect(self.plotBtnClick)
        inputsLayout.addWidget(self_plotButton)
        
        inputsLayout.setSpacing(12)
        inputsLayout.addStretch()
        self._generalLayout.addLayout(inputsLayout)

    def _createPlot(self):
        self._plt = QMatPlot(self)
        self._generalLayout.addWidget(self._plt)

    def plotBtnClick(self):
        min_x = self._min_x_Input.text()
        max_x = self._max_x_Input.text()
        expr = self._exprInput.text()



def main():
    app = QApplication(sys.argv)
    ui = FuncPlotterUI()
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()