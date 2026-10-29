class Point: 
    def __init__(self, abs, ord):
        self.x=abs
        self.y=ord
    def norm(self):
        return(self.x**2+self.y**2)**(1/2)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p.norm(), Point.norm(p))

#Le code proposé va renvoyer [1], car a et b ont été définis simultanément par le même élément, ils y sont tout deux rattachés, et subissent donc simultanément les modification effectuées sur l'objet. 
class Bad:
    def __init__(self):
        self.items=[]

    def add(self, x):
        self.items.append(x)

a,b= Bad(),Bad()
a.add(1)
print(b.items)

#1) Effectivement, b voit l'élément ajouté à a pour les raisons évoquées ci-dessus. Item est un attribut de classe partagé par tous les éléments de la classe. 
#2)L'ajout d'une fonction d'initialisation permet lors de l'attribution, de créer pour chaque variable sa propre liste vide. Ces listes ayant été initialisées indépendamment, elles peuvent être modifiées séparément. 

class Tirelire:
    def __init__(self):
            self.T=[]

    def deposit(self, value: float):
        if value > 0: 
            self.T.append(value)
        else : 
            raise ValueError("...")

    def total(self):
        return sum(self.T)

    def __len__(self):
        return len(self.T)
    def __repr__(self):
            return f"Tirelire({len(self)} coins, total={self.total()})"

    
# pour tester

try:
    t = Tirelire()
    t.deposit(0.5)
    t.deposit(1)
    assert len(t) == 2
    assert t.total() == 1.5
    assert repr(t) == "Tirelire(2 coins, total=1.5)"
    other = Tirelire()
    assert len(other) == 0
    try:
        other.deposit(-1)
    except ValueError:
        pass
    else:
        raise Exception("a negative value should raise ValueError")
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#On doit créer la liste de pièces dans l'initialisation pour que deux tirelires soient indépendantes.

# votre code

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.prenom = first_name
        self.nom = last_name
        self.grades=[]

    def add_grade(self, course: str, grade: float):
        if grade >20 or grade<0: 
            raise ValueError("...")
        else :
            self.grades.append(grade)

    def __repr__(self):
        return f" {self.prenom}, {self.nom}, Grades:{self.grades}"


# pour tester

try:
    student = Student("Achille", "Talon")
    r = repr(student)
    assert isinstance(r, str), "__repr__ must return a str"
    assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
