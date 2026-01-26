# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def Divisible(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter number : "))
    ret = Divisible(no)
    print(ret)

if __name__ == "__main__":
    main()
