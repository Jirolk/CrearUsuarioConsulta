import mysql.connector
import logging
from dotenv import load_dotenv
import os


#def create_jasper_consulta(username, password, database, ip):
def create_jasper_consulta(username, password, ip):
    conn=None
    load_dotenv()
    host = os.getenv("DATABASE_HOST")
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    logging.basicConfig(filename='log_create_user_consulta.txt', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')     
    try:
            
       # Conexión a la base de datos MySQL
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password            
        )
        print("Conexión Exitosa")
        
        # Crear un cursor
        cursor = conn.cursor()
       
         # Crear usuario y otorgarle privilegios
        cursor.execute(f"CREATE USER '{username}'@'{ip}' IDENTIFIED BY '{password}';")
        #cursor.execute(f"GRANT SELECT ON {database}.* TO '{username}'@'{ip}';")
        cursor.execute(f"GRANT SELECT ON *.* TO '{username}'@'{ip}';")
        cursor.execute("FLUSH PRIVILEGES;")
        
        # # Confirmar los cambios
        conn.commit()

        # logging.info(f"El usuario '{username}' ha sido creado y tiene permisos de consulta en la base de datos '{database}'.")
        # print(f"El usuario '{username}' ha sido creado y tiene permisos de consulta en la base de datos '{database}' y con la ip {ip}.")

        logging.info(f"El usuario '{username}' ha sido creado y tiene permisos de consulta en la base de datos.")
        
        print(f"El usuario '{username}' ha sido creado y tiene permisos de consulta en la base de datos y con la ip {ip}.")
    
    except mysql.connector.Error as error:        
        print("Error al conectar a la base de datos:", error)    
        logging.error(f"Error con base de datos: {error}")

    finally:
        # Cerrar la conexión
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión a la base de datos cerrada.")


#create_jasper_consulta("jasper", "RzB*n2T*2044", "dev_api_backend_fe", "172.30.%.%")

create_jasper_consulta("jasper", "RzB*n2T*2044", "172.30.%.%")
