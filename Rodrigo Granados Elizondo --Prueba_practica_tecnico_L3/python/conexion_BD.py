import mysql.connector

conexion=mysql.connector.connect(user='root', password='sql12345',
                                     host='localhost',
                                     database='prueba_istmocenter', port='3306')

insertar=conexion.cursor()



## Definicion de las funciones para un menu sencillo del control de la entidad-relacion de las
## tablas establecidas

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        
        '1': ('Opción 1 _ Insertar en tabla panelpersons', accion1),
        '2': ('Opción 2 _ Insertar en tabla panelinventory', accion2),
        '3': ('Opción 3 _ Mostrar contenido de las tablas', accion3),
        '4': ('Opción 4 _ Eliminar una fila de la tabla panelpersons', accion4),
        '5': ('Opción 5 _ Eliminar una fila de la tabla panelinventory', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():
    print('Has elegido Insertar en tabla panelpersons')
    PERSON_NAME = input('Escriba PERSON_NAME: ')
    PERSON_EMAIL = input('Escriba PERSON_EMAIL: ')
    PERSON_PASSWORD = input('Escriba PERSON_PASSWORD: ')

    sql = "INSERT INTO panelpersons ( PERSON_NAME, PERSON_EMAIL, PERSON_PASSWORD) VALUES (%s, %s, %s)"
    val = (PERSON_NAME, PERSON_EMAIL, PERSON_PASSWORD)

    insertar.execute(sql, val)

    conexion.commit()

    print(insertar.rowcount, "registro insertado")


def accion2():
    print('Has elegido Insertar en tabla panelinventory')
    ITEM_BARCODE = input('Escriba ITEM_BARCODE: ')
    CREATED = input('Escriba CREATED: ')
    CREATED_BY = input('Escriba CREATED_BY: ')

    sql = "INSERT INTO panelinventory (ITEM_BARCODE, CREATED, CREATED_BY) VALUES (%s, %s, %s)"
    val = (ITEM_BARCODE, CREATED, int(CREATED_BY))

    try:
        insertar.execute(sql, val)
    
    except:
        print( "Valor incorrecto de CREATED_BY")
        print( "jajaja")
        
    else:
        conexion.commit()
        print(insertar.rowcount, "registro insertado")


def accion3():
    print('Contenido de la tabla panelpersons')
    insertar.execute("SELECT * FROM panelpersons")
    resultado = insertar.fetchall()
    for x in resultado:
        print(x)

    print("")
    print('Contenido de la tabla panelinventory')
    insertar.execute("SELECT * FROM panelinventory")
    resultado = insertar.fetchall()
    for x in resultado:
        print(x)
        
def accion4():
    print('Eliminar una fila de la tabla panelpersons')
    fila = input('Escriba el numero de PERSON_ID a eliminar ')
    
    sql = "DELETE FROM panelpersons WHERE PERSON_ID = %s"
    val = (int(fila))

    insertar.execute(sql, (val,))

    conexion.commit()

    print(insertar.rowcount, "registro borrado")

def accion5():
    print('Eliminar una fila de la tabla panelinventory')
    fila = input('Escriba el numero de ITEM_ID a eliminar ')
    
    sql = "DELETE FROM panelinventory WHERE ITEM_ID = %s"
    val = (int(fila))

    insertar.execute(sql, (val,))

    conexion.commit()

    print(insertar.rowcount, "registro borrado")


def salir():
    print('Ha finalizado el proceso')


if __name__ == '__main__':
    menu_principal()
