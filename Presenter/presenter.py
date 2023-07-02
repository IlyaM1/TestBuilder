from abc import ABC


class Presenter(ABC):
    def __init__(self, view, model=None):
        self.view = view
        self.model = model
