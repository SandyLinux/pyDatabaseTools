class Shape:
    def __init__(self, name):
        self.name = name
        print('new shape is created')
    def __call__(self,name):
        print('the shape is :', name, self.name)


s = Shape('test1')
s1 = s
s2 = s

s('another')
s1('two')
s2('three')