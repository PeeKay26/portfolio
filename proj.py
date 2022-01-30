import random
no = random.randint(1,100)
attempt = 0
def factors(x):
   print("The factors of the number are:")
   for i in range(1, x + 1,x-1):
       if x % i == 0:
           print(i)

while True:
    usa = int (input("Enter your guess: "))
    if no == usa:
        print ("Well Done!!")
        break
    elif no > usa:
        print ("Your guess is lower than the number")
        attempt += 1
    elif no < usa:
        print ("Your guess is higher than the number")
        attempt += 1
    if attempt == 1:
        if usa//2 == 0:
            print ("The number is even")
        else:
            print ("The number is odd")
    if attempt == 2:
        factors(no)
    if attempt == 3:
        print ("You lose")