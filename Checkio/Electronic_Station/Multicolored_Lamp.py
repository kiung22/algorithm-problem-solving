class Lamp:

    def __init__(self):
        self.lights = ['Green', 'Red', 'Blue', 'Yellow']
        self.n = -1

    def light(self):
        self.n += 1
        if self.n == 4:
            self.n -= 4
        return self.lights[self.n]
