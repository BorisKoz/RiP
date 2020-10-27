class FigureColour:

    def __init__(self):
        self._color = None

    @property
    def colourproperty(self):
        return self._color

    @colourproperty.setter
    def colourproperty(self, value):
        self._color = value