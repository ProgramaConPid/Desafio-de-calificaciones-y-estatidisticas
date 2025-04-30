# Actividad: Desafio de calificaciones y estadisticas

## Paso #1: Determinar el estado de aprobacion de una calificacion
# - Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# - Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

try:
  # Entrada: Solicitar nombre y calificacion al usuario
  user_name = str(input("Ingresa tu nombre: ")).capitalize()
  user_last_name = str(input("Ingresa tu Apellido: ")).capitalize()
  
  print("")
  
  # Validacion: Verificar que el usuario ingrese un nombre valido.
  while not user_name.isalpha() and not user_last_name.isalpha():
    error_name = str(input("ERROR, Ingresa un nombre valido: ")) 
    user_name = error_name
    print("------------------------------------------")
  
  user_note = int(input("Ingresa una calificacion entre 0 - 100: "))
  
  # Entrada: Se crea un diccionario vacio que mas adelante mostrara tanto datos como estado de aprobacion de el usuario
  data = {}
  
  # Validacion: Verificar que el usuario haya ingresado una calificacion correcta
  if user_note < 0 and user_note > 100:
    print(f"La calificacion {user_note} no se encuentra en el rango especificado.") 
  else:
    # Validacion: Verificar y determinar el estado de aprobacion 
    if user_note >= 50:
      print("A continuacion veras los datos ingresado y el estado de aporbacion. \n")
      
      data = {
        "Nombre usuario": user_name,
        "Apellido usuario": user_last_name,
        "Calificacion ingresada": user_note,
        "Estado": "Aprobado"
      }
      
      print(f"""
        Nombre usuario => {data['Nombre usuario']} {data[user_last_name]}  
        Calificacion ingresada => {data['Calificacion ingresada']}
        Estado => {data['Estado']}    
      \n""")
      
    else:
      print("A continuacion veras los datos ingresado y el estado de aporbacion. \n")
      
      data = {
        "Nombre usuario": user_name,
        "Calificacion ingresada": user_note,
        "Estado": "Desaprobado",
        "Mensaje motivacional": "La proxima vez te ira mejor."
      }
      
      print(f"""
        Nombre usuario => {data['Nombre usuario']} {data[user_last_name]}  
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
  
  grades = []
  amount_grades = int(input("Cantidad de calificaciones que ingresaras (MIN 2 - MAX 15): "))
  while amount_grades < 2 and amount_grades > 15:
    error_amount = int("\nERROR, Ingresa una cantidad valida: ")
    amount_grades = error_amount
  
  print(amount_grades)
  
except ValueError:
  print("ERROR, Ingresaste un valor invalido.")