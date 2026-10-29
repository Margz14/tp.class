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

#1)Après test, les deux commandes sont identiques, le chemin (ordre des étapes)est différent, mais les étapes sont les mêmes.
#2) Il y a un problème d'arguments. 
#3) quand repr n'est pas défini, python renvoie l'objet avec le nom qu'il utilise pour le stocker, donc une série de caractères qui ne correspond pas au nom qu'on a donné à l'objet.