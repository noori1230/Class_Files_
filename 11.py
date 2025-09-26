#ask if homework is done
homework_done = input("did you finish your work?(yes/no)").lower()

#ask if chores are done

chores_done = input("did you do your chores?(yes/no)").lower()

#check if dessert is allowed

if homework_done =="yes" or chores_done == "yes":
    print("yay!you can have dessert!")
else:
    print("oh no!finish your homework or chores first.")