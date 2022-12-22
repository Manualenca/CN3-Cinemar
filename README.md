# CN3-Cinemar
# Evaluación del Curso de Python

# Sistema de Gestión.

Cinemar.

Contexto.

Cinemar es una empresa que se dedica a proyectar películas esencialmente
dedicadas al público adolescente.
El cine cuenta con una cantidad de salas con diferentes capacidades (siendo
esta capacidad la cantidad de butacas), también dispone de salas 2D como 3D
variando el precio de las entradas.
Cuando un cliente se presenta en ventanilla muestra su tarjeta de descuento, si
la tiene, se le efectúa un descuento en el valor de la entrada, sino pueden solicitar una
sí acudieron al menos 6 veces en 3 meses, en caso contrario el precio de la entrada no
tendrá descuento alguno.
Actualmente la tabla de descuentos para los que tienen la tarjeta de
descuentos es la siguiente:
- Lunes y Miércoles: 20%
- Martes y Jueves: 15%
- Viernes, Sábados y Domingos: 10%

Siendo modificable según los directivos.

Problemática
Los directivos de Cinemar comentaron a nuestro equipo que no cuentan con un
control de los clientes, para realizar reservas de butacas y otorgarles descuentos para
aquellos que son más recurrentes de forma automática.
Todo se efectúa mediante ventanilla y a mano, lo que provoca que en algunas
salas a veces se terminan vendiendo más entradas que la capacidad de la sala, y
perdiendo ventas en funciones por no contar con reservas por página web en horarios
específicos.

Solución
Nos llega desde la administración del cine a nuestro equipo de desarrolladores
que tenemos que implementar una solución que nos permita lo siguiente.
Para el cliente:
- Registrarse.
- Iniciar sesión. (Opcional)
- Crear una reserva.
- Modificar una reserva.
- Observar mis reservas.
- Ver el histórico de mis entradas.
Para la Administración:
- Ver reservas de todos los clientes.
- Ver reservas de un cliente en particular.
- Crear una sala con la película.
- Modificar una sala.
- Eliminar una sala.
- Modificar descuentos.
Troncales
- Ver salas
Consideraciones
- No se vencerán las películas, sino que será por la creación de una sala.
- La reserva implica el pago de la entrada.
- Las reservas solo se pueden modificar siempre y cuando se hagan antes de la
función.
- Las funciones son todos los días.
- No se contempla los procesos relacionados a la tarjeta de descuento.

Entregables

Checkpoint 1 (Fecha: 31/10 al 09/11) (opcional)
1) Elaborar un diagrama de clases proponiendo la solución.
2) Elaborar otro diagrama de clases mostrando el método de registro de clientes e inicio de sesión. (opcional)

Checkpoint 2 (Fecha: 14/11 al 23/11)
1) Elaborar el DER (diagrama de entidad relación) de la solución. (opcional)
2) Presentar los Script de generación de esquemas de la base de datos.

Checkpoint 3 (Fecha: 28/11 - 14/12)
1) Avances en codificación y dudas técnicas.

Entrega Final (Fecha: 19/12)
1) Presentación grupal del proyecto.
2) Explicación del código.
3) Decisiones de diseño
