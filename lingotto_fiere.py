import csv
class LingottoFiere:
    def __init__(self, nome):
        self.nome = nome
        self.stands = []
        self.exhibitors = []

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cod = row[0]
                codid = cod[:-1]

                if codid == "ST":
                    codStand = cod
                    sq = int(row[1])
                    pavilion = int(row[2])
                    g=row[4].isdigit()
                    if row[4] == "unset":
                        price = int(row[3])
                        s = Standard(codStand, sq, pavilion, price)
                    elif g:
                        price = int(row[3])
                        s= Plus(codStand, sq, pavilion, price, int(row[4]))
                    else:
                        price = int(row[3])
                        s= Premium(codStand, sq, pavilion, price, row[4])
                    self.stands.append(s)
                elif codid == "ES":
                    codEx = row[0]
                    name = row[1]
                    surname = row[2]
                    e = Exhibitor(codEx, name, surname)
                    self.exhibitors.append(e)

                else:
                    print(f"{cod} non valido")
    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        stand = next((s for s in self.stand_list if s.codice == codice_stand), None)
        espositore = next((e for e in self.espositori_list if e.codice == codice_espositore), None)

        # 2. Verifica che entrambi esistano
        if not stand or not espositore:
            raise ValueError("Stand o espositore non esistenti.")

        # 3. Altre verifiche (es. disponibilità dello stand, l'espositore ha già uno stand, ecc.)
        if not stand.stAssigned:
            raise ValueError("Lo stand non è disponibile.")

        if espositore.exAssigned():  # Esempio di controllo logico
            raise ValueError("L'espositore ha già uno stand assegnato.")

        # 4. Effettua l'assegnazione
        stand.assegna_a(espositore)

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO

class Stand :
    def __init__(self, codStand, sq, pavilion):
        self.codStand = codStand
        self.sq = sq
        self.pavilion = pavilion
        self.exAssigned = None

    def __str__(self):
        return f'id stand: {self.codStand} - square meters: {self.sq} -  pavilion: {self.pavilion}'



class Standard (Stand):
    def __init__(self, codStand, sq, pavilion, exAssigned, price):
        super().__init__(codStand, sq, pavilion, exAssigned)
        self.price = price

    def __str__(self):
        return f"{super().__str__()} - price: {self.price})"



class Plus (Stand):
    def __init__(self, codStand, sq, pavilion, exAssigned, price, additionalSockets):
        super().__init__(codStand, sq, pavilion, exAssigned)
        plusPrice = price * (1 + 0.07 * additionalSockets)
        self.price = plusPrice
        self.additionalSockets = additionalSockets

    def __str__(self):
        return f"{super().__str__()} - price: {self.price})"




class Premium (Stand):
    def __init__(self, codStand, sq, pavilion, exAssigned, price, position):
        super().__init__(codStand, sq, pavilion, exAssigned)
        premiumPrice = price*1.3
        self.price = premiumPrice
        self.position = position

    def __str__(self):
        return f"{super().__str__()} - price: {self.price} - position: {self.position})"


class Exhibitor:
    def __init__(self, codEx, name, surname, stAssigned):
        self.codEx = codEx
        self.name = name
        self.surname = surname
        self.stAssigned = False
    def __str__(self):
        return f"ID Exhibitor: {self.codEx} - name: {self.name} - surname: {self.surname}"










