# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(a, b):
    return a + b

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    ret = Add(no1, no2)
    print("Addition :", ret)

if __name__ == "__main__":
    main()
