listaCompras= [""]

def funcion():
    respuesta = input("Quieres meter un nuevo producto?\n")
    while respuesta == "si":
        producto = input("Escribe el producto")
        listaCompras.append(producto)
        respuesta = input("Quieres meter un nuevo producto?\n")

if __name__ == "__main__":
    funcion()

with open("compra.txt","w") as filehandle:
    for listitem in listaCompras:
        filehandle.write(listitem+"\n")

print("Esta es tu lista de la compra")
compra = open("compra.txt","r")
nota = compra.read()
print(nota)