import random

player1= input("Enter Player 1 name: ")
player2= input("Enter Player 2 name: ")
player3= input("Enter Player 3 name: ")

big_list = [random.randint(0, 100) for i in range(100)]


temp_list = big_list.copy()


small_list_1 = []
for i in range(5):
    if temp_list: 
        element = random.choice(temp_list)
        small_list_1.append(element)
        temp_list.remove(element)



small_list_2 = []
for i in range(5):
    if temp_list:
        element = random.choice(temp_list)
        small_list_2.append(element)
        temp_list.remove(element)



small_list_3 = []
for i in range(5):
    if temp_list:
        element = random.choice(temp_list)
        small_list_3.append(element)
        temp_list.remove(element)
remaining_list = temp_list


sum1 = sum(small_list_1)
sum2 = sum(small_list_2)
sum3 = sum(small_list_3)


print("The big list: \n", big_list)
print("Remaining elements \n:", remaining_list)
print(f"{player1}:", small_list_1)
print(f"{player2}:", small_list_2)
print(f"{player3}:", small_list_3)


if (sum1>sum2 and sum1>sum3):
    print(f"The {player1} won")

elif(sum2>sum1 and sum2>sum3):
    print(f"The {player2} won")

else:
    print(f"The {player3} won")
