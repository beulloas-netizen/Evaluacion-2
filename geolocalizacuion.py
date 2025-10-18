import requests



#Tu API Key de Graphhopper

GRAPHOPPER_KEY = "1e543026-6bea-4e8f-81f0-70dec56e7bee"

URL = "https://graphhopper.com/api/1/route"



while True:

    print("\n=== Calculadora de Rutas con Graphhopper ===")

    origen = input("Ingrese el punto de origen (latitud,longitud) o 's' para salir: ").strip()

    if origen.lower() in ["s", "salir"]:

        print("Saliendo del programa...")

        break



    destino = input("Ingrese el punto de destino (latitud,longitud): ").strip()

    if destino.lower() in ["s", "salir"]:

        print("Saliendo del programa...")

        break



    try:

        # Parámetros de la API

        params = {

            "point": [origen, destino],

            "vehicle": "car",

            "locale": "es",

            "instructions": "true",

            "key": GRAPHOPPER_KEY

        }



        # Petición a la API

        response = requests.get(URL, params=params)

        data = response.json()



        if "paths" not in data:

            print("No se pudo calcular la ruta. Verifique los puntos ingresados.")

            continue



        ruta = data["paths"][0]

        distancia_km = ruta["distance"] / 1000  # convertir metros a km

        tiempo_min = ruta["time"] / 60000       # convertir ms a minutos



        print(f"\nDistancia total: {distancia_km:.2f} km")

        print(f"Tiempo estimado: {tiempo_min:.2f} minutos")

        print("\n=== Instrucciones paso a paso ===")

        for paso in ruta["instructions"]:

            print(f"- {paso['text']} ({paso['distance']:.2f} m)")



    except Exception as e:

        print(f"Error al procesar la ruta: {e}")
