i=3
while i !=0:
    print("Meow!")
    i= i-1

print("Woof!\n"*3, end="")

for i in range(3):
    print("Oink!")

for i in ["Cat","Dog","Pig"]:  
    print(i)

for i in range(1,6):
    print("Hello, world.")

for i in range(1,11):
    print(i)

x = int(input('digite un númerico: '))
print("woof!\n"*x, end="")

while True:
    n=int(input("Que es n?: "))
    if n>0:
        break

for i in range(n):
    print("meow!")

def otro():
    n=int(input("Quien es n?: "))
    for i in range(n):
        print("meow!")
otro()

respuesta = "s"  # Inicializamos con "s" para entrar al bucle

while respuesta == "s":  # El bucle sigue mientras la respuesta sea "s"
    print("Sigo repitiendo el bucle")
    respuesta = input("¿Quieres seguir? (s/n): ").lower()

print("¡Bucle terminado!")

while True:
    word=(input("ingrese una palabra: "))
    for i in range(10):
        print(word)
    respuesta=input("¿desea continuar? (s/n): ").lower()
    if respuesta!="s":
        break
print("¡Bucle terminado!")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Ingrese un número positivo: "))
        if n>0:
            return n 

def meow(n):
    for _ in range(n):
        print("Meow!")

main()