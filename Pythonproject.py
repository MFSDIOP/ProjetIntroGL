import math
from lib2to3.fixer_util import p1
from math import sqrt
from math import pow


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print("Point(", self.x, ",", self.y, ")")


class Cercle(Point):
    def __init__(self, p1, r):
        self.p1 = p1
        self.r = r

    def perimetre(self):
        return 2 * 3.14 * self.r

    def surface(self):
        return 3.14 * self.r

    def appartenance(self, p2):
        d=math.sqrt(math.pow((p2.x - self.p1.x), 2) + math.pow((p2.y - self.p1.y), 2))

        if d == self.r :
            print("Le point de coordonnées (", p2.x, ",", p2.y, " ) appartient au cercle");
        else:
            print("Le point  de coordonnées (",p2.x,",",p2.y," ) n'appartient pas au cercle");

    def afficher(self):
        print("Cercle(", self.p1.x, ",", self.p1.y, ",", self.r, ")")


class Cylindre(Cercle):
    def __init__(self, r, hauteur):
        Cercle.__init__(self, p1, r)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur

    def afficher(self):
        print("Le rayon du cylindre est ", self.r, "et la hauteur est", self.hauteur)


if __name__ == '__main__':
    A = Point(4, 5)
    B = Point(1, 5)
    E = Point(1, 3)
    A.afficher()
    C = Cercle(A, 3)
    per = C.perimetre()
    sur = C.surface()
    Cyl = Cylindre(3, 5)
    C.afficher()
    print("Le perimetre du cercle est", per)
    print("La surface du cercle est", sur)
    C.appartenance(B)
    C.appartenance(E)
    Cyl.afficher()
    vol = Cyl.volume()
    print("Le volume du cylindre est", vol)
