import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Plot:
    matplotlib.use('TkAgg')

    def __init__(self, list1, list2, m=None, b=None):
        self.m = m
        self.b = b
        self.xpoints1, self.ypoints1 = self.convertList(list1)
        self.xpoints2, self.ypoints2 = self.convertList(list2)

        plt.figure()
        plt.scatter(self.xpoints1, self.ypoints1, c='red', marker='o')
        plt.scatter(self.xpoints2, self.ypoints2, c='blue', marker='o')

        if(self.m != None and self.b != None):
            x = np.linspace(-10, 10, 1000)
            y = self.f(x)
            plt.plot(x, y)


        plt.show()

    def convertList(self, list):
        xlist = []
        ylist = []
        for point in list:
            xlist.append(point.x)
            ylist.append(point.y)
        return xlist, ylist
    
    def f(self, x):
        return x * self.m + self.b

