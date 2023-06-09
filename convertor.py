day = int(input("roz :"))
mount = int(input("mah : "))
year = int(input("sal : "))

def convertor(day,mount,year):
    if mount>10:
        birthday = year + 622
    elif day>10 and mount==10:
        birthday = year + 622

    else:birthday= year + 621

    print (f"sal tavalodet is {birthday}")

convertor(day,mount,year)