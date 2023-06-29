import mysql.connector

def create_jasper_user(username, password, database):
    try:
        # Conexión a la base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="nombre_basedatos"
        )
        
        # Crear un cursor
        cursor = conn.cursor()
        
        # Crear usuario y otorgarle privilegios
        cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
        cursor.execute(f"GRANT SELECT ON {database}.* TO '{username}'@'localhost';")
        cursor.execute("FLUSH PRIVILEGES;")
        
        # Confirmar los cambios
        conn.commit()
        
        print(f"El usuario '{username}' ha sido creado y tiene permisos de consulta en la base de datos '{database}'.")
    
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos MySQL:", error)
    
    finally:
        # Cerrar la conexión
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión a la base de datos MySQL cerrada.")

# Ejemplo de uso
create_jasper_user("jasper_user", "jasper_password", "nombre_basedatos")
