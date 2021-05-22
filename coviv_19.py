def run():
    try:
        estados = [
        {"Estado":"Aguascalientes","Casos":3000},
        {"Estado":"Baja California","Casos":1500},
        {"Estado":"Baja California Sur","Casos":12000},
        {"Estado":"Campeche","Casos":1500},
        {"Estado":"Coahuila de Zaragoza","Casos":12000},
        {"Estado":"Colima","Casos":4000},
        {"Estado":"Chiapas","Casos":600},
        {"Estado":"Chihuahua","Casos":9000},
        {"Estado":"Ciudad de México","Casos":2460},
        {"Estado":"Durango","Casos":34200},
        {"Estado":"Guanajuato","Casos":31000},
        {"Estado":"Guerrero","Casos":12000},
        {"Estado":"Hidalgo","Casos":56000},
        {"Estado":"Jalisco","Casos":35679},
        {"Estado":"Estado de México","Casos":1294},
        {"Estado":"Michoacán","Casos":569679},
        {"Estado":"Morelos","Casos":12567},
        {"Estado":"Nayarit","Casos":7667},
        {"Estado":"Nuevo Leon","Casos":67676},
        {"Estado":"Oaxaca","Casos":13245},
        {"Estado":"Puebla","Casos":4554},
        {"Estado":"QUeretaro","Casos":45569},
        {"Estado":"Quintana Roo","Casos":23243},
        {"Estado":"San Luis Potosí","Casos":56565},
        {"Estado":"Sinaloa","Casos":55657},
        {"Estado":"Sonora","Casos":56767},
        {"Estado":"Tabasco","Casos":45676},
        {"Estado":"Tamaulipas","Casos":56776},
        {"Estado":"Tlaxcala","Casos":45687},
        {"Estado":"Veracruz","Casos":56760},
        {"Estado":"Yucatán","Casos":45656},
        {"Estado":"Zacatecas","Casos":45766}
        ]
        num=0
        selcción = ("Seleccione una opción:")
    
        for item in estados:
            num += 1
            print(num ,"-", item["Estado"] )
    
        opc = int(input("---------->"))

        print(estados[opc-1]["Estado"], " Registró ", estados[opc-1]["Casos"], " Hasta el 19 de mayo")
    except IndexError:
        print("Ingrese una opción válida")


if __name__ == "__main__":
    run()
