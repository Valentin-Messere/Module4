def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        print(f"This triangle {side1, side2, side3} is equilateral.")
    elif side1 == side2 != side3 or side1 != side2 == side3 or side1 == side3 != side2:
        print(f"This triangle {side1, side2, side3} is isosceles.")
    elif side1 != side2 != side3:
        print(f"This triangle {side1, side2, side3} is scalene.")


triangle_type(100, 100, 100)
triangle_type(100, 120, 120)
triangle_type(120, 120, 100)
triangle_type(120, 100, 120)
triangle_type(120, 140, 100)


def adventure_game(dialogue, choice1, choice2, choice3, decision, result):
    print("First choice ")
    if input("A"):
        result = choice1
    elif input("Z"):
        result = choice2
    elif input("E"):
        result = choice3


adventure_game()
