""""This is a coment"""

from xmlrpc.client import boolean


coins = (.01,.05,.10,.15,.50)
cent, five, dime, quarter, half = coins

print(cent)

while True:
    cents=int(input("how many CENTS do you have? "))
    fives=int(input("how many FIVES do you have? "))
    dimes=int(input("How many DIMES do you have? "))
    quarters=int(input("How many QUARTERS do you have? "))
    halfs=int(input("How many HALFS do you have? "))
    money=(cents*cent)+(fives*five)+(dimes*dime)+(quarters*quarter)+(halfs*half)
    print("You have: ", money)

    answer=input("Did you finish? YES or NOT : ")
    if answer=='YES' or answer == 'yes':
        break