# Actividad: Desafio de calificaciones y estadisticas

## Paso #1: Determinar el estado de aprobacion de una calificacion
# - Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# - Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

print("")
try:
  # Entrada: Solicitar nombre y calificacion al usuario
  user_name = str(input("Ingresa tu nombre: ")).capitalize()

  # Validacion: Verificar que el usuario ingrese un nombre valido.
  while not user_name.isalpha():
    error_name = str(input("ERROR, Ingresa un nombre valido: ")) 
    user_name = error_name
    print("------------------------------------------")

  
  user_last_name = str(input("Ingresa tu Apellido: ")).capitalize()
  
  while not user_last_name.isalpha():
    error_last_name = str(input("ERROR, Ingresa un apellido valido: ")) 
    user_last_name = error_last_name
    print("------------------------------------------")

  user_note = int(input("Ingresa una calificacion entre 0 - 100: "))
  
  # Entrada: Se crea un diccionario vacio que mas adelante mostrara tanto datos como estado de aprobacion de el usuario
  data = {}
  
  # Validacion: Verificar que el usuario haya ingresado una calificacion correcta
  if user_note < 0 or user_note > 100:
    print(f"La calificacion {user_note} no se encuentra en el rango especificado.") 
  else:
    # Validacion: Verificar y determinar el estado de aprobacion 
    print("A continuacion veras los datos ingresado y el estado de aporbacion. \n")

    if user_note >= 50:
      
      data = {
        "Nombre usuario": user_name,
        "Apellido usuario": user_last_name,
        "Calificacion ingresada": user_note,
        "Estado": "Aprobado"
      }
      
      print(f"""
        Nombre usuario => {data['Nombre usuario']} {data["Apellido usuario"]}  
        Calificacion ingresada => {data['Calificacion ingresada']}
        Estado => {data['Estado']}    
      \n""")
      
    else:
      data = {
        "Nombre usuario": user_name,
        "Apellido usuario": user_last_name,
        "Calificacion ingresada": user_note,
        "Estado": "Desaprobado",
        "Mensaje motivacional": "La proxima vez te ira mejor."
      }
      
      print(f"""
        Nombre usuario => {data['Nombre usuario']} {data["Apellido usuario"]}  
        Calificacion ingresada => {data['Calificacion ingresada']}
        Estado => {data['Estado']} 
        Mensaje motivacional => {data['Mensaje motivacional']}   
      \n""")
      
# Control: Si el usuario ingresa un valor invalido, manejar el error, y mostrar mensaje personalizado.
except ValueError:
  print("ERROR, Ingresaste un valor invalido.")
  
## Paso #2: Calcular el promedio
# - Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
# - Calcular y mostrar el promedio de las calificaciones en la lista

try:
  
  # Entrada: Lista que almacenara las calificaciones del usuario
  grades = []
  amount_grades = int(input("Cantidad de calificaciones que ingresaras (MIN 2 - MAX 15): "))
  while amount_grades < 2 and amount_grades > 15:
    error_amount = int("\nERROR, Ingresa una cantidad valida: ")
    amount_grades = error_amount
    print("---------------------------------------------")

  print("")
  
  # Indicacion: Se le indicara al usuario la cantidad de notas que va a ingresar
  print(f"* A continuacion ingresaras {amount_grades} calificaciones * \n")

  for i in range(amount_grades):
    calificacion = float(input(f"Ingresa la calificacion #{i+1}: "))
    print("----------------------------------------------")
  
    if calificacion < 1 or calificacion > 100:
      print("Ingresaste una calificacion erronea.")
      break
    else:
      grades.append(calificacion)

  
  print("")

  print(f"Las calificaciones ingresadas fueron: {grades}")

  # Sumatoria: Sumar las calificaciones ingresadas por el usuario
  total = 0
  for grade in grades:
    total = int(total + grade)

  average = total / len(grades)
  print(f"El promedio que obtuviste segun las calificaciones ingresadas es: {average}")

except ValueError:
  print("ERROR, Ingresaste un valor invalido.")