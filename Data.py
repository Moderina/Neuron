import random

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print(self.x, self.y)
        # print(type(self.x), type(self.y))

class Data:

    def __init__(self, data=""):
        self.PointsList = []
        self.data = data;
        if(data != ""):
            self.splitData(self.data)

    def setData(self, data):
        self.PointsList.clear()
        self.data = data;
        self.splitData(self.data)

    def splitData(self, data):
        x = ''
        y = '' 
        for z in data:
            if(z == ' '): continue
            if(z == ','):
                x = float(x)
                continue
            if(z == '\n'):
                y = float(y)
                self.PointsList.append(Point(x, y))
                x = ''
                y = ''
                continue
            if(isinstance(x, float)):
                y = y + z;
            else:
                x = x + z;
        if(data[-1] != '\n'):
            y = float(y)
            self.PointsList.append(Point(x, y))

    def generatePoints(self, num):
        count = 0;
        self.PointsList.clear()
        random.seed()
        while(count < num):
            self.PointsList.append(
                Point(
                    random.randint(-1000, 1000)/100,
                    random.randint(-1000, 1000)/100
                )
            )
            count += 1
        return self.getPointsList()

    def getPointsList(self):
        string = ""
        for point in self.PointsList:
            string = string + str(point.x) + ", " + str(point.y) + '\n'
        return string
