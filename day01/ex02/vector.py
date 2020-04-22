class Vector:
    def __init__(self, init):
        self.values = None
        self.size = None
        self.set_atributes(init)

    def set_atributes(self, init):
        if type(init) is list:
            self.values = init
            self.size = len(init)
        elif type(init) == int:
            l = []
            for i in range(init):
                l.append(float(i))
            self.values = l
            self.size = len(l)
        elif type(init) == tuple:
            l = []
            for i in range(init[0], init[1]):
                l.append(float(i))
            self.values = l
            self.size = len(l)

v1 = Vector([1.0, 2.0, 3.5])
v2 = v1 * 5
v3 = Vector((1,6))
print(v1)
print(v1.values)
print(v2)
print(v2.values)
print(v3)
print(v3.values)
