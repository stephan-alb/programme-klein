"""****************************************************************************
Berechnung von Variationen und Kombinationen
alb.05.01.21
*****************************************************************************"""
def variation_berechnen(n, k):
    f = n
    while k-1 > 0:
        n = f * n
        k -= 1
    print()
    print("Zu Ihren Eingaben gibt es ", n , " Variationen.")

def variation_wiederholung(n, k):
    nk = n - k
    liste_variationen =[]
    i = 0
    y = 1
    while n > 0:
        liste_variationen.append(n)
        n -= 1
    z = len(liste_variationen)
    while i < (z-1):
        x = liste_variationen[i] * liste_variationen[i+1]
        y = x * y 
        i += 2
    
    liste_kombinationen =[]
    ii = 0
    yy = 1
    while nk > 0:
        liste_kombinationen.append(nk)
        nk -= 1
    zz = len(liste_kombinationen)
    while ii < (zz-1):
        xx = liste_kombinationen[ii] * liste_kombinationen[ii+1]
        yy = xx * yy 
        ii += 2    
    fact = y / yy 
    
    print()  
    print("Zu Ihren Eingaben gibt es ", fact, " Variationen.")

def kombination_wiederholung(n, k):
    nk = n - k
    liste_variationen =[]
    i = 0
    y = 1
    while n > 0:
        liste_variationen.append(n)
        n -= 1
    z = len(liste_variationen)
    while i < (z-1):
        x = liste_variationen[i] * liste_variationen[i+1]
        y = x * y 
        i += 2
    
    liste_kombinationen =[]
    ii = 0
    yy = 1
    while nk > 0:
        liste_kombinationen.append(nk)
        nk -= 1
    zz = len(liste_kombinationen)
    while ii < (zz-1):
        xx = liste_kombinationen[ii] * liste_kombinationen[ii+1]
        yy = xx * yy 
        ii += 2    
    
    liste_kombinationen_2 =[]
    iii = 0
    yyy = 1
    while k > 0:
        liste_kombinationen_2.append(k)
        k -= 1
    zzz = len(liste_kombinationen_2)
    while iii < (zzz-1):
        xxx = liste_kombinationen_2[iii] * liste_kombinationen_2[iii+1]
        yyy = xxx * yyy 
        iii += 2    
    
    fact = y / (yy*yyy) 
    
    print() 
    print("Zu Ihren Eingaben gibt es ", fact, " Variationen.")

#def kombination_mit wiederholung

def programm_start():
    print("Programm zur Berechnung von Variationen und Kombinationen\n")
    print("Bitte wählen Sie welche Berechnung Sie vornehmen möchten:\n"
          "1 - Variationen ohne Wiederholung\n"
          "2 - Variationen mit Wiederholung\n"
          "3 - Kombination ohne Wiederholung\n"
          "4 - Kombination mit Wiederholung (noch nicht verfügbar)\n")
    auswahl = int(input("Bitte wählen Sie durch Eingabe der entsprechenden Ziffer: "))
    
    elemente = float(input("Bitte geben Sie die Anzahl der Elemente ein: "))
    variation = float(input("Wieviele Möglichkeiten sollen berechnet werden? "))

    if auswahl == 1:
        variation_berechnen(elemente, variation)
        print("-------------------------------------------------------\n")
        programm_start()
    if auswahl == 2:
        variation_wiederholung(elemente, variation)
        print("-------------------------------------------------------\n")
        programm_start()
    if auswahl == 3:
        kombination_wiederholung(elemente, variation)
        print("-------------------------------------------------------\n")
        programm_start()
    if auswahl == 4:
        print("Diese Funktion steht bald zur Verfügung")
        print("-------------------------------------------------------\n")
        programm_start()
    else:
        print("Das war nichts")
        print("-------------------------------------------------------\n")
        programm_start()

programm_start()