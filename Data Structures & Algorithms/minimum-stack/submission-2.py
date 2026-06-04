class MinStack:
    def __init__(self):
        # Ogni elemento sarà una coppia: (valore, minimo_fino_a_qui)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # Se la pila è vuota, il minimo è il valore stesso
            self.stack.append((val, val))
        else:
            # Il nuovo minimo è il più piccolo tra il valore attuale e il minimo precedente
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]