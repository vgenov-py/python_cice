# TIA Covid-19

# NOMENCLATURA EN INGLÉS

##Recopilación

1. Crear un json con todos los datos obtenidos en la response, de este punto en adelante, solo se consultará **nuestro json**

* Este dataset funciona de la siguiente manera, cada día que pasa se agregan todos los municipios con su nuevo valor acumulativo.
* Por ende, no se reescriben, se agregan (append) todos los municipios cada vez

2. Sin contar la reescrituras, cuántos municipios hay en total? O lo que es lo mismo, cuántos diccionarios se agregan cada día?
3. Obtener la TIA inicial
4. Obtener la TIA final
5. Crea una lista con valores de 1 a **n** siendo 1 la primer fecha y **n** la última
* Esta lista representará el eje **x**
6. Crea una lista con la TIA diaria de la comunidad (Cada valor será la sumatoria de todos los municipios)
* Esta lista representará el eje **y**


## OOP

1. Crea en un fichero aparte, un objeto llamado statistics
2. Tendrá los siguiente atributos: x (list), y (list)
3. Propiedades: n, media de x, media de y, varianza de x, varianza de y, sumatoria xy, sumatoria x^2, sumatoria y^2, sumatoria x^2y^2, covarianza,b b0
4. Métodos: coeficiente pearson, y'

# En conjunto

1. Cuál es el coeficiente de pearson?
2. Cuál es el valor de la covarianza
3. b
4. b0
5. Pasando 10 días, cuál será el valor de la TIA de la comunidad?
6. Cuál era el valor de Pearson durante el confinamiento

## Gráficas

1. Representar los últimos 20 días en una gráfica



