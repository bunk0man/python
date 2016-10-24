class numOps(object):
    """docstring for numOps"""
    def __init__(self, num1, num2):
        super(numOps, self).__init__()
        self.one = float(num1)
        self.two = float(num2)
        print '%f' % self.one, ', %f' % self.two

    def add(self):
        print 'Sum: %0.2f' % (self.one + self.two)

    # def __add__(self):
    #     print 'Sum: %0.2f' % (self.one + self.two)

x = numOps(3,4)
x.add()