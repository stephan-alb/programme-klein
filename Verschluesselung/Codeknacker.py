"""*****************************************************************************
Codeknacker Programm zu Verschluesselungsprogramm
*****************************************************************************"""

#Funktion Umdrehen
def dreher_knacken(kette):
    #die laenge der urspruenglichen Zeichenkette ermittelln
    laenge = len(kette)
    laenge -= 1
    zaehler = laenge
    print("das Umdrehen ergibt:")
    while zaehler >= 0:
        print(kette[zaehler], end = " ")
        zaehler -= 1

    print("\n")
#Caesar verschluessleung knacken
def caesar_knacken(kette):
    print("Durchprobieren der Caesar-Verschluesselung")
    verschiebung = 1
    #alle Verschiebungen von 1 - 25 durchgehen
    while verschiebung <= 25:
        print("Mit der Verschiebezahl", verschiebung, " ist das Ergebnis: ", end = " ")
        #jedes zeichen um den Wert Verschiebungen
        for zeichen in kette:
            if zeichen.isupper():
                print(chr((ord(zeichen) - verschiebung - 65) % 26 + 65), end = "")
            else:
                print(chr((ord(zeichen) - verschiebung - 97) % 26 + 97), end = "")

        print(" ")

        if verschiebung % 10 == 0:
            input("Druecken Sie Enter um vortzufahren: ")
        verschiebung +=1

    print("\n")

def gartenzaun_knacken(kette):
    #eine leere Zeichenkette vereinbaren
    decodiert = ""
    #laenge der urspruenglichen Zeichenkette ermittelln
    laenge = len(kette)

    #die Mitte finden
    mitte = laenge // 2
    # wenn die Zahl ungerade ist noch 1 addieren
    if laenge % 2 != 0:
        mitte = mitte + 1

    # die Zeichenkette zerlegen
    teil1 = kette[0: mitte]
    teil2 = kette[mitte: laenge + 1]

    zaehler = 0

    #die Zeichen verteilen
    while zaehler < laenge:
        #zeichen mit einem geraden Index kommen aus der Zeichenketten
        #teil1
        if zaehler % 2 == 0:
            decodiert = decodiert + teil1[zaehler // 2]
        else:
            decodiert = decodiert + teil2[zaehler // 2]
        zaehler = zaehler + 1
        print("Der Versuch mit der Gartenzaunmethode ergibt:", decodiert)


eingabe = input("Code eingeben: ")
print("Die ursprünglichen Zeichen sind:", eingabe, "\n")

dreher_knacken(eingabe)
caesar_knacken(eingabe)
gartenzaun_knacken(eingabe)
