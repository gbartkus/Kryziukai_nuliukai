# Masyvas, sukuriantis reikšmes X ir O
def zaidimas():
    global lenta, zaidejas, zaidimo_statusas
    lenta = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Sukuriamas masyvas su 10 tuščių langelių
    zaidejas = 1
    zaidimo_statusas = veikia

    # Kryžiukų nuliukų lentos išdėstymas
    def LentosPiesimas():
        for i in range(1, 10):
            if lenta[i] == ' ':
                print(f" {i} ", end="")
            else:
                print(f" {lenta[i]} ", end="")

            if i % 3 == 0:
                print("\n---|---|---")
            else:
                print("|", end="")

    # Tikrinama ar laisva vieta
    def Tikrinimas(x):
        return lenta[x] == ' '

    # Nustatomos žaidimo galimos baigtys
    def Pergale():
        global zaidimo_statusas
        for i in range(1, 4):
            if lenta[i * 3 - 2] == lenta[i * 3 - 1] == lenta[i * 3] and lenta[i * 3 - 2] != ' ':
                zaidimo_statusas = pergale
        for i in range(1, 4):
            if lenta[i] == lenta[i + 3] == lenta[i + 6] and lenta[i] != ' ':
                zaidimo_statusas = pergale
        if lenta[1] == lenta[5] == lenta[9] and lenta[1] != ' ':
            zaidimo_statusas = pergale
        if lenta[3] == lenta[5] == lenta[7] and lenta[3] != ' ':
            zaidimo_statusas = pergale
        if all(lenta[i] != ' ' for i in range(1, 10)):
            zaidimo_statusas = lygiosios

    print("Kryžiukų nuliukų programa")
    print("Pirmas žaidėjas [X] - Antras žaidėjas [O]\n")

    while zaidimo_statusas == veikia:
        # Pirmo žaidėjo nustatymas
        zyme = 'X' if zaidejas % 2 != 0 else 'O'
        print(f"Žaidėjo ({zyme}) ejimas ")

        # X ir O pasirinkimo vieta
        pasirinkimas = int(input("Pažymėkite poziciją nuo 1 iki 9: "))
        if Tikrinimas(pasirinkimas):
            lenta[pasirinkimas] = zyme
            zaidejas += 1
            Pergale()

            # Atspausdiname lentą po kiekvieno ėjimo
            LentosPiesimas()

            if zaidimo_statusas == lygiosios:
                print("Lygiosios!")
            elif zaidimo_statusas == pergale:
                print(f"Žaidėjas {zyme} laimėjo!")
        else:
            print("Pasirinkta vieta užimta, bandykite dar kartą!")

# Pagrindinė programa
veikia = 0
pergale = 1
lygiosios = -1

while True:
    zaidimas()  # Pradėti žaidimą
    # Klausimas, ar norima žaisti dar kartą
    paklausti = input("Ar norite žaisti dar kartą? (t/n): ").strip().lower()
    if paklausti != 't':
        print("Ačiū, kad žaidėte!")
        break