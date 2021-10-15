def docente (informacion:dict) -> dict:
    nueva_informacion = {"nombre": informacion["nombre"], "sueldo": 0, "prima_servicio": 0, "educacion": informacion["educacion"], "activo":True,
                        "horas_trabajo": informacion["horas_trabajo"] }
    informacion1= {"categoria": informacion["categoria"], "id_docente": informacion["id_docente"]}
        
    if informacion1["categoria"] == "A":
        nueva_informacion["activo"]= True
        if informacion["horas_trabajo"] >=2500 and informacion["horas_trabajo"]<=3000:
            nueva_informacion["sueldo"]= 7000000
            nueva_informacion["prima_servicio"] = 0.30*nueva_informacion["sueldo"]
        else: 
            nueva_informacion["sueldo"]= 7000000
            nueva_informacion["prima_servicio"] ="N/A"
    if informacion1["categoria"] == "B":
        nueva_informacion["activo"]= True
        if informacion["horas_trabajo"] >=1500 and informacion["horas_trabajo"]<=2000:
            nueva_informacion["sueldo"]= 5000000
            nueva_informacion["prima_servicio"] = 0.35*nueva_informacion["sueldo"]
        else: 
            nueva_informacion["sueldo"]= 5000000
            nueva_informacion["prima_servicio"] ="N/A"
    if informacion["categoria"] == "C":
        nueva_informacion["activo"]= True
        if informacion["horas_trabajo"] >=1000 and informacion["horas_trabajo"]<=2000:
            nueva_informacion["sueldo"]= 3000000
            nueva_informacion["prima_servicio"] = 0.40*nueva_informacion["sueldo"]
        else: 
            nueva_informacion["sueldo"]= 3000000
            nueva_informacion["prima_servicio"] ="N/A"
    if informacion["categoria"] == "D":
        nueva_informacion["activo"]= False
        if informacion["horas_trabajo"] >=900 and informacion["horas_trabajo"]<=2000:
            nueva_informacion["sueldo"]= 2500000
            nueva_informacion["prima_servicio"] = 0.50*nueva_informacion["sueldo"]
        else: 
            nueva_informacion["sueldo"]= 2500000
            nueva_informacion["prima_servicio"] ="N/A"
        
    if informacion["categoria"] != "A" and informacion["categoria"] != "B" and informacion["categoria"] != "C" and informacion["categoria"] != "D":
        nueva_informacion["sueldo"]= "N/A"
        nueva_informacion["activo"]= "N/A"
        nueva_informacion["horas_trabajo"]= "N/A"
        nueva_informacion["prima_servicio"] = "N/A"
    return nueva_informacion   
        
informacion = {
    "id_docente": 3,
    "nombre": "Lorena Cuayal",
    "categoria": "E",
    "educacion": "Doctorado",
    "horas_trabajo": 3000
}
print(docente(informacion))