from Controller import Controller
from View import View

class App:
    def __init__(self):
        self.controller = Controller()


if __name__ == "__main__":
    app = App()
    app.controller.main()



