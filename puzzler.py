import turtle
from random import randrange as rng

# The algorithm is as follows:
# Make a basic map, comprised of cells
# Make rooms from those cells
# Populate the cells


class Cell:
    def __init__(self, position):
        self.type = 0
        self.position = position


def makeCells(numCells, draw=False, cellSize=None):
    dungeon = []
    dungeon.append(Cell([0, 0]))
    for _ in range(numCells - 1):
        options = findOptions(dungeon)
        dungeon.append(options[rng(len(options))])
    return (drawCells(dungeon, cellSize), None)[draw == True]


def findOptions(dungeon):
    options = []
    p = dungeon[rng(len(dungeon))].position
    potentialOptions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for os in potentialOptions:
        if not [cell for cell in dungeon if cell.position == [p[0] + os[0], p[1] + os[1]]]:
            options.append(Cell([p[0] + os[0], p[1] + os[1]]))
    if options != []:
        return options
    else:
        return findOptions([cell for cell in dungeon if cell.position != p])


def drawCells(dungeon, writeSize):
    turtle.pensize(2)
    turtle.color('blue')
    turtle.up()
    turtle.speed(7)
    for cell in dungeon:
        turtle.setpos(cell.position[0]*writeSize, cell.position[1]*writeSize)
        drawCross()
    return('Finished')


def drawCross(pos):
    turtle.setpos(pos[0] * 15, pos[1] * 15)
    turtle.forward(5)
    turtle.down()
    turtle.backward(10)
    turtle.up()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.down()
    turtle.backward(10)
    turtle.right(90)
    turtle.up()


class Cell2:
    def __init__(self, position, neighboors):
        self.type = 0
        self.position = position
        self.neighboors = neighboors

    def returnOption(self):
        print(self.position)
        return self.neighboors.returnOption(self.position)

    def notifyNeighboors(self):
        if self.neighboors.up:
            self.neighboors.up.neighboors.addNeighboor('up', self)
        if self.neighboors.down:
            self.neighboors.down.neighboors.addNeighboor('down', self)
        if self.neighboors.left:
            self.neighboors.left.neighboors.addNeighboor('left', self)
        if self.neighboors.right:
            self.neighboors.right.neighboors.addNeighboor('right', self)


class Neighboors:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.openSlots = False
        self.checkForOpenSlots()

    def addNeighboor(self, direction, cell):
        setattr(self, direction, cell)
        print('added neighboor: ' + f'{cell.position}')
        self.checkForOpenSlots()

    def checkForOpenSlots(self):
        if self.up and self.down and self.left and self.right:
            self.openSlots = False
        else:
            self.openSlots = True

    def returnOption(self, p):
        options = []
        if self.left == None:
            options.append([p[0] - 1, p[1]])
        if self.right == None:
            options.append([p[0] + 1, p[1]])
        if self.up == None:
            options.append([p[0], p[1] + 1])
        if self.down == None:
            options.append([p[0], p[1] - 1])
        print('\n' + str(options) + '\n')
        return options[rng(len(options))]


def newMakeCells(numCells):
    dungeon = []
    dungeon.append(Cell2([0, 0], Neighboors(None, None, None, None)))
    drawCross([0, 0])
    for _ in range(numCells - 1):
        newCell = generateNewCell(dungeon)
        dungeon.append(newCell)
        drawCross(newCell.position)


def findNeighboors(p, dungeon):
    px = p[0]
    py = p[1]
    up = handleDirection([px, py + 1], dungeon)
    down = handleDirection([px, py - 1], dungeon)
    right = handleDirection([px + 1, py], dungeon)
    left = handleDirection([px - 1, py], dungeon)
    return up, down, left, right


def handleDirection(p, dungeon):
    neighboor = [cell for cell in dungeon if cell.position == p]
    if not neighboor == []:
        neighboor = neighboor[0]
    else:
        neighboor = None
    return neighboor


def generateNewCell(dungeon):
    openCells = [cell for cell in dungeon if cell.neighboors.openSlots]
    openCell = openCells[rng(len(openCells))]
    cellPosition = openCell.returnOption()
    up, down, left, right = findNeighboors(cellPosition, dungeon)
    newCell = Cell2(cellPosition, Neighboors(up, down, left, right))
    newCell.notifyNeighboors()
    return newCell


newMakeCells(20)
