import random

print("=================")
print("¡¡elige tu dado!!")
print("=================")
print("1D4")
print("1D6")
print("1D8")
print("1D10")
print("1D12")
print("1D20")
dado=int(input("Elige tu dado "))



#funciones
def dcuatro():
    x=random.randint(1,4)
    return x
def dseis():
    x=random.randint(1,6)
    return x
def docho():
    x=random.randint(1,8)
    return x
def ddiez():
    x=random.randint(1,10)
    return x
def ddoce():
    x=random.randint(1,12)
    return x
def dveinte():
    x=random.randint(1,20)
    return x



if dado <4:
    print("tu dado no existe")
elif dado == 4:
    print(dcuatro())
elif dado == 6:
    print(docho())
elif dado == 8:
    print(ddiez())
elif dado == 10:
    print(ddoce())
elif dado == 12:
    print(dseis())
elif dado == 20:
    print(dveinte())
elif dado >20:
    print ("Tu dado no existe")

print("Que la pifia este contigo")


