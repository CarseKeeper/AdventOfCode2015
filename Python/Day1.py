def main():
    floor: int = parseClue()
    print(floor)
    
    
def parseClue() -> int:
    clue :str = input('> ')
    floor:int = 0
    for x in clue:
        if(x == '('):
            floor += 1
        elif(x == ')'):
            floor -= 1
    return floor


if __name__ == '__main__':
    main()