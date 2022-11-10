# Prime Number Checker
while True:
    num = int(input('Enter your Number: \n')) 
    flag = False
    if(num>1):
        for i in range(2, num):
            if(num % i == 0):
                flag = True
                break
    if(flag):
        print(f'Your number {num} is Not a prime number')
    else:
        print(f'Your number {num} is a Prime number')
    userWantsToQuit = input('Do you want to Quit? (yes/no) \n')
    if userWantsToQuit == 'yes':
        break

