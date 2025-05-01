# Actividad: Desafio de calificaciones y estadisticas

## Paso #1: Determinar el estado de aprobacion de una calificacion
# - Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# - Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

print("")
try:
  # Entrada: Solicitar nombre del usuario para una experiencia mas personalizada.
  user_name = str(input("Ingresa tu nombre: ")).capitalize()

  # Validacion: Verificar que el usuario ingrese un nombre valido.
  while not user_name.isalpha():
    error_name = str(input("* ERROR, Ingresa un nombre valido: ")) 
    user_name = error_name
    print("------------------------------------------")

  print("")

  # Entrada: Solicitar apellido
  user_last_name = str(input("Ingresa tu Apellido: ")).capitalize()

  # Validacion: Verificar que el usuario ingrese un apellido valido
  while not user_last_name.isalpha():
    error_last_name = str(input("* ERROR, Ingresa un apellido valido: ")) 
    user_last_name = error_last_name
    print("------------------------------------------")

  # Separador
  print("")

  # Entrada: Se le pide al usuario ingresar una calificacion en el rango especificado.
  user_note = int(input("Ingresa una calificacion entre 0 - 100: "))
  
  # Entrada: Se crea un diccionario vacio que mas adelante mostrara tanto datos como estado de aprobacion de el usuario.
  data = {}
  
  # Validacion: Verificar que el usuario haya ingresado una calificacion correcta.
  if user_note < 0 or user_note > 100:
    print(f"La calificacion {user_note} no se encuentra en el rango especificado.") 
  else:

    # Indicacion
    print("A continuacion veras los datos ingresados y el estado de aprobacion. \n")

    # Validacion: Si el usuario aprobo se mostraran sus datos, calificacion y estado.  
    if user_note >= 50:
      
      # Asignacion: Se modifica el diccionario previamente creado y se le asignan los respectivos valores ingresados por el usuario.
      data = {
        "Nombre usuario": user_name,
        "Apellido usuario": user_last_name,
        "Calificacion ingresada": user_note,
        "Estado": "Aprobado"
      }
      
      # Salida: Se le muestra al usuario los datos ingresados previamente.
      print(f"""
        Nombre usuario => {data['Nombre usuario']} {data["Apellido usuario"]}  
        Calificacion ingresada => {data['Calificacion ingresada']}
        Estado => {data['Estado']}    
      \n""")
      
    else:
      
      # Asignacion
      data = {
        "Nombre usuario": user_name,
        "Apellido usuario": user_last_name,
        "Calificacion ingresada": user_note,
        "Estado": "Desaprobado",
        "Mensaje motivacional": "La proxima vez te ira mejor."
      }
      
      # Salida: Se le muestra al usuario los datos ingresados previamente.
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

# Manejo de errores: Se implementa una estructura try - except para manejar un posible error valueError(error de valor).
try:
  
  # Entrada: Lista que almacenara las calificaciones del usuario
  grades = []
  amount_grades = int(input("Cantidad de calificaciones que ingresaras (MIN 2 - MAX 15): "))
  while amount_grades < 2 or amount_grades > 15:
    error_amount = int(input("\n* ERROR, Ingresa una cantidad valida: "))
    amount_grades = error_amount
    print("---------------------------------------")

  # Separador
  print("")
  
  # Indicacion - Adicional: Se le indicara al usuario la cantidad de notas que va a ingresar.
  print(f"* A continuacion ingresaras {amount_grades} calificaciones (0 - 100) * \n")

  # Entrada - Modificacion: En vez de solicitar al usuario las calificaciones separadas por comas y posteriormente aplicarles un metodo para convertirlas en una lista, se implementa un ciclo for que por cada iteracion le va a solicitar al usuario las calificaciones y su respectivo indice.
  for i in range(amount_grades):
    grade = float(input(f"Ingresa la calificacion #{i+1}: "))
    print("-------------------------------")
  
    # Validacion: Si la calificacion no se encuentra en el rango especificado se dara un error.
    while grade < 1 or grade > 100:
      error_grade = float(input(f"* ERROR, Ingresa nuevamente la calificacion #{i+1}: "))
      grade = error_grade
      print("---------------------------------------------------")
      
    grades.append(grade)

  # Separador
  print("")

  # Salida: Se le muestra al usuario las calificaciones que ingreso en una lista.
  print(f"Las calificaciones ingresadas fueron: {grades}")

  # Sumatoria: Sumar las calificaciones ingresadas por el usuario.
  total = 0
  for grade in grades:
    total = int(total + grade)
    
  # Separador  
  print("")

  # Promedio: Obtener el promedio segun las calificaciones ingresadas.
  average = total / len(grades)
  print(f"El promedio que obtuviste segun las calificaciones ingresadas es: {round(average, 1)} \n")
  
  # Paso #3: Contar calificaciones mayores
  # - Preguntar al usuario un valor especifico
  # - Contar cuantas calificaciones en la lista son mayores a ese valor
  
  # Entrada: Preguntar al usuario por una calificacion especifica.
  specific_value = int(input("Ingresa una calificacion especifica de las calificaciones que ingresaste previamente: "))
  
  # Separador
  print("")

  # Validacion: Funcion que maneja un error de rango de calificacion y se repite hasta que el usuario ingrese una califiaciones valida.
  def error_specific_grade(value):
    while not value in grades:
      specific_value_error = int(input(f"* ERROR, Ingresa una calificacion que se encuentre en {grades}: "))
      value = specific_value_error

      if value in grades:
        return value

  # Valor obtenido de la funcion de validacion.
  def first_validation_grade(validation_grade):
    if validation_grade in grades:
      validation_grade = specific_value
      return validation_grade
    else:
      validation_grade = error_specific_grade(specific_value)
      return validation_grade
  
  validation_result = first_validation_grade(specific_value)

  # Calculo - conteo calificaciones mayores: Ciclo for que recorre las calificaciones y calcula cuantas calificicaciones son mayores que la calificacion ingresada.
  amount_high = 0
  for grade in grades:
    if validation_result < grade:
      amount_high += 1
      
  # Salida: Se le muestra al usuario la cantidad de calificaciones mayores a la ingresada.
  print(f"Cantidad de calificaciones mayores a {validation_result}: [{amount_high}] \n")
  
  # Paso #4: Verificacion y conteo
  # - Preguntar al usuario por una calificacion especifica
  # - Mediante un bucle for realizar un conteo de cuantas veces se repite esa calificacion en la lista de calificaciones.
  
  # Indicacion: Se le indica al usuario que ingresara nuevamente una calificacion para realizar un conteo de repeticiones.
  print("* A continuacion ingresaras nuevamente una calificacion especifica y se realizara un conteo de cuantas veces se repite * \n")
  
  # Entrada: Se le pide nuevamente al usuario ingresar una calificaciones de la lista de calificaciones.
  specific_value = int(input("Calificacion: "))
  
  validation_result = first_validation_grade(specific_value)
  
  # Separador
  print("")
  
  # Calculo: Se implementa un bucle for para calcular cuantas veces se repite la calificacion ingresada en la lista de calificaciones.
  amount_same_grades = 0
  if validation_result in grades:
    for grade in grades:
      if validation_result != grade:
        continue
      else:
        amount_same_grades += 1
        
  # Salida: Se le muestra al usuario la cantidad de veces que se repite la calificacion ingresada en la lista de calificaciones.
  print(f"La calificacion ingresada: {validation_result}, se repite {amount_same_grades} veces en la lista de calificaciones -> {grades}")
                
except ValueError:
  print("ERROR, Ingresaste un valor invalido, vuelve a intentarlo mas tarde.")