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



#On doit créer la liste de pièces dans l'initialisation pour que deux tirelires soient indépendantes.

# votre code

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.prenom = first_name
        self.nom = last_name
        self.grades=defaultdict(list)  #on créer un dictionnaire qui comprend quand on crée une nouvelle clef

    def add_grade(self, course: str, grade: float):
        if grade >20 or grade<0: 
            raise ValueError("...")
        else :
            self.grades[course].append(grade) #on ajoute les notes en les associant à la bonne matière

    def followed_topics(self):
        return self.grades.keys()

    def __repr__(self):
        return f" {self.prenom}, {self.nom}, Grades:{self.grades}"


# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

