class Processor:
    def __init__(self):
        self.inputs = []

    def insertNumber(self, number):
        self.inputs.append(number)

    def searchNumber(self, target):
        if target in self.inputs:
            index = self.inputs.index(target) + 1
            print(index)
        else:
            print(-1)