t = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
possibilities = [t[0:3], t[3:6], t[6:9], t[0:7:3], t[1:8:3],
                 t[2:9:3], t[0:9:4], t[2:7:2]]

def screen():
    print("---------")
    print(f"| {t[0]} {t[1]} {t[2]} |")
    print(f"| {t[3]} {t[4]} {t[5]} |")
    print(f"| {t[6]} {t[7]} {t[8]} |")
    print("---------")
screen()

def results(): 
    if " " not in t:
        if "XXX" in possibilities:
            print("X wins")
            return True
        elif "OOO" in possibilities:
            print("O wins")
            return True
        else:
            print("Draw")
            return True

def plug_coordinate(coordinate):
    global t
    if coordinate == "1 1":
        if t[6] == " ":
            t[6] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "1 2":
        if t[3] == " ":
            t[3] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "1 3":
        if t[0] == " ":
            t[0] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 1":
        if t[7] == " ":
            t[7] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 2":
        if t[4] == " ":
            t[4] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 3":
        if t[1] == " ":
            t[1] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 1":
        if t[8] == " ":
            t[8] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 2":
        if t[5] == " ":
            t[5] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 3":
        if t[2] == " ":
            t[2] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False

options = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]
def check_coordinate(coordinate):
    if coordinate not in options:
        print("Coordinates should be from 1 to 3!")
        return False
    elif coordinate[0] and coordinate[2] not in "1234567890":
        print("You should enter numbers!")
        return False
    else:
        return True

while " " in t:
    coordinate = input("Enter the coordinates: ")
    acceptable = check_coordinate(coordinate)
    game_over = results()
    if acceptable:
        plug_coordinate(coordinate)
        screen()
        results()
    elif game_over:
        break
