from abc import ABC, abstractmethod

class FigureAbstract(ABC):
    figure_type = 'NaN'

    @abstractmethod
    def area(self):
        pass
