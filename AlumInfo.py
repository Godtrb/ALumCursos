from tokenize import Double
alumnos={}
def ingresar_alumno(alums=[]):
    cantidad=int(input(f"\nIngrese la cantidad de estudiantes: "))
    for i in range(cantidad):
        print(f"\n producto #{i+1}:")
        carne=input("Ingrese el carne del estudiante: ")
        if carne>0:
            if carne not in alumnos:

                    nombre=input("Ingrese el nombre del alumno: ")
                    age=float(input("La edad del alumno:"))
                    if (age>0):
                            carrera=input("Ingrese el carrera del alumno: ")
                            cantidad = int(input("Ingrese la cantidad de cursos al que se inscribira el alumno: "))
                        if cantidad>0:
                            alums[carne] = {
                                "nombre": nombre,
                                "age": age,
                                "carrera": carrera,
                                "cantidad": cantidad
                                }
                        elif cantidad<=0:
                            print("Cantidad invalida")
                            i=i-1
                    elif age<=0:
                        print("Edad invalida invalido.")
                        i=i-1

            else:
                    print("Ya un producto con ese codigo.")
                    i=i-1
        elif carne<=0:
            print("Carne no valido.")
            i=i-1




print("\nListe de productos")
for Codigo in productos.items():
    print(f"Codigo: {Codigo}")
    print(f"Nombre: {Codigo["nombre"]}")
    print(f"Precio: {Codigo["precio"]}")
    print(f"Categoria: {Codigo["categoria"]}")
    print(f"Talla: {Codigo["talla"]}")
    print(f"En existencia: {Codigo["cantidad"]}")

print(" Buscar producto")
ado=input("Ingrese el codigo del producto a buscar: ")
if ado in productos:
    print(f"Codigo: {ado}")
    print(f"Nombre: {ado["nombre"]}")
    print(f"Precio: {ado["precio"]}")
    print(f"Categoria: {ado["categoria"]}")
    print(f"Talla: {ado["talla"]}")
    print(f"En existencia: {ado["cantidad"]}")
else:
    print("El producto no existe")
ValorInventario=0
for Codigo in productos.items():
    ValorInventario= ValorInventario + (Codigo["precio"]*Codigo["cantidad"])

print(f"EL valor total del inventario es: Q{ValorInventario}")

for Codigo in productos.items():
    if Codigo["categoria"]=="Mujer":
        Mujer=Mujer+Codigo["cantidad"]
    if Codigo["categoria"]=="Hombre":
        Hombre=Hombre+Codigo["cantidad"]
    if Codigo["categoria"]=="Niño":
        Niño=Niño+Codigo["cantidad"]
print("\nListe de categorias")
print(f"Mujer: {Mujer}")
print(f"Hombre: {Hombre}")
print(f"Niño: {Niño}")