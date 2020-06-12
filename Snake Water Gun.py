import random

lst = ["s", "w", "g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0


print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome To Snake,Water,Gun Game\n\n\n")

print("Please Enter Your name: ")

a = input()

#this game in while loop

while no_of_chance < chance:
    Rinput = input("Snake,Water,Gun: ")
    Rrandom = random.choice(lst)

    if Rinput == Rrandom:
        print("tie both 0 point to each\n ")

    # if user enter s
    if Rinput == "s" or Rrandom == "g":
        computer_point = computer_point + 1
        print(f"your guess {Rinput} and computer guess is {Rrandom}")
        print("computer wins 1 point \n")
        print(f"computer point is {computer_point} and {a} point is {human_point}")

    elif Rinput == "s" or Rrandom == "w":
        human_point = human_point + 1
        print(f"your guess {Rinput} and computer guess is {Rrandom}")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and {a} point is {human_point}")

    # if user enter w
    elif Rinput == "w" or Rrandom == "s":
        computer_point = computer_point + 1
        print(f"your guess is {Rinput} and computer geuss is {Rrandom}")
        print("computer win 1 points\n")
        print(f"computer point is {computer_point} and {a} point is {human_point}")

    elif Rinput == "w" or Rrandom == "g":
        human_point = human_point + 1
        print(f"your guess is {Rinput} and computer guess is {Rrandom}")
        print("human win 1 points\n")
        print(f"computer point is {computer_point} and {a} point is {human_point}")

    # if user enter g

    elif Rinput == "g" or Rrandom == "s":
        computer_point = computer_point + 1
        print(f"human guess {Rinput} and computer guess {random}")
        print("computer win 1 point\n")
        print(f"{a} point is {human_point} and computer point is {computer_point}")

    elif Rinput == "g" or Rrandom == "w":
        human_point = human_point + 1
        print(f"your guess is {Rinput} and computer guess is {Rrandom}")
        print("human wins 1 point\n")
        print(f"{a} point is {human_point} and computer point is {computer_point}")

    else:
        print("you have enter wrong input")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game Over")

if computer_point > human_point:
    print(f"computer win the game and {a} loss the game")

if computer_point < human_point:
    print(f"congress {a} win the game and computer loss the game")

print(f"{a} point is {human_point} and computer point is {computer_point}")

