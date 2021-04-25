# Desfibriladores fuera del ámbito sanitario

https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json

## Crear vuestra propia BBDD (JSON)

### Conocer tu dataset

1. Cuántos DEAS hay en total
2. Considerando solo los DEAS de los códigos postales dentro de la M-30, cuántos hay?
3. Cuántos se encuentran en entidades públicas y cuántos en privadas?

### Menú

1. Crear un menu
	* (1)
	* Crear usuario
	* Acceder
	* Admins
	* Salir
	
2. Crear usuario:
	* (2)
	* Que permita crear un usuario con campos nombre y contraseña
	* Que sea guardado en otro JSON para USERS 
	
3. Acceder: (SOLO si la información concuerda con lo que el usuario ha colocado)
	* (3)
	* Buscar DEA por código
	* Buscar DEA por distancia
	
4. Admins: (SOLO si contraseña PREdefinida)
	* (4)
	* Agregar
	* Modificar
	* Eliminar
	

### OOP

1. Crear objeto DEA con x,y
	* Método H
2. Crear objeto User nombre, contraseña
	* Método distancia (x, y, target)
3. Crear hijo Admin
	* Métodos CRUD







