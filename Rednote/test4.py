
lista = []
A = "A" ; B = "B" ; C = "C" ; D = "D"

class Test():
    def __init__(self, key):
        global lista
        self.kulcs = key

        self.count_a = 0
        self.count_b = 0
        self.count_c = 0
        self.count_d = 0

        self.points = 0

        lista.append(self)

Test([C,B,A,A,D,A,A,A,B,A,D,B,A,A,A,A,B,A,B,C,B,D,D,D,B,D,A,C,B,B,B,A,C,D,A,D,B,D,A,C])
Test([A,A,B,C,B,D,B,D,D,B,A,B,D,B,C,D,B,A,A,C,D,B,D,C,A,B,D,A,A,A,A,A,A,A,B,B,A,D,C,A])

Test([D,B,C,B,D,C,A,B,D,C,D,C,A,C,B,B,D,C,A,D,A,B,A,D,B,B,C,A,C,D,B,A,A,D,C,C,B,D,A,C])
Test([C,C,B,B,D,B,D,A,B,C,D,B,A,C,C,D,B,A,D,C,A,C,C,D,C,C,C,D,D,B,A,C,B,A,D,A,A,B,B,D])

Test([A,D,B,D,C,D,C,D,A,B,B,B,C,D,A,C,A,B,B,A,C,B,C,D,C,C,B,B,C,A,A,C,D,D,B,B,C,A,D,A])
Test([B,D,B,A,A,B,B,A,A,C,A,D,C,B,D,C,D,C,B,A,B,C,B,B,C,D,A,A,B,A,D,C,C,A,D,A,D,D,B,C])

Test([B,C,D,A,D,C,A,B,D,A,D,A,C,B,B,A,C,D,A,A,A,D,C,B,C,B,A,D,D,B,B,C,D,B,D,A,B,C,D,C])
Test([C,B,A,B,B,A,A,B,C,A,C,D,D,D,A,C,A,D,C,D,D,B,A,D,C,D,C,A,A,A,B,D,B,D,C,C,B,D,D,B])

solution = input("Add meg a megoldásaid: ").replace(" ", "").split(",")

for i in lista:
    for x in range(40):
        if i.kulcs[x] == solution[x]:
            i.points += 1
    print(i.points)

