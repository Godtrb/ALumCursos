from tokenize import Double
alumnos={}
cursos={}
def ingresar_alumno(alums=[]):
    cantidad=int(input(f"\nIngrese la cantidad de estudiantes: "))
    for i in range(cantidad):
        print(f"\n estudiante #{i+1}:")
        carne=int(input("Ingrese el carne del estudiante: "))
        if carne>0:
            if carne not in alumnos:

                    nombre=input("Ingrese el nombre del alumno: ")
                    correo = input("Ingrese el correo electrónico del alumno: ")
                    telefono = input("Ingrese el número de teléfono del alumno: ")
                    age=float(input("La edad del alumno:"))
                    if (age>0):
                        carrera=input("Ingrese el carrera del alumno: ")
                        cantidad = int(input("Ingrese la cantidad de cursos al que se inscribira el alumno: "))
                        if cantidad>0:
                            for e in range(cantidad):
                                cursName=input("Ingrese el nombre del curso: ")
                                not1=int(input("Ingrese la nota de las tareas: "))
                                if(not1>0):
                                    not2=int(input("Ingrese la nota del parcial: "))
                                    if(not2>0):
                                        not3=int(input("Ingrese la nota del proyecto: "))
                                        if(not3>0):
                                            cursos[cursName] ={
                                                "NotaTearea":not1,
                                                "NotaProyecto":not3,
                                                "NotaParcial":not2
                                            }

                                        elif(not3<0):
                                            print("Nota Invalida")
                                            e = e - 1
                                    elif (not2<0):
                                        print("Nota Invalida")
                                        e=e-1

                                elif(not1<0):
                                    print("Nota invalida")
                                    e=e-1
                            alums[carne] = {
                                "nombre": nombre,
                                "age": age,
                                "carrera": carrera,
                                "contacto": {
                                    "correo": correo,
                                    "telefono": telefono
                                },
                                "cusos":cursos
                                }
                            cursos.clear()
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