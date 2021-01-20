from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class BarChartCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        langs = ['C', 'C++', 'Java', 'Python', 'PHP']
        students = [23, 17, 35, 29, 12]
        ax = self.figure.add_subplot(111)
        ax.bar(langs, students)