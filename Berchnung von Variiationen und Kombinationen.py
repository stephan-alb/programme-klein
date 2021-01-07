"""****************************************************************************
Berechnung von Variationen und Kombinationen
alb.05.01.21
*****************************************************************************"""
# n 'hoch' k
def variation_berechnen(n, k):
    # variable zur potentierung setzen
    f = n
    # potentierung
    while k-1 > 0:
        n = f * n
        k -= 1
    print()
    print("Zu Ihren Eingaben gibt es ", n , " Variationen.")

# n! / (n - k)!
def variation_wiederholung(n, k):
    # variable (n - k)
    nk = n - k
    # Liste fuer fakultäten n! erstellen
    liste_variationen =[]
    #index variable
    i = 0
    y = 1
    #Fakultät n
    while n > 0:
        liste_variationen.append(n)
        n -= 1
    #Laenge der Liste ermitteln Fakultät n!
    z = len(liste_variationen)
    # multiplizieren der Listenelemente
    while i < (z-1):
        x = liste_variationen[i] * liste_variationen[i+1]
        y = x * y
        i += 2

    liste_kombinationen =[]
    #index variable
    ii = 0
    yy = 1
    #Fakultät nk
    while nk > 0:
        liste_kombinationen.append(nk)
        nk -= 1
    #Laenge der Liste ermitteln Fakultät nk!
    zz = len(liste_kombinationen)
    # multiplizieren der Listenelemente
    while ii < (zz-1):
        xx = liste_kombinationen[ii] * liste_kombinationen[ii+1]
        yy = xx * yy
        ii += 2
    fact = y / yy

    print()
    print("Zu Ihren Eingaben gibt es ", fact, " Variationen.")

# n! / (k! * (n - k)!)
def kombination_ohne_wiederholung(n, k):
    # variable (n - k)
    nk = n - k
    liste_variationen = []
    i = 0
    y = 1
    #Fakultät n
    while n > 0:
        liste_variationen.append(n)
        n -= 1
    #Laenge der Liste ermitteln Fakultät n!
    z = len(liste_variationen)
    # multiplizieren der Listenelemente
    while i < (z-1):
        x = liste_variationen[i] * liste_variationen[i+1]
        y = x * y
        i += 2

    liste_kombinationen =[]
    #durchlaufvariable
    ii = 0
    yy = 1
    #Fakultät nk
    while nk > 0:
        liste_kombinationen.append(nk)
        nk -= 1
    #Laenge der Liste ermitteln Fakultät nk!
    zz = len(liste_kombinationen)
    # multiplizieren der Listenelemente
    while ii < (zz-1):
        xx = liste_kombinationen[ii] * liste_kombinationen[ii+1]
        yy = xx * yy
        ii += 2

    liste_kombinationen_2 =[]
    #durchlaufvariable
    iii = 0
    yyy = 1
    #Fakultät nk
    while k > 0:
        liste_kombinationen_2.append(k)
        k -= 1
    #Laenge der Liste ermitteln Fakultät nk!
    zzz = len(liste_kombinationen_2)
    # multiplizieren der Listenelemente
    while iii < (zzz-1):
        xxx = liste_kombinationen_2[iii] * liste_kombinationen_2[iii+1]
        yyy = xxx * yyy
        iii += 2
    #Formel ausrechnen
    fact = y / (yy*yyy)

    print()
    print("Zu Ihren Eingaben gibt es ", fact, " Kombinationen.")

# (n + k - 1)! / (k! * (n - k)!)
def kombination_mit_wiederholung(n, k):
    #  n + k - 1
    nk = n + k - 1
    liste_variationen = []
    i = 0
    y = 1
    #Fakultät y (n)
    while nk > 0:
        liste_variationen.append(nk)
        nk -= 1
    #Laenge der Liste ermitteln Fakultät n!
    z = len(liste_variationen)
    # multiplizieren der Listenelemente
    while i < (z-1):
        x = liste_variationen[i] * liste_variationen[i+1]
        y = x * y
        i += 2

    # Binominalkoeffizient n - k in diesem Falle y - k da "n" = n + k -1
    nk2 = n + k - 1 - k
    liste_kombinationen =[]
    #durchlaufvariable
    ii = 0
    yy = 1
    #Fakultät nk
    while nk2 > 0:
        liste_kombinationen.append(nk2)
        nk2 -= 1
    #Laenge der Liste ermitteln Fakultät nk!
    zz = len(liste_kombinationen)
    # multiplizieren der Listenelemente
    while ii < (zz-1):
        xx = liste_kombinationen[ii] * liste_kombinationen[ii+1]
        yy = xx * yy
        ii += 2

    liste_kombinationen_2 =[]
    #durchlaufvariable
    iii = 0
    yyy = 1
    #Fakultät nk
    while k > 0:
        liste_kombinationen_2.append(k)
        k -= 1
    #Laenge der Liste ermitteln Fakultät nk!
    zzz = len(liste_kombinationen_2)
    # multiplizieren der Listenelemente
    while iii < (zzz-1):
        xxx = liste_kombinationen_2[iii] * liste_kombinationen_2[iii+1]
        yyy = xxx * yyy
        iii += 2
    #Formel ausrechnen
    fact = y / (yy*yyy)

    print(y, yy, yyy)
    print()
    print("Zu Ihren Eingaben gibt es ", fact, " Kombinationen.")

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
        kombination_ohne_wiederholung(elemente, variation)
        print("-------------------------------------------------------\n")
        programm_start()
    if auswahl == 4:
        kombination_mit_wiederholung(elemente, variation)
        print("-------------------------------------------------------\n")
        programm_start()
    else:
        print("Das war nichts")
        print("-------------------------------------------------------\n")
        programm_start()

programm_start()
