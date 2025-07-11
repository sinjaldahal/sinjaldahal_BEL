'''
**Write a program to simulate a basic stack and queue using a list. Provide options to:**

   * Push
   * Pop (stack)
   * Enqueue
   * Dequeue (queue)
'''
queue = []
while True:
    choice = input("enter 1 eqQueue 2 deQueue 3 display")
    if choice=="1":
        num = int(input("Enter a number: "))
        queue.append(num)
    elif choice=="2":
        if(len(queue)==0):
            print("queue is empty")
            continue
        print(f"Deleted element is: {queue.pop(1)}")
    elif choice=="3":
        if(len(queue)==0):
            print("queue is empty")
            continue
        print(f"elements are: {queue}")
    else:
        print("invalid choice")
        break