a=10


list = [10,23,34,12]

try:
    print(list[2])
    b=a/0
    print(a, " ---   ",b)
except ZeroDivisionError:
        print("Zero devod error in the program")        
except IndexError :
    print("Handle the error index value out of the range")


print("Remaining program is executed ")