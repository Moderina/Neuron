import random

class Perceptron:

    def __init__(self):
        self.bias = 0.0
        self.errors = []
        # self.input1 = [[point.x, point.y] for point in data1.PointsList]
        # self.input2 = [[point.x, point.y] for point in data2.PointsList]
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]

        self.learning_rate = 0.1
        # self.weighted_sum = sum(x * w for x, w in zip())

    # @staticmethod
    def train(self, list1, list2, num_epochs):
        training_data = self.convertToTrainingData(list1, list2)
        self.errors = []
        for _ in range(num_epochs):
            for inputs, label in training_data:
                prediction = self.predict(inputs)
                error = label - prediction
                self.errors.append(error)
                self.weights = [w + self.learning_rate * error * x for x, w in zip(inputs, self.weights)]
                weighted_sum = sum(x * w for x, w in zip(inputs, self.weights)) + self.bias
                self.bias += self.learning_rate * error
                yield inputs[0], inputs[1], self.weights[0], self.weights[1], weighted_sum, prediction

    def predict(self, inputs):
        weighted_sum = sum(x * w for x, w in zip(inputs, self.weights)) + self.bias
        return 1 if weighted_sum >=0 else 0
    
    def convertToTrainingData(self, list1, list2):
        data = []
        for coords in list1:
            data.append(tuple(([coords.x, coords.y], 0)))
        for coords in list2:
            data.append(tuple(([coords.x, coords.y], 1)))
        return data
    
    def Clear(self):
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.bias = 0.0


