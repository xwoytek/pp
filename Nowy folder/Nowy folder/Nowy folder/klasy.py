import datetime
from random import randint
class basicdata:
    def __init__(self,imie : str,nazwisko : str,wiek : int,rok : int) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.wiek = wiek
        self.rok = rok

    def informations(self):
        print(f'hej jestem {self.__imie} {self.__nazwisko} mam {self.wiek} lat i dzis jest {self.rok} rok')

class generatorocen:
    def __init__(self,oceny_z_matemtyki : list,oceny_z_fizyki : list) -> None:
        self.oceny_z_matemtyki = oceny_z_matemtyki
        self.oceny_z_fizyki = oceny_z_fizyki

    def generuj_losowe_oceny(self):
        for i in range(5):
            self.oceny_z_matemtyki.append(randint(1,6))
            self.oceny_z_fizyki.append(randint(1,6))
        print(f'oto losowe oceny z matematyki: {self.oceny_z_matemtyki}, a oto oceny z fizyki {self.oceny_z_fizyki}')
    
    def obliczenia(self):
        for i in range(5):
            self.oceny_z_matemtyki.append(randint(1,6))
            self.oceny_z_fizyki.append(randint(1,6))
        print(f'średnia z matmy {sum(self.oceny_z_matemtyki)/len(self.oceny_z_matemtyki)} i z fizyki {sum(self.oceny_z_fizyki)/len(self.oceny_z_fizyki)}')


class deltaessasupajoljolmatmahejsuper:
    @staticmethod
    def dawajdelte(a,b,c):
        delta = b**2-4*a*c
        if delta > 0 :
            print('równanie kwadratowe ma 2 rozwiązania')
        if delta == 0:
            print('równanie kwadratowe ma 1 rozwiązanie')
        if delta < 0:
            print('równanie kwadratowe nie ma rozwiązania')