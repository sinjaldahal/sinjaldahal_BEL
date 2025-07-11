'''
**Write a program to input two sets of student roll numbers: one who play cricket and another who play football. Find:**

   a. Students who play both sports
   b. Students who play only one sport
   c. Students who play neither (given a master list of all students)

'''

cricket_input = input("Enter roll numbers of cricket players : ")
cricket = set(int(x) for x in cricket_input.split())

football_input = input("Enter roll numbers of football players : ")
football = set(int(x) for x in football_input.split())

master = set(range(1, 96))  


def both_players(cricket, football):
    res = []
    for i in cricket:
        if i in football:
            res.append(i)
    return res


def only_one(cricket, football):
    res = []
    for i in cricket:
        if i not in football:
            res.append(i)
    for j in football:
        if j not in cricket:
            res.append(j)
    return res


def no_one(master, cricket, football):
    all_sports = cricket.union(football)
    res = []
    for i in master:
        if i not in all_sports:
            res.append(i)
    return res


print("\nStudents who play both sports:", both_players(cricket, football))
print("Students who play only one sport:", only_one(cricket, football))
print("Students who play no sports:", no_one(master, cricket, football))
