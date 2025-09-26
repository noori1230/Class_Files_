var=1
print(var > 0)
print(not (var <= 0))#not convert false into true
print(var <= 0)
var=1
print(var != 0)#"!" means not
print(not (var == 0))#always equal come with operator or equal
i=15
longer = not i
#asking for player's age and points
age = int(input("how old are you? "))
point = int(input("how many points do you have? "))
#check if player is allowed to play
if age >= 10 and point >= 20:
    print("you can play the game!")
else:
    print("sorry, you can't play yet.")
    # and operator is used

age = int(input("how old are you? "))
point = int(input("how many points do you have? "))
if age >= 10 or point >= 20:
    print("you can play the game!")
else:
    print("sorry, you can't play yet.")
    # operator or is used

    age = int(input("how old are you? "))
point = int(input("how many points do you have? "))
if age >= 10 not point >= 20:
    print("you can play the game!")
else:
    print("sorry, you can't play yet.")


