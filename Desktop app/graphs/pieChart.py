from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from model.backendFunctions import *

class PieChartCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        NofBatches , total_packets ,valid , invalid = stat(user_id=1)

        x = np.array([NofBatches , total_packets ,valid , invalid])
        labels = ["No Of Batched", "Total Packets", "Valid" , "Invalid"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)
