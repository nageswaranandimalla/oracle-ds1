a=10


list = [10,23,34,12]

try:
    print(list[2])
    try:
        b=a/1
        print(a, " ---   ",b)
    except:
        print("Zero devod error in the program")
        
except:
    print("Handle the error index value out of the range")


finally:
    print("Remaining program is executed ")