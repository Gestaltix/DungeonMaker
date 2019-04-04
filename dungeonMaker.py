from random import randrange as rng
import turtle as t


class Cell:
    def __init__(self, position):
        self.position = position


def makeDungeon(numberOfCells):
    dungeon = []
    stack = []
    beginningCell = Cell([0, 0])
    dungeon.append(beginningCell)
    while len(dungeon) < numberOfCells:
        stack = lookForOptions(dungeon, stack)
        newCell = Cell(stack.pop(rng(len(stack))))
        dungeon.append(newCell)
    drawCells(dungeon, 15)


def lookForOptions(dungeon, stack):
    newStack = [*stack]
    cell = dungeon[-1]
    potentials = [[0, 1], [0, -1], [-1, 0], [+1, 0]]
    for x in enumerate(potentials):
        print(x)
        potentials[x[0]] = [potentials[x[0]][0] + cell.position[0],
                            potentials[x[0]][1] + cell.position[1]]
    for potential in potentials:
        if potential not in newStack:
            if potential not in [cell.position for cell in dungeon if cell.position == potential]:
                newStack.append(potential)
    print(newStack)
    return newStack


def drawCells(dungeon, writeSize):
    t.pensize(2)
    t.color('blue')
    t.up()
    t.speed(8)
    for cell in dungeon:
        t.setpos(cell.position[0]*writeSize, cell.position[1]*writeSize)
        drawCross()
    return('Finished')


def drawCross():
    t.forward(5)
    t.down()
    t.backward(10)
    t.up()
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.down()
    t.backward(10)
    t.right(90)
    t.up()


makeDungeon(50)
