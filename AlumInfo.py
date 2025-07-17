from tokenize import Double
alumnos={}
def ingresar_alumno(alums=[]):
    cantidad=int(input(f"\nIngrese la cantidad de estudiantes: "))
    for i in range(cantidad):
        print(f"\n estudiante #{i+1}:")
        carne=int(input("Ingrese el carne del estudiante: "))
        if carne>0:
            if carne not in alumnos:

                    nombre=input("Ingrese el nombre del alumno: ")
                    age=float(input("La edad del alumno:"))
                    if (age>0):
                        carrera=input("Ingrese el carrera del alumno: ")
                        cantidad = int(input("Ingrese la cantidad de cursos al que se inscribira el alumno: "))
                        if cantidad>0:
                            for e in range(cantidad):
                                cursName=input("Ingrese el nombre del curso: ")
                                not1=int(input("Ingrese la nota de las tareas: "))
                                not2=int(input("Ingrese la nota del parcial: "))
                                not3=int(input("Ingrese la nota del proyecto: "))

                            alums[carne] = {
                                "nombre": nombre,
                                "age": age,
                                "carrera": carrera,
                                "cursos": {


                                }
                                }
                        elif cantidad<=0:
                            print("Cantidad invalida")
                            i=i-1
                    elif age<=0:
                        print("Edad invalida invalido.")
                        i=i-1

            else:
                    print("Ya existe un alumno con ese carne.")
                    i=i-1
        elif carne<=0:
            print("Carne no valido.")
            i=i-1
ingresar_alumno(alumnos)