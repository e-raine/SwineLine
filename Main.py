import Userinput as User
import Database as dt

# Main
def main():
    choice = choice1()



# Add / Edit / Delete 
def choice1():
    choice = str(input("Add, Edit or Delete? ")).lower()
    
    if choice == "add":
        list = print(sort_data())
        return list
    elif choice == "edit":
        list = print("Edit")
        return list
    elif choice == "delete":
        list = print("Delete")
        return list
    else:
        choice1()


# Add Section 
def sort_data():
    list = choice2()
    if len(list) == 3:
        date = list[0]
        con = list[1]
        num = list[2]
        sorted_dict = {num: [date, con]}
        return  sorted_dict
        # print("Date => ", date)
        # print("Population => ", num)
    elif len(list) == 4:
        date = list[0]
        con = list[1]
        num = list[2]
        con2 = list[3]
        sorted_dict = {num: [date, con, con2]}
        return sorted_dict
        # print("Culling Date => ", date)
        # print("# of Culled Swine => ", num)


def choice2():
    choice = str(input("Population or Culled? ")).lower()

    if choice == "population":
        list = User.population()
        return list 
    elif choice == "culled":
        list = User.culled()
        return list 
    else:
        choice2()

# Edit section











# Delete section







main()
