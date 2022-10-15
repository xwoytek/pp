import kalkulatordefinicje
while True:
    print('pole kwadratu, pole prostokata, pole rownolegloboku, pole trapezu, pole trojkata, pole trojkata rownobocznego, pole kola, pole rombu')
    print('wzor pitagorasa, przekatna kwadratu, wysokosc trojkata rownobocznego, obwod kwadratu, obwod prostokata, obwod rownolegloboku, obwod trapezu, obwod trojkata, obwod trojkatarownobocznego, obwod kola, obwod rombu')
    print('objetosc szescianu, objetosc prostopadloscianu, objetosc graniastoslupa, objetosc ostroslupa, objetosc stozka, objetosc kuli')
    print('pole calkowite szescianu, pole calkowite prostopadloscianu, pole calkowite graniastoslupa, pole calkowite ostroslupa, pole calkowite walca, pole calkowite stożka, pole calkowite pckuli')
    inp = input('wybieraj: ').lower()
    if inp == 'pole kwadratu':
        kalkulatordefinicje.pkwadratu()
    elif inp == 'pole prostokata':
        kalkulatordefinicje.pprostokata()
    elif inp == 'pole rownolegloboku':
        kalkulatordefinicje.prownolegloboku()
    elif inp == 'pole trapezu':
        kalkulatordefinicje.ptrapezu()
    elif inp == 'pole trojkata':
        kalkulatordefinicje.ptrojkata()
    elif inp == 'pole trojkata rownobocznego':
        kalkulatordefinicje.ptrojkatarownobocznego()
    elif inp == 'pole kola':
        kalkulatordefinicje.pkola()
    elif inp == 'pole rombu':
        kalkulatordefinicje.prombu()
    elif inp == 'wzor pitagorasa':
        kalkulatordefinicje.pitagoras()
    elif inp == 'przekatna kwadratu':
        kalkulatordefinicje.przkwadratu()
    elif inp == 'wysokosc trojkata rownobocznego':
        kalkulatordefinicje.htrojkatarownobocznego()
    elif inp == 'obwod kwadratu':
        kalkulatordefinicje.obwkwadratu()
    elif inp == 'obwod prostokata':
        kalkulatordefinicje.obwprostokata()
    elif inp == 'obwod rownolegloboku':
        kalkulatordefinicje.obwrownolegloboku()
    elif inp == 'obwod trapezu':
        kalkulatordefinicje.obwtrapezu()
    elif inp == 'obwod trojkata':
        kalkulatordefinicje.obwtrojkata()
    elif inp == 'obwod trojkatarownobocznego':
        kalkulatordefinicje.obwtrojkatarownobocznego()
    elif inp == 'obwod kola':
        kalkulatordefinicje.obwkola()
    elif inp == 'obwod rombu':
        kalkulatordefinicje.obwrombu()
    elif inp == 'objetosc szescianu':
        kalkulatordefinicje.vszescianu()
    elif inp == 'objetosc prostopadloscianu':
        kalkulatordefinicje.vprostopadloscianu()
    elif inp == 'objetosc graniastoslupa':
        kalkulatordefinicje.vgraniastoslupa()
    elif inp == 'objetosc ostroslupa':
        kalkulatordefinicje.vostroslupa()
    elif inp == 'objetosc walca':
        kalkulatordefinicje.vwalca()
    elif inp == 'objetosc stozka':
        kalkulatordefinicje.vstozka()
    elif inp == 'objetosc kuli':
        kalkulatordefinicje.vkuli() 
    elif inp == 'pole calkowite szescianu':
        kalkulatordefinicje.pcszescianu()
    elif inp == 'pole calkowite prostopadloscianu':
        kalkulatordefinicje.pcprostopadloscianu()
    elif inp == 'pole calkowite graniastoslupa':
        kalkulatordefinicje.pcgraniastoslupa()
    elif inp == 'pole calkowite ostroslupa':
        kalkulatordefinicje.pcostroslupa()
    elif inp == 'pole calkowite walca':
        kalkulatordefinicje.pcwalca()
    elif inp == 'pole calkowite stożka':
        kalkulatordefinicje.pcstożka()
    elif inp == 'pole calkowite pckuli':
        kalkulatordefinicje.pckuli()
    print('')