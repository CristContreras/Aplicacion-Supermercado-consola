import random as r  # Permite generar números random
import datetime  # Permite obtener la fecha
import os  # Permite limpiar la consola
import time  # Permite poner una pausa de segundos en la ejecución del programa
import main as d


# Funcion que permite al usuario loguearse
def login():
    pin = 0
    while pin == 0:
        cls()
        mostrar_credenciales_prueba()
        usuario = solicitar_usuario()
        pin = solicitar_pin(usuario)
    print("Iniciando sesión...")
    time.sleep(2)
    cls()
    saludar_emp(usuario)
    return usuario


# Funcion para mostrar un saludo al usuario logueado
def saludar_emp(usuario):
    print(
        f"Bienvenido/a {d.empleados[usuario]['nombre']} {d.empleados[usuario]['apellido']}\n"
    )


# Función para solicitiar el coigo de usuario
def solicitar_usuario():
    es_solicitud_aprobada = False
    while not es_solicitud_aprobada:
        usuario = pedir_numero("Ingrese su número de empleado: ")
        if es_usuario_valido(usuario):
            es_solicitud_aprobada = True
        else:
            print("Usuario no encontrado")

    return usuario


# Función para comprobar si un dato ingresado es un número
def es_numero(usuario: str):
    return usuario.isdigit()


# Función para mostrar las credenciales de ejemplo para acceso al sistema
def mostrar_credenciales_prueba():
    print("Credenciales para probar el sistema\n")
    print(
        "ROL: GERENTE\nID: 1\nPin:1234\n\nROL: CAJERO\nID: 4\nPin:2432\n\nROL: REPOSITOR\nID:9\nPin:5621\n"
    )


# Función para solicitar pin al usuario
def solicitar_pin(usuario):
    es_solicitud_aprobada = False
    while not es_solicitud_aprobada:
        pin = pedir_numero("ingrese su número de pin(cero para reiniciar): ")
        if pin != 0:
            if es_pin_valido(usuario, pin):
                es_solicitud_aprobada = True
            else:
                print("PIN incorrecto")
        else:
            return pin
    return pin


# Fución para validar el usuario
def es_usuario_valido(usuario):
    for emp in d.empleados.keys():
        if usuario == emp:
            return True
    return False


# Fución para validar el pin ingresado
def es_pin_valido(usuario, pin):
    id_clave = d.empleados[usuario]["claves"]
    if pin == d.claves[id_clave]["pin"]:
        return True
    else:
        return False


# Fución para cerrar sesión del usuario
def cerrar_sesion(usuario):
    usuario = 0
    print("\nCerrando sesión...")
    time.sleep(2)
    return usuario


# Función para mostrar el menú del repositor
def mostrar_menu_repositor():
    for item in obtener_op_repositor():
        print(item)


# Función para mostrar el menú dependiendo del rol
def mostrar_menu(codigo_rol):
    if codigo_rol == 1:
        mostrar_menu_gerente()
        print("")

    elif codigo_rol == 2:
        mostrar_menu_cajero()
        print("")
    elif codigo_rol == 3:
        mostrar_menu_repositor()
        print("")


# Función para obtener las funciones del repositor en strings
def obtener_op_repositor():
    list_op_repositro = [
        "1. Ver notificaciones",
        "2. Ver productos",
        "3. Cerrar sesión",
    ]
    return list_op_repositro


# Función para obtener las operaciones del gerente en strings
def obtener_op_gerente():
    list_op_gerente = [  # Agregar ver ganancias y productos mas vendidos
        "1. Agregar empleado",
        "2. Ver Empleados",
        "3. Ver Sueldos",
        "4. Ver Ganancia",
        "5. Ver Lista de ventas",
        "6. Ver Productos por ventas",
        "7. Cerrar sesión",
    ]
    return list_op_gerente


# Función para mostrar la ganancia calculada y el subtotal
def mostrar_ganancia():
    cls()
    print("=== GANANCIA ===")
    print(f"\nSubtotales: ${calcular_subtotales()}")
    print(f"\nLa ganancia es: ${calcular_ganancia()}")
    msj_volver()
    input()


# Función para calcular todos los subtotales
def calcular_subtotales():
    subtotales = 0
    for venta in d.ventas:
        subtotales += d.ventas[venta]["subtotal"]
    return subtotales


# Función para calcular la ganancia
def calcular_ganancia():
    costo_total = 0.0
    for clave in d.ventas_productos:
        costo_total += (
            d.productos[d.ventas_productos[clave]["id_producto"]]["costo"]
            * d.ventas_productos[clave]["cantidad"]
        )

    ganancia = calcular_subtotales() - costo_total
    return ganancia


# Función para el respositor, muestra las notificaciones almacenadas en el diccionario
def mostrar_notificaciones():
    cls()
    print("=== NOTIFICACIONES ===")
    if len(d.notificaciones) > 0:
        hay_notificacion = False
        for clave in d.notificaciones.keys():
            print(f"ID: {clave} Mensaje: {d.notificaciones[clave]['mensaje']}")
            hay_notificacion = True
        if not hay_notificacion:
            print("No hay notificaciones para mostrar.")
    else:
        print("No hay notificaciones para mostrar.")
    msj_volver()
    input()


# Función para mostrar todos los productos del diccionario
def mostrar_productos():
    cls()
    print("=== VER PRODUCTOS ===\n")
    if len(d.productos) > 0:
        # ordenamos y mostramos cada producto del diccionario productos
        for clave in sorted(d.productos.keys()):
            print(
                f"Id: {clave} Nombre: {d.productos[clave]['nombre']} precio: {d.productos[clave]['precio']} stock: {d.productos[clave]['stock']} categoria: {d.productos_cat[d.productos[clave]['categoria']]} \n"
            )
    else:
        print("No hay productos para mostrar.")
    msj_volver()
    input()


# Función para imprimir las operaciones del gerente
def mostrar_menu_gerente():
    for item in obtener_op_gerente():
        print(item)


# Función para obtener la lista de operaciones del cajero
def obtener_op_cajero():
    list_op_cajero = ["1. Iniciar Venta Nueva", "2. Cerrar Sesión"]
    return list_op_cajero


# Función para mostrar el menú del cajero
def mostrar_menu_cajero():
    for item in obtener_op_cajero():
        print(item)


# Función para obtener el rol del diccionario de empleados
def obtener_codigo_rol(usuario):
    codigo_rol = d.empleados[usuario]["empleados_rol"]
    return codigo_rol


# Función para solicitar la operacion del usuario
def solicitar_operacion():
    es_numero_valido = False
    while not es_numero_valido:
        op = pedir_numero("Ingrese la operación: ")
        es_numero_valido = True
    return op


# Función para mostrar todos los empleados del diccionario de empleados
def mostrar_empleados():
    cls()
    print("=== VER EMPLEADOS ===\n")
    if len(d.empleados) > 0:
        # ordenamos y mostramos cada empleado del diccionario empleados
        for clave in sorted(d.empleados.keys()):
            print(
                f"Id: {clave} DNI: {d.empleados[clave]['dni']} "
                + "Nombre: "
                + d.empleados[clave]["nombre"]
                + " "
                + "Apellido: "
                + d.empleados[clave]["apellido"]
                + " "
                + "Rol: "
                + d.empleados_rol[d.empleados[clave]["empleados_rol"]]["nombre"]
                + " "
                + "Turno : "
                + d.empleados_turno[d.empleados[clave]["empleados_turno"] - 1]
                + "\n"
            )
    else:
        print("No hay empleados para mostrar.")
    msj_volver()
    input()


# Función para mostrar todos los sueldos de cada rol
def mostrar_sueldos():
    cls()
    print("=== VER SUELDOS ===\n")
    # ordenamos y mostramos cada empleado del diccionario empleados
    for clave in sorted(d.empleados_rol.keys()):
        print(
            f"Rol: {d.empleados_rol[clave]['nombre']} Sueldo: {d.empleados_rol[clave]['sueldo']} \n"
        )
    msj_volver()
    input()


# Función para acceder al menu correspondiente según el codigo de rol y operación seleccionada
def procesar_operacion(op, codigo_rol, usuario):
    es_opcion_valida = False
    while not es_opcion_valida:
        if codigo_rol == 1:
            if op == 1:
                agregar_emp()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 2:
                mostrar_empleados()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 3:
                mostrar_sueldos()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 4:
                mostrar_ganancia()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 5:
                ver_lista_ventas()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()

            elif op == 6:
                ver_productos_ventas()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 7:
                usuario = cerrar_sesion(usuario)
                es_opcion_valida = True
            else:
                es_opcion_valida = False
                mostrar_op_incorrecta(codigo_rol)
                op = solicitar_operacion()

        # Cajero
        elif codigo_rol == 2:
            if op == 1:  # iniciar venta
                iniciar_venta(usuario)
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()

            elif op == 2:
                usuario = cerrar_sesion(usuario)
                es_opcion_valida = True
            else:
                es_opcion_valida = False
                mostrar_op_incorrecta(codigo_rol)
                op = solicitar_operacion()

        # repositor
        elif codigo_rol == 3:
            if op == 1:
                mostrar_notificaciones()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()

            elif op == 2:
                mostrar_productos()
                cls()
                saludar_emp(usuario)
                mostrar_menu(codigo_rol)
                op = solicitar_operacion()
            elif op == 3:
                usuario = cerrar_sesion(usuario)
                es_opcion_valida = True
            else:
                es_opcion_valida = False
                mostrar_op_incorrecta(codigo_rol)
                op = solicitar_operacion()
    return usuario


# Función para calcular y devolver el subtotal de una venta
def calcular_subtotal(carrito: list):
    subtotal = 0
    for producto in carrito:
        cantidad = producto[4]
        precio = producto[5]
        subtotal += cantidad * precio
    return subtotal


# Función para calcular el total de la venta
def calcular_total(carrito: list):
    total = 0
    for producto in carrito:
        precio = producto[5]
        iva = producto[6]
        cantidad = producto[4]
        if iva > 0:
            while cantidad >= 1:
                total += ((precio * iva) / 100) + precio
                cantidad -= 1
        else:
            total += precio * cantidad
    return total


# Función para verificar si existe el producto en el diccionario de productos
def existe_producto(codigo_prod):
    existe_producto = False
    for clave in d.productos.keys():
        if codigo_prod == clave:
            existe_producto = True
    return existe_producto


# Función para iniciar una nueva venta, solicitar datos, comprobar stock, notificar si es baja de stock, y almacenar en el diccionario de ventas y ventas_producto
def iniciar_venta(usuario):
    cls()
    print("=== NUEVA VENTA ===\n")
    if len(d.productos) > 0:
        fechayhora = datetime.datetime.now().replace(microsecond=0)
        carrito = []
        codigo_prod = 1
        # ingresara productos hasta que codigo sea cero
        while codigo_prod != 0:
            print("Para finalizar ingrese 0 (cero)")
            # ingreso codigo de producto
            codigo_prod = pedir_numero("\nIngrese código de producto: ")
            # si cod prod es distinto a cero, hacer
            if codigo_prod != 0:
                if existe_producto(codigo_prod):
                    print(f"\nProducto: {d.productos[codigo_prod]['nombre']}")
                    print(f"Cantidad disponible: {d.productos[codigo_prod]['stock']}")
                    cantidad = pedir_numero("\nIngrese la cantidad: ")
                    # mientras la cantidad sea mayor a cero
                    while cantidad > 0:
                        # si el stock supera a lo pedido
                        if d.productos[codigo_prod]["stock"] >= cantidad:
                            # agrega el producto al carrito
                            carrito.append(
                                [
                                    codigo_prod,
                                    d.productos[codigo_prod]["nombre"],
                                    d.productos[codigo_prod]["marca"],
                                    d.productos[codigo_prod]["categoria"],
                                    cantidad,
                                    d.productos[codigo_prod]["precio"],
                                    d.productos[codigo_prod]["iva"],
                                ]
                            )
                            # descontar y actualizar stock disponible
                            actualizar_stock = (
                                d.productos[codigo_prod]["stock"] - cantidad
                            )
                            d.productos[codigo_prod]["stock"] = actualizar_stock
                            # cortar el while
                            cantidad = -1
                            # region si hay menos de 11 productos avisar que falta stock
                            if d.productos[codigo_prod]["stock"] <= 10:
                                codigo_notificacion = r.randint(
                                    1000, 9999
                                )  # tiene q verificar  q no existe ( si existe volver a iterar)
                                for notificacion in sorted(d.notificaciones.keys()):
                                    if codigo_notificacion == notificacion:
                                        notificacion += 1
                                mensaje = f"{datetime.datetime.now().replace(microsecond=0)} Falta stock, ID: {codigo_prod}, Nombre: {d.productos[codigo_prod]['nombre']} Disponible: {d.productos[codigo_prod]['stock']}"
                                d.notificaciones[codigo_notificacion] = {
                                    "Fecha": fechayhora,
                                    "mensaje": mensaje,
                                }
                            # endregion
                        else:  # Si la cantidad supera la almacenada
                            print("\nCantidad supera la almacenada")
                            # mostrar stock disponible
                            print(
                                f"\nCantidad disponible: {d.productos[codigo_prod]['stock']}"
                            )
                            cantidad = pedir_numero("\nIngrese la cantidad: ")
                    # mostrar carrito actual
                    print("\n   DETALLE DE VENTA")
                    for producto in carrito:
                        print("\nProducto: " + producto[1])
                        print("Marca: " + producto[2])
                        print(f"Cantidad: {producto[4]}")
                        print(f"Precio: ${producto[5]}")

                    # calcular subtotal
                    subtotal = calcular_subtotal(carrito)
                    # mostrar subtotal actual
                    print(f"\nSubtotal: ${subtotal}\n")
                else:
                    print("Error. El producto no existe\n")
        if len(carrito) > 0:
            # si no hay mas productos, calcular precio total con iva
            precio_total = calcular_total(carrito)
            # mostrar precio total
            print("\n===============================================")
            print(f"\nPrecio total con iva incluido: ${precio_total}")

            # solicita dinero
            dinero_cliente = 0.0
            while dinero_cliente < precio_total:
                dinero_cliente = float(input("\nIngrese el dinero: "))
                if dinero_cliente > precio_total:
                    vuelto = dinero_cliente - precio_total
                    print(f"\nVuelto: ${vuelto}")
                else:
                    print("\nEl dinero ingresado es insuficiente. Vuelva a intentarlo")

            # Sección para guardar en el diccionario
            codigo_venta = r.randint(1000, 9999)  # encuentra un id disponible
            for venta_id in sorted(d.ventas.keys()):
                if codigo_venta == venta_id:
                    codigo_venta += 1

            # almancear la venta
            d.ventas[codigo_venta] = {
                "fecha": fechayhora,
                "codigo_vendedor": usuario,
                "subtotal": subtotal,
                "total": precio_total,
            }

            # itrear sobre carrito
            for lista_carro in carrito:
                # buscar posicion disponible en venta_productos
                cod_prod_venta = r.randint(1000, 9999)  # encuentra un id disponible
                for clave in sorted(d.ventas_productos.keys()):
                    if cod_prod_venta == clave:
                        cod_prod_venta += 1

            d.ventas_productos[cod_prod_venta] = {
                "id_venta": codigo_venta,
                "id_producto": lista_carro[0],
                "nombre": lista_carro[1],
                "marca": lista_carro[2],
                "categoria": lista_carro[3],
                "cantidad": lista_carro[4],
                "precio": lista_carro[5],
            }
            print("\nVenta realizada correctamente.")
    else:
        print("No hay productos almacenados.")
    msj_volver()
    input()


# Función para mostrar todas las ventas realizadas
def ver_lista_ventas():
    cls()
    print("== LISTA DE VENTAS ==")
    if len(d.ventas) > 0:
        # muestra lista de ventas
        for clave in d.ventas:
            print(
                f"\nID: {clave} Fecha: {d.ventas[clave]['fecha']} Codigo_empleado: {d.ventas[clave]['codigo_vendedor']} Subtotal: ${d.ventas[clave]['subtotal']} Total: ${d.ventas[clave]['total']}"
            )
    else:
        print("No hay ventas para mostrar.")
    msj_volver()
    input()


# Función para ver los productos de cada venta
def ver_productos_ventas():
    cls()
    print("\n== PRODUCTOS POR VENTA ==")
    # lista de productos por venta
    if len(d.ventas_productos) > 0:
        for clave in d.ventas_productos:
            print(
                f"\nID: {clave} ID Venta: {d.ventas_productos[clave]['id_venta']} Nombre: {d.ventas_productos[clave]['nombre']} Marca: {d.ventas_productos[clave]['marca']} Cantidad: {d.ventas_productos[clave]['cantidad']} Precio(sin iva): ${d.ventas_productos[clave]['precio']}"
            )
    else:
        print("No se realizaron ventas aún.")
    msj_volver()
    input()


# Función para mostrar un mensaje para volver
def msj_volver():
    print("\nPresione enter para volver")


# Función para indicar que se inserto un codigo incorrecto
def mostrar_op_incorrecta(codigo_rol):
    print("Operacion ingresada incorrecta")
    mostrar_menu(codigo_rol)


# Función para mostrar los turnos de empleados de la tupla
def mostrar_turnos():
    i = 0
    for turnos in d.empleados_turno:
        i += 1
        print(str(i) + ". " + turnos)


# Función para mostrar los roles que existe en la tupla
def mostrar_roles():
    i = 0
    for rol_emp in d.empleados_rol:
        i += 1  # utilizo la variable por si se guarda otro rol
        print(str(i) + ". " + d.empleados_rol[rol_emp]["nombre"])


# Función para solicitar un número y validarlo, devuelve el número
def pedir_numero(solicitud: str):
    error_msj = "Debe ingresar solo números"
    testear = input(solicitud)
    while not es_numero(testear):
        print(error_msj)
        testear = input(solicitud)
    numero = int(testear)
    return numero


# Función para pedir letras o texto, validarlo y devolverlo
def pedir_letras(solicitud: str):
    error_msj = "Debe ingresar solo letras"
    testear = input(solicitud)
    # es_letra = es_numero(testear)
    texto = [testear]
    existe_numero = False
    while not existe_numero:
        for palabra in texto:
            for letra in palabra:
                if es_numero(letra):
                    existe_numero = True
        if existe_numero:
            print(error_msj)
            testear = input(solicitud)
            texto.clear()
            texto.append(testear)
            existe_numero = False
        else:
            existe_numero = True
    letras = texto[0]
    return letras


# Función para agregar un nuevo empleado y almacenarlo en el diccionario de empleados
def agregar_emp():
    cls()
    print("=== AGREGAR EMPLEADO ===\n")
    # Solicitamos datos
    dni_emp = pedir_numero("Ingrese DNI del empleado sin puntos: ")
    nombre_emp = pedir_letras("\nIngrese nombre del empleado: ")
    apellido_emp = pedir_letras(
        "\nIngrese apellido del empleado: "
    )  # control de string

    # mostrar turnos
    print("\nSeleccione un turno\n")

    mostrar_turnos()
    # controlar q sea turno correcto
    turno_emp = pedir_numero("\nIngrese el turno: ")

    # seleccionr rol
    print("\nSelecione un rol\n")
    mostrar_roles()
    # controlar numero
    rol_emp = pedir_numero("\nIngrese el Rol: ")
    # ingresar pin
    pin_emp = pedir_numero("\nIngrese pin: ")
    # validr datos
    print("\n¿Son correctos los datos ingresados?\n")
    print(f"DNI: {dni_emp}")
    print(f"Nombre: {nombre_emp}")
    print(f"Apellido: {apellido_emp}")
    print(f"Turno: {turno_emp}.{d.empleados_turno[turno_emp]}")
    print(f"Rol: {rol_emp}.{d.empleados_rol[rol_emp]['nombre']}")
    print(f"Pin: {pin_emp}")

    # confirmar
    es_op_valida = False
    while not es_op_valida:
        respuesta = pedir_letras("\nIngrese si o no: ")

        respuesta = respuesta.lower().strip()

        if respuesta == "si":
            # generar codigo emp
            codigo_emp = r.randint(1000, 9999)
            for idemp in sorted(d.empleados.keys()):
                if codigo_emp == idemp:
                    codigo_emp += 1

            ultima_pos = 1
            for idclave in sorted(d.claves.keys()):
                if ultima_pos == idclave:
                    ultima_pos += 1

            # inserto el pin en posicion disponible encontrada
            d.claves[ultima_pos] = {"pin": int(pin_emp)}

            d.empleados[codigo_emp] = {
                "dni": dni_emp,
                "nombre": nombre_emp,
                "apellido": apellido_emp,
                "claves": ultima_pos,
                "empleados_turno": turno_emp,
                "empleados_rol": rol_emp,
            }

            print("\nEmpleado guardado correctamente\n")
            es_op_valida = True
        elif respuesta == "no":
            print("\nOperación cancelada\n")
            es_op_valida = True
        else:
            print("\nError. Debe ingresa si o no\n")
    time.sleep(2)


# Función para limpiar la consola
def cls():
    os.system("cls")
