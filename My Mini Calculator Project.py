#Mini special Calculator
def main():
    print("Hello.Welcome to mini caculator.This program can give some math processes.Choose the number command")
    while True:
        info()
        n=int(input())
        if n==1:
            find_maximum_and_minimum_value()
        elif n==2:
            find_factorial_value()
        elif n==3:
            find_avarage_value()
        elif n==4:
            find_square_root_value()
        elif n==5:
            find_square_value()
        elif n==0:
            break

def info():
    print("Choose 1 command for find maximum and minimum")
    print("Choose 2 command for find factorial")
    print("Choose 3 command for find avarage")
    print("Choose 4 command for find square root")
    print("Choose 5 command for find square")
    print("Choose 0 command for exit this program")

def find_maximum_and_minimum_value():
    input_list = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, input_list.split()))
    print("The maximum value is",max(numbers),"\nThe minimum value is",min(numbers))

def find_factorial_value():
        k=int(input("Which number do you want to find factorial?.Write number please:"))
        factorial=1
        for i in range(1,k+1):
            factorial*=i
        print("The factorial value is:",factorial)
            

def find_avarage_value():
    input_list = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, input_list.split()))
    print("The avarage value is:" , sum(numbers)/len(numbers))

def find_square_root_value():
    l=int(input("Which number do you want to find square root?.Write number please:"))
    square_root=l**0.5
    print("The square root value is:", square_root)

def find_square_value():
    y=int(input("Which number do you want to find square?.Write number please:"))
    square=y**2
    print("The square value is:",square)

main()