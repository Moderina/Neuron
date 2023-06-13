import matplotlib
import matplotlib.pyplot as plt

class ErrorPlot:
    matplotlib.use('TkAgg')

    def __init__(self, errors):
        plt.figure()
        plt.plot(range(1, len(errors)+1), errors)

        plt.xlabel('iteracja')
        plt.ylabel('Error')
        plt.title('Error Graph')
        plt.show()

