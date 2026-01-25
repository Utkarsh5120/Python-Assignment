# 1

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Mdata = list(map(lambda Arr : Arr * Arr,Data))

    print("Suqare of each elements is :",Mdata)

if __name__ == "__main__":
    main()


# 2

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 == 0 ,Data))

    print("Even number is :",Fdata)

if __name__ == "__main__":
    main()


# 3

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 != 0 ,Data))

    print("Odd number is :",Fdata)

if __name__ == "__main__":
    main()


# 4


from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Rdata = int(reduce(lambda A , B : A + B,Data))

    print("Summation of all elements are :",Rdata)

if __name__ == "__main__":
    main()


# 5

from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Rdata = int(reduce(lambda A , B : A + B,Data))

    print("Summation of all elements are :",Rdata)

if __name__ == "__main__":
    main()


# 6

from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The data is : ",Data)

    Fdata = int(reduce(lambda a, b: (a < b) and a or b,Data))

    print(Fdata)


if __name__ == "__main__":
    main()


# 7

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = str(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda a : len(a) > 5 ,Data))

    print(Fdata)

    if(len(Fdata) >= 0):
        print("There is no String having lenght is grater than or equal 5")
       


if __name__ == "__main__":
    main()


# 8

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : (No % 3 == 0) and (No % 5 == 0),Data))

    print("The number which divisible by 3 and 5 are :",Fdata)

if __name__ == "__main__":
    main()


# 9

from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Rdata = int(reduce(lambda A , B : A * B,Data))

    print("Product of all elements are :",Rdata)

if __name__ == "__main__":
    main()


# 10

def main():
    Sum = 0
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 == 0 ,Data))

    for i in range(len(Fdata)):
        Sum = Sum + 1
    
    print("Even number count is :",Sum)

if __name__ == "__main__":
    main()
