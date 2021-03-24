# COUNTRIES
* **https://restcountries.eu/**
* **https://requests.readthedocs.io/en/master/**

* Ejercicio 1: Crea, en un directorio aparte, un entorno virtual y un archivo main.py
* Ejercicio 2: Instalar la librería requests
* Ejercicio 3: Hacer una request a la url que nos traiga todos los países del mundo
* Ejercicio 4: Crear una pequeña aplicación con las siguientes características:
	
	Debe permitirnos buscar países por nombre y por continentes
	Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitira los siguientes valores:
		name, capital, region, population, area, idioma (el primero), flag
		A su vez estos valores acturán como encabezados
	
	Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico
		EJ. dinámico --> Si se busca "africa", el archivo deberá llamarse --> africa.json
		
* Ejercicio 5: Agregar un mensaje asíncrono que indique al usuario que se está procesando su respuesta 
* Ejercicio 6: Agregar opción "population"
* Ejercicio 7: Al elegir la opción population se obtendrá la población total que el usuario haya indicado anteriormente, de no existir el archivo manejar el error
