# Caso 1
paciente = { 10852758781: { "nombres": "Julian", "apellidos": "Gomez, Lopez", "edad": 20, "barrio": "La colina", "barrios": [ { "comuna": 1,
 "autorizado": "si" }, ] }, 1010275871: { "nombres": "Adriana Lucia", "apellidos": "Melo, Castillo", "edad": 35, "barrio": "Aranda","barrios": [  { "comuna": 2, "autorizado": "si" }, ] },  10102758715: { "nombres": "Mike Angel", "apellidos": "Santacruz, Cruz", "edad": 40, "barrio": "Los dos puentes", "barrios": [ { "comuna": 3, "autorizado": "si" }, ] }, 10122758089: { "nombres": "Felipe", "apellidos": "Fajardo, Quintero", "edad": 55, "barrio": "Bolivar", "barrios": [ { "comuna": 3, "autorizado": "si" }, ] }, 101227580874: { "nombres": "Juan Carlos", "apellidos": "Jojoa, Ruiz", "edad": 90, "barrio": "Triunfo", "barrios": [ { "comuna": 4, "autorizado": "no" }, ] }}
# salida 1
# (['a.melo@gmail.com', 'f.fajardo@gmail.com', 'j.gomez@gmail.com', 'm.santacruz@gmail.com'], {10852758781: {'nombres': 'Julian', 'apellidos': 'Gomez, Lopez', 'edad': 20, 'barrio': 'La colina', 'barrios': [{'comuna': 1, 'autorizado': 'si'}]}, 1010275871: {'nombres': 'Adriana Lucia', 'apellidos': 'Melo, Castillo', 'edad': 35, 'barrio': 'Aranda', 'barrios': [{'comuna': 2, 'autorizado': 'si'}]}, 10102758715: {'nombres': 'Mike Angel', 'apellidos': 'Santacruz, Cruz', 'edad': 40, 'barrio': 'Los dos puentes', 'barrios': [{'comuna': 3, 'autorizado': 'si'}]}, 10122758089: 
# {'nombres': 'Felipe', 'apellidos': 'Fajardo, Quintero', 'edad': 55, 'barrio': 'Bolivar', 'barrios': [{'comuna': 3, 'autorizado': 'si'}]}})
# caso 2
# paciente = { 1010005878: { "nombres": "Luis Carlos", "apellidos": "Gomez, Lopez", "edad": 20, "barrio": "La colina", "barrios": [ { "comuna": 1, "autorizado": "no" }, ] }, 1010205871: { "nombres": "Lucia", "apellidos": "Melo, Castillo", "edad": 35, "barrio": "Aranda", "barrios": [
#  { "comuna": 2, "autorizado": "no" }, ] }, 10002758715: { "nombres": "Angel", "apellidos": "Santos, Cruz", "edad": 40, "barrio": "Los dos puentes", "barrios": [ { "comuna": 3, "autorizado": "no" }, ] }, 18122700089: { "nombres": "Ana Maria", "apellidos": "Fernandez, Moran", "edad": 55, "barrio": "Bolivar", "barrios": [ { "comuna": 3, "autorizado": "no"  }, ] }, 1027580874: { "nombres": "Juan Carlos", "apellidos": "Jojoa, Ruiz", "edad": 90, "barrio": "Triunfo", "barrios": [ { "comuna": 4, "autorizado": "no" }, ] }}
#  salida 2
#  ([], {})

def validar_paciente(paciente:dict) -> tuple:
    for identificacion, nombres in paciente.items():
        for comuna, autorizado in barrios.values():
            nombre=nombres["nombres"]
            autorizado= barrios[autorizado]
            if autorizado == "si".lower():
                correo= [paciente["nombre",0].lower()]
                correo=correo.insert(1,".")
                correo= correo.insert(2, paciente["apellidos",0].lower())
                correo=correo.insert(3,"@gmail.com".lower())
            if autorizado == "no":
                paciente.pop(identificacion)
    return correo

print  (validar_paciente(paciente))    
    # pass

# for codigo, registro in paciente.items():
#         barrios = registro['barrios']
#         for area in barrios:
#             autorizado = area['autorizado']
#         if autorizado == "no":
#             fun.pop(codigo)
#     correos = listadoCorreos(fun)
#     tupla = (correos, fun)
#     return(tupla)

#([Correos ordenados], {Diccionario de entrada filtrado}) #Se debe tener en cuenta que se debe retornar una tupla la cual debe tener como primer elemento una lista ordenada de los correos y el segundo elemento debe ser un diccionario con la estructura de la tabla inicial, tanto la lista como los diccionarios deben ser de pacientes con barrios autorizados es decir con autorizado: "si"
