"""*****************************************************************************
Ein einfaches Verschluesselungsprogramm*****************************************
1 Umdrehung des Textes - 2 Numerische Verschluesselung Ausgabe des Ascii Wertes
3 Caesar Verschluesselung - 4 Gartenzaunverschluesselung mit 2 Zeilen***********
*****************************************************************************"""

# 1 Funktion zum umdrehen
def dreher(kette):
    #laenge der ursprünglichen Zeichenkette ermitteln
    laenge = len(kette)
    #len liefert die "echte" Menge, daher muss 1 abgezogen werden
    laenge = laenge - 1
    # Zaehler fuer die Ausgabe
    zaehler = laenge

    print("Verschlüsselung durch Umdrehen")
    #due Zeichen von hinten nach vorne ausgeben
    while zaehler >= 0:
        print(kette[zaehler], end = "")
        zaehler = zaehler - 1
    print("\n")

#Die Funktion zum Ausgeben des numerischen Wertes in Ascii Zeichenkette
def ascii_code(kette):
    print("Verschlüsselung durch ASCII Ausgabe")
    #Fuer jedes Zeichen ueber ord() den Ascii Wert Ausgeben
    for zeichen in kette:
        print(ord(zeichen), end = " ")

    print("\n")

#Funktion zur Caesar Verschluesselung
def caesar(kette):
    print("Caesar-Verschluesselung")
    verschiebung = int(input("Bitte Verschiebung eingeben: "))
    #Jedes Zeichen um den angebenen Wert verschieben
    for zeichen in kette:
        #ist es ein grosser Bucuhstabe?
        if zeichen.isupper():
            print(chr((ord(zeichen) + verschiebung - 65) % 26 + 65), end = "")
        else:
            print(chr((ord(zeichen) + verschiebung - 97) % 26 + 97), end = "")
    print("\n")

#Funktion zur Gartenzaunverschluesselung
def gartenzaun(kette):
    # zwei leere Zeichenketten vereinbaren
    teil1 = ""
    teil2 = ""

    #die laenge der urspruenglichen Zeichenkette ermittelln
    laenge = len(kette)
    #für den Index
    zaehler = 0

    #die zeichen verteilen
    while zaehler < laenge:
        #Zeichen mit einem geraden Indey kommen in die Zeichenkette teil1
        if zaehler % 2 == 0:
            teil1 = teil1 + kette[zaehler]
        #Ungerader Index = teil2
        else:
            teil2 = teil2 + kette[zaehler]
        zaehler = zaehler + 1

    # Die beiden Zeichenketten wieder zusammenbauen
    codiert = teil1 + teil2

    #ausgeben
    print("Die obere Haelfte: ", teil1)
    print("Die untere Haelfte: ", teil2)
    print("Das komplette Wort ist: ", codiert)

#Die ursprünfliche Zeichenkette einlesen
eingabe = input("Bitte geben Sie eine Zeichenkette ein: ")
print("Die ursprünfliche Zeichenkette ist:\n", eingabe, "\n")

#Die Verschluesselung durchfuehren
dreher(eingabe)
ascii_code(eingabe)
caesar(eingabe)
gartenzaun(eingabe)
