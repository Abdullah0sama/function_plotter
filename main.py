import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  (
    QApplication,
    QLabel,
    QWidget,
    QHBoxLayout,
    QMainWindow,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
    QPushButton,
    QMessageBox
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
        self._centralWidget.setObjectName('centralWidget')
        self._centralWidget.setStyleSheet('#centralWidget{ background-color:#FFEF82; }')
        self._centralWidget.setMinimumSize(1000, 540)
        self._generalLayout.setContentsMargins(0,0,0,0) 

        self._createInputs()
        self._createPlot()

    def _createInputs(self):

        inputsLayout = QVBoxLayout()
        # Setting up Expression input
        self._exprInput = QLineEdit()
        self._exprInput.setPlaceholderText(" F(x) to plot")
        self._exprInput.setStyleSheet('background-color: #E4EFE7; font-size: 18px;')
        inputsLayout.addWidget(self._exprInput)

        # Setting up Range of x inputs
        self._min_x_Input = QSpinBox()
        self._min_x_Input.setRange(-1000000, 1000000)
        self._min_x_Input.setStyleSheet('background-color: #E4EFE7; font-size:15px;')
        minSpinBoxLayout = QHBoxLayout()
        minLabel = QLabel("Minimum x:")
        minLabel.setStyleSheet('font-size: 15px;')
        minSpinBoxLayout.addWidget(minLabel)
        minSpinBoxLayout.addWidget(self._min_x_Input)
        inputsLayout.addLayout(minSpinBoxLayout)

        self._max_x_Input = QSpinBox()
        self._max_x_Input.setRange(-1000000, 1000000)
        self._max_x_Input.setValue(1)
        self._max_x_Input.setStyleSheet('background-color: #E4EFE7; font-size:15px;')
        maxSpinBoxLayout = QHBoxLayout()
        maxLabel = QLabel("Maximum x:")
        maxLabel.setStyleSheet('font-size: 15px;')
        maxSpinBoxLayout.addWidget(maxLabel)
        maxSpinBoxLayout.addWidget(self._max_x_Input)
        inputsLayout.addLayout(maxSpinBoxLayout)

        self._plotButton = QPushButton("Plot")
        self._plotButton.clicked.connect(self.plotBtnClick)
        inputsLayout.addWidget(self._plotButton)
        btnFont = self._plotButton.font()
        btnFont.setBold(True)
        btnFont.setPointSize(13)
        self._plotButton.setFont(btnFont)
        self._plotButton.setStyleSheet('background-color: #EFD345; color: #383838')


        self._alertLabel = self._createAlertLabelWidget()
        inputsLayout.addWidget(self._alertLabel)
        
        inputsLayout.setSpacing(12)
        inputsLayout.addStretch()

        inputsLayout.setContentsMargins(10, 15, 10, 10)
        self._generalLayout.addLayout(inputsLayout, 2)
            
    def _createPlot(self):
        self._plt = QMatPlot(self)
        self._generalLayout.addWidget(self._plt, 3)

    def _createAlertLabelWidget(self):
        alertLabel = QLabel()
        alertLabel.setStyleSheet('color: #FF1700; font-size:14px;')
        alertLabel.setAlignment(Qt.AlignCenter)
        return alertLabel

    def _hideAlert(self):
        self._alertLabel.hide()

    def _showAlert(self, msg):
        self._alertLabel.show()
        self._alertLabel.setText(msg)

    def plotBtnClick(self):
        min_x = int(self._min_x_Input.text())
        max_x = int(self._max_x_Input.text())
        expr = self._exprInput.text()   
        if min_x >= max_x:
            self._showAlert('Minimum x should be less then maximum x')

def main():
    app = QApplication(sys.argv)
    ui = FuncPlotterUI()
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()