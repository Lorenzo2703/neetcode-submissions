class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lista = {}
        self.id = 0
        

    def get(self, key: int) -> int:
        # 1. Evitiamo il KeyError: se la chiave non c'è, ritorniamo subito -1
        if key not in self.lista:
            return -1
        
        self.id += 1
        self.lista[key][1] = self.id  # Aggiorna il timestamp (diventa l'elemento usato più di recente)
        return self.lista[key][0]
        


    def put(self, key: int, value: int) -> None:
        self.id += 1
        
        # 2. Controllo capacità: se la chiave è NUOVA e siamo già al limite (>= capacity)
        if key not in self.lista and len(self.lista) >= self.capacity:
            # 3. Troviamo la chiave che ha il timestamp più vecchio (l'indice 1 della lista associata)
            min_key = min(self.lista, key=lambda k: self.lista[k][1])
            del self.lista[min_key]

        # Inseriamo o aggiorniamo la chiave con il nuovo valore e il timestamp corrente
        self.lista[key] = [value, self.id]
