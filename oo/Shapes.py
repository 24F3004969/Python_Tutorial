class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')


class Square(Shape):
    side = 0

    def __init__(self, side):
        super().__init__('Square')
        self.side = side
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()

    def compute_area(self):
        return self.side * self.side

    def compute_perimeter(self):
        return 4 * self.side
print(Square(4).display())