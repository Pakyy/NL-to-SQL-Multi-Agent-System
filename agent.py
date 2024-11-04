class Agent:
    def __init__(self, name):
        self.name = name

    def process(self, input_data):
        raise NotImplementedError("Subclasses should implement this method")