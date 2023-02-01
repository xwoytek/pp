from random import randint
class basicdata:
    def __init__(self,imie : str,nazwisko : str,wiek : int,rok : int) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.wiek = wiek
        self.rok = rok
        self.oceny = generatorocen.generuj_losowe_oceny()

    def informations(self):
        print(f'hej jestem {self.__imie} {self.__nazwisko} mam {self.wiek} lat i dzis jest {self.rok} rok i moje oceny to')
        print(self.oceny)
class generatorocen():
    def __init__(self,oceny_z_matemtyki : list,oceny_z_fizyki : list) -> None:
        self.oceny_z_matemtyki = oceny_z_matemtyki
        self.oceny_z_fizyki = oceny_z_fizyki
        
    def generuj_losowe_oceny():
        oceny_z_matemtyki = []
        oceny_z_fizyki = []
        for i in range(5):
            oceny_z_matemtyki.append(randint(1,6))
            oceny_z_fizyki.append(randint(1,6))
        print(f'oceny z matmy: {oceny_z_matemtyki} oceny z fizyki: {oceny_z_fizyki}')
    
    @staticmethod
    def obliczenia():
        oceny_z_matemtyki = []
        oceny_z_fizyki = []
        for i in range(5):
            oceny_z_matemtyki.append(randint(1,6))
            oceny_z_fizyki.append(randint(1,6))
        print(f'średnia z matmy {sum(oceny_z_matemtyki)/len(oceny_z_matemtyki)} i z fizyki {sum(oceny_z_fizyki)/len(oceny_z_fizyki)}')


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