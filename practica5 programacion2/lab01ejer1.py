class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, o):
        return Vector(self.x +o.x,self.y+o.y,self.z+o.z)
    def __str__(self):
        return f"({self.x},{self.y},{self.z}"
v1= Vector(3,4,5)
v2=Vector(1,2,3)
resultado=v1+v2
print(f"la suma de {v1}y{v2}es {resultado}")