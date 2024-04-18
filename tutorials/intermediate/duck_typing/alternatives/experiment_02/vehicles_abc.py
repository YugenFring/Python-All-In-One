from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    # Enfore the necessary interface.
    # `NotImplementedError` wiil be raised if this api is not
    # be implemented.
    @abstractmethod
    def start(self):
        raise NotImplementedError("start() must be implemented")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("stop() must be implemented")

    @abstractmethod
    def drive(self):
        raise NotImplementedError("drive() must be implemented")