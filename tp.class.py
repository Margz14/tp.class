class Point: 
    def __init__(self, abs, ord):
        self.x=abs
        self.y=ord
    def norm(self):
        return(self.x**2+self.y**2)**(1/2)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# pour tester

try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
