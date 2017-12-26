class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''

    # write your code here
    def __init__(self, width, height):
        self.width = width
        self.height = height
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''

    # write your code here
    def getArea(self):
        return self.width * self.height


def main():
    obj = Rectangle(3, 4)
    print(obj.getArea())


if __name__ == '__main__':
    main()
