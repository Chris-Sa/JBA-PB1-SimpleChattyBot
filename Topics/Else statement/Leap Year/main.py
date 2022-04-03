# put your python code here

year = int(input())

if year % 4 == 0:
    # print("divisible by four")
    if year % 400 == 0:
        # print("divisible by 400")
        print("Leap")
    elif year % 100 == 0:
        # print("divisible by 100")
        print("Ordinary")
    else:
        print("Leap")
else:
    # print("not divisible by four")
    print("Ordinary")