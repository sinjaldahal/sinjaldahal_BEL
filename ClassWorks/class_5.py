'''

Write py code for the following :-

- Generate a random integer in the given range
- Ask user to guess the number in the same range
- if the guess matches 
        - display "You guessed right"
-otherwise 
        - Ask user "Do you want to continue (y/n)"
        - If -y- repeat the above
        - Otherwise exit



Create a login system as per following:-
- Create a dictionary record containing username: password field for 8 users
- User will get 5 attempts in case of wrong username or password
- Ask user to enter usrname and passsword 
- if username and password matches
        -display "Welcome to abc system"
- else repeat the above for max 5 steps
- if process cannot be completed in 5 attempts display
        - "your attempts expired"





 
import random

while True:
    a = int(input("Enter upper range: "))
    b = int(input("Enter lower range: "))
    c = random.randint(b, a)
    
    d = int(input("Guess a number: "))
    
    if c == d:
        print("You guessed right!")
        break
    else:
        print(f"You guessed wrong! The correct number was {c}.")
    
    x = input("Do you want to continue? (Y/N): ")
    if x.lower() != 'y':
        break
'''


user_database = {
    "suraj": "suraj123",
    "sinjal": "sinjal123",
    "surendra": "surendra123",
    "chapri": "chapri321",
    "angel_priya": "hakerrrr",
}


attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in user_database and user_database[username] == password:
        print("Welcome to Geda system")
        break
    else:
        print("Incorrect username or password. Try again.")
        print(f"You have {max_attempts-attempts} left")
        attempts += 1

if attempts == max_attempts:
    print("Your attempts expired")