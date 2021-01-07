"""*****************************************************************************
Programm zur Verschluesselung einer Zeichenfolge mittels Caesarverschluessellung
Jedes Zeichen wird um den Wert seines Index verschoben
alb.03.01.21
*****************************************************************************"""

def caesar(kette):
    print("Caesar-Verschluesselung wird gestartet...\n")
    #in der Variablen "verschiebung" wird der Indexwert des jeweilgen Zeichens uebergeben
    verschiebung = 1
    #Erstellen von einer Variablen zum speichern der einzelnen Werte, fuer den finalen Ausdruck
    codiert = ""
    #Verschluesselnd er einzelnen Zeichen und Ausgabe zur Kontralle der Indexvariablen / Verschiebewert
    for zeichen in kette:
        #ist es ein grosser Buchstabe?
        if zeichen.isupper():
            x = chr((ord(zeichen) + verschiebung - 65) % 26 + 65)
        else:
            x = chr((ord(zeichen) + verschiebung - 97) % 26 + 97)
        print("Verschiebewert: +", verschiebung, "\t", x)
        #Speichern der Werte in Vaiable fur den finalen Ausdruck
        codiert += x
        #Erhoehung der Indexvariablen um 1 pro Durchlauf
        verschiebung += 1
    #Ausgabe der gesammten verschluessleten Zeichenfolge
    print("\n")
    print("Die von Ihnen eingegebene Zeichenfolge wurde erfolgreich verschluesselt:\n\n",codiert, "\n")

#Eingabe der zur verschluessendlen Zeichenfolge
eingabe = input("Bitte geben Sie die Zeichenfolge ein welche Sie verschluiesseln möchten.\n"
                "Verwenden Sie bitte nur Klein- und/oder Grossbuchstaben: ")
print("\n")
#Aufruf der Funktion
caesar(eingabe)

print("-----Programm Ende-----")
