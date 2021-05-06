# COUNTRIES
* **https://restcountries.eu/**
* **https://requests.readthedocs.io/en/master/**

* Ejercicio 1: Crea, en un directorio aparte, un entorno virtual y un archivo main.py
* Ejercicio 2: Instalar la librería requests
* Ejercicio 3: Hacer una request a la url que nos traiga todos los países del mundo
* Ejercicio 4: Crear una pequeña aplicación con las siguientes características:
	
	Debe permitirnos buscar países por nombre y por continentes
	Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitirá los siguientes valores:
		name, capital, region, population, area, idioma (el primero), flag
		A su vez estos valores acturán como encabezados
	
	Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico
		EJ. dinámico --> Si se busca "africa", el archivo deberá llamarse --> africa.json
		
* Ejercicio 5: Agregar un mensaje asíncrono que indique al usuario que se está procesando su respuesta 
* Ejercicio 6: Agregar opción "population"
* Ejercicio 7: Al elegir la opción population se obtendrá la población total que el usuario haya indicado anteriormente, de no existir el archivo manejar el error
* Ejercicio 8: Luego de buscar un país e imprimirlo por pantalla preguntar si desea guardar la imagen del país encontrado.
* Ejercicio 9: Descargar la imagen indicada con anterioridad en --> ./images (Nota: El formato de las imágenes de restcountries es SVG)
* Ejercicio 10: Agregar una root function historial de búsqueda
* Ejercicio 11: La función del ejercicio 10, entregará los nombres y las poblaciones de todos los países previamente buscados de la siguiente manera name:value **\n** poblacion: value
* Ejercicio 12: Luego de mostrar la lista de países del ejercicio 10 preguntar si quiere descargar las banderas de los mismos
* Ejercicio 13: Descargar todas las imágenes en un directorio aparte
* Ejercicio 14: Crear una clase país attr--> name, capital, population
* Ejercicio 15: Convertir TODOS los países en un objeto y luego podamos acceder a un atributo de clase y nos indique la población total

MENU TIPO:
--REST Countries--
Country
Region
Population --> country||region --> if !country: req else: from json
Search history --> lista de países --> Quiere descargar las imágenes de las banderas ?  write wb:pass


