import matplotlib
matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class QMatPlot(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.axes.set_facecolor('#FDFAF6')
        fig.patch.set_facecolor('#FFEF82')

        super(QMatPlot, self).__init__(fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.axes.plot(x, y, 'r')
        self.draw()