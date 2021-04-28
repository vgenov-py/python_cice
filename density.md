## Comprobación de una ley
* https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json
* Para poder realizar este ejercicio deberán descargar el archivo JSON en éste mismo repositorio
* Ejercicio 1: Obtener la densidad media de los municipios de Madrid
* Ejercicio 2: Obtener municipio por codigo ine // Extra: utilizando función filter
* Ejercicio 3: Obtener el municipio más grande
* Ejercicio 4: Obtener los 10 municipios con mayor densidad poblacional
* Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
	* la lista 1 tendrá todos los valores de densidad que empiecen por 1
	* la lista 2 tendrá todos los valores de densidad que empiecen por 2
	ej:
	lista_1 = ["134324", "1354211", "349.34"]
	

## OOP
* Ejercicio 5: Crear una clase de tipo municipality/municipio
	* Debe tener nombre, superficie, densidad
* Ejercicio 6: Crear una función que acepte un solo parámetro (municipio) y que devuleva un objecto con las propiedades (nombre, densidad, superfice)
* Ejercicio 7: Modificar el tipo de impresión (print) para que se vea así --> nombre: valor
										 densidad: float con tres decimales
										 superficie: float con tres decimales
* Ejercicio 8: Crear una función que acepte como parámetro toda la lista de diccionarios y devuelva una lista de objetos
* Ejercicio 9: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2, crear un MÉTODO 
	(una función dentro del objeto) que devuelva la población del municipio dado
* Ejercicio 10: Ya que tenemos una lista con todos los objetos, con su método "get_total_density()" 
	obtener la población de la comunidad de Madrid


* Ejercicio 11: Crea un contador de modo que cada vez que se cree una nueva instancia, el mencionado contador aumente en 1
* Ejercicio 12: Crea un classmethod llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"
* Ejercicio 13: Estable una tasa de crecimiento anual del 2%
* Ejercicio 14: Define un método que aplique el crecimiento anual sobre un objeto
* Ejercicio 15: Convertir el método del ejercicio 10 en propiedad
* Ejercicio 16: Modificiar el print() para que también devuelva la población
* Ejercicio 17: Define un set_anual_growth que permita modificar la tasa de crecimiento
* Ejercicio 18: Agregar un Error Handeling para verficar que el type pasado como argumento en from_string sea un float

CSV
* Ejercicio 19: Crear un backup de todos nuestros objetos en un fichero tipo CSV
