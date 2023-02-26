
from ursina import *

class Spawner:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.status = "processing"
        self.open = [[6,6]] #bele kerülnek azok a koordináták, amelyeket kinyitottunk.
        self.neighbours = [] # bele kerülnek a kinyitott területek körül lévők koordinátái.
        self.possible_way = [] # bele kerülnek azok a koordináták, amelyek útvonalként szolgálnak-

# az origin csak az opened csempékhez tartozhatnak.

class Grid:
    def __init__(self, size_x, size_y): # Szabad -e a terület, távolság a starttól, táv a végtől, a kettő összege, és az origin lista.
        self.grid = [[[False,0,0,0,[]] for x in range(size_x)] for y in range(size_y)]
        self.size_x = size_x

        self.size_y = size_y

    def get_value(self, state, x, y): # visszaadja az adott terület értékét
        return self.grid[y][x][state]
    def set_value(self, state, x, y, value): # adott területre értéket állít
        self.grid[y][x][state] = value

    def show_matrix(self): # printeli a mátrixot
        for x in self.grid:
            print(f'{x}')

enemy1 = Spawner(6, 5)
grid = Grid(size_x = 200, size_y = 200)

#grid.show_matrix()

# ---------------------------------------------------------------------------------------------------------------------

def distances(target, x, y, x_end, y_end): # kiszámolja a távolságot a start és a csempe közt..
    grid.set_value(1, x, y, int(10 * round(distance([x, y, 0], [target.x, target.y, 0]),1))) # távolság start és szomszéd közt. G_cost
    grid.set_value(2, x, y, int(10 * round(distance([x, y, 0], [x_end, y_end, 0]),1)))  # távolság vég és szomszéd közt. H_cost
    grid.set_value(3, x, y, int(10 * round((distance([x, y, 0], [target.x, target.y, 0])) + (distance([x, y, 0], [x_end, y_end, 0])),1))) # F_cost
    if [x, y] == [target.x, target.y]:
        grid.set_value(1, x, y, 1)
                    # kezdő  -  vég

def open_node(target, x, y, x_end, y_end):
    if [x,y] not in target.open:
        nb_list = [[x + 1, y], [x + 1, y - 1], [x, y - 1], [x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
        if grid.get_value(0, x, y) == False: # Ha a területen nincs akadály
            distances(target, x, y, x_end, y_end)
            target.open.append([x,y])

            neighbour_gcosts = [] # 0: g_cost || 1: originated to || 2: center
            for xy in nb_list:
                if grid.get_value(0, xy[0], xy[1]) == False:
                    distances(target, xy[0], xy[1], x_end, y_end)
                    target.neighbours.append([grid.get_value(3, xy[0], xy[1]), xy])
            for xy in nb_list:
                nbs = [[xy[0] + 1, xy[1]], [xy[0] + 1, xy[1] - 1], [xy[0], xy[1] - 1], [xy[0] - 1, xy[1] - 1], [xy[0] - 1, xy[1]], [xy[0] - 1, xy[1] + 1], [xy[0], xy[1] + 1], [xy[0] + 1, xy[1] + 1]]
                for nb in nbs:
                    if grid.get_value(1, nb[0], nb[1]) != 0:
                        if [nb[0],nb[1]] in target.open:
                            neighbour_gcosts.append([grid.get_value(1, nb[0], nb[1]), nb, xy])

            #print(f"{neighbour_fcosts}\n{neighbour_gcosts}")

            sorted_nbgcost = sorted(neighbour_gcosts)
            for i in range(8):
                grid.set_value(4, sorted_nbgcost[i][2][0], sorted_nbgcost[i][2][1], sorted_nbgcost[i][1])


def relocate(target, x_end, y_end): # target a célszemély, x_end a vég koordináta.
    for x in range(grid.size_x): # a for ciklus üressé teszi a F cost, H cost és G cost értékeit.
        for y in range(grid.size_y):
            for counter in range(1,4):
                if grid.get_value(counter, x, y) != 0:
                    grid.set_value(counter, x, y, 0)

    open_node(target, target.x, target.y, x_end, y_end)
    while [x_end, y_end] not in target.open:
        sorted_nb_fcosts = sorted(target.neighbours)
        open_node(target, sorted_nb_fcosts[0][1][0], sorted_nb_fcosts[0][1][1], x_end, y_end)
        del sorted_nb_fcosts[0]
        print(sorted_nb_fcosts)
        break


    if [x_end, y_end] in target.open:
        print('Elértem a célom')
        print(target.open)





# ---------------------------------------------------------------------------------------------------------------------

relocate(enemy1, 2, 10)

#grid.show_matrix()
#print(f'\n{enemy1.open}\n{enemy1.neighbour}')










