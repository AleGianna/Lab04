import csv
from operator import attrgetter
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
            for row in reader:
                cod = row[0].strip()
                codid = cod[:-1]

                if codid == "ST":
                    codStand = cod
                    sq = int(row[1])
                    pavilion = int(row[2])
                    price = int(row[3])
                    try:
                        g=int(row[4])
                        s= Plus(codStand, sq, pavilion, price, int(row[4]))
                    except IndexError:
                        s = Standard(codStand, sq, pavilion, price)
                    except ValueError:
                        price = int(row[3])
                        s = Premium(codStand, sq, pavilion, price, row[4])
                    self.stands.append(s)
                    print(s)
                elif codid == "ES":
                    codEx = row[0]
                    name = row[1]
                    surname = row[2]
                    e = Exhibitor(codEx, name, surname)
                    self.exhibitors.append(e)

                else:
                    print(f"{cod} non valido")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """
        Assegna uno stand a un espositore, verificando che:
        1. Lo stand e l'espositore esistano.
        2. Lo stand sia libero (non già assegnato).
        3. L'espositore non abbia già un altro stand assegnato.
        """
        # 1. Trova lo stand e l'espositore nelle rispettive liste
        stand = next((s for s in self.stands if s.codStand == codice_stand), None)
        espositore = next((e for e in self.exhibitors if e.codEx == codice_espositore), None)

        # 2. Verifica l'esistenza degli elementi
        if not stand:
            raise ValueError(f"Lo stand con codice '{codice_stand}' non esiste.")
        if not espositore:
            raise ValueError(f"L'espositore con codice '{codice_espositore}' non esiste.")

        # 3. Verifica che lo stand sia disponibile
        if stand.exAssigned is not None:
            raise ValueError(f"Lo stand '{codice_stand}' è già occupato.")

        # 4. Verifica che l'espositore non abbia già uno stand
        if espositore.stAssigned is not None:
            raise ValueError(f"L'espositore '{codice_espositore}' ha già uno stand assegnato.")

        # 5. Effettua l'assegnazione bidirezionale
        stand.exAssigned = espositore
        espositore.stAssigned = stand

        print(
            f"Successo: Stand {codice_stand} assegnato a {espositore.name} {espositore.surname} ({codice_espositore}).")


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for e in self.exhibitors:
            print(e)



    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # Restituisce una nuova lista ordinata in base all'attributo 'price' degli oggetti stand
        return sorted(self.stands, key=attrgetter('price'))

class Stand :
    def __init__(self, codStand, sq, pavilion):
        self.codStand = codStand
        self.sq = sq
        self.pavilion = pavilion
        self.exAssigned = None

    def __str__(self):
        return f'id stand: {self.codStand} - square meters: {self.sq} -  pavilion: {self.pavilion}'



class Standard (Stand):
    def __init__(self, codStand, sq, pavilion, price):
        super().__init__(codStand, sq, pavilion)
        self.price = round(price,2)

    def __str__(self):
        return f"{super().__str__()} - price: {self.price})"



class Plus (Stand):
    def __init__(self, codStand, sq, pavilion, price, additionalSockets):
        super().__init__(codStand, sq, pavilion)
        plusPrice = price * (1 * 0.07 * additionalSockets)
        self.price = round(plusPrice,2)
        self.additionalSockets = additionalSockets

    def __str__(self):
        return f"{super().__str__()} - price: {self.price})"




class Premium (Stand):
    def __init__(self, codStand, sq, pavilion, price, position):
        super().__init__(codStand, sq, pavilion)
        premiumPrice = price*1.3
        self.price = round(premiumPrice,2)
        self.position = position

    def __str__(self):
        return f"{super().__str__()} - price: {self.price} - position: {self.position})"


class Exhibitor:
    def __init__(self, codEx, name, surname):
        self.codEx = codEx
        self.name = name
        self.surname = surname
        self.stAssigned = None
    def __str__(self):
        return f"ID Exhibitor: {self.codEx} - name: {self.name} - surname: {self.surname} - stand assigned: {self.stAssigned}"










