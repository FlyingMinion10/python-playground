import sqlite3
import json

# Connect to a database (or create one if it doesn't exist)
def connect():
    conn = sqlite3.connect('keyCards.db')
    cursor = conn.cursor()
    return cursor

# Create a table
# cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users
#                (id INTEGER PRIMARY KEY, 
#                name TEXT, 
#                userNumber INTEGER, 
#                token TEXT)''')

# Insert a row of data
def insertUser(name, userNumber, token):
    # Asegúrate de que la ruta a tu base de datos es correcta
    conn = sqlite3.connect('ruta/a/tu/base_de_datos.db')
    cursor = conn.cursor()
    
    # Intenta ejecutar tu operación
    token = json.dumps(token)
    try:
        cursor.execute(f"INSERT INTO users (name, userNumber, token) VALUES (?, ?, ?)", (name, userNumber, token))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar el usuario: {e}")
    finally:
        # Asegúrate de cerrar la conexión al final
        conn.close()

# Save (commit) the changes

# Query the database
def checkToken(userNumber, passKey):
    
    # Establecer coneccion
    conn = sqlite3.connect('ruta/a/tu/base_de_datos.db')
    cursor = conn.cursor()

    # Intenta ejecutar tu operación
    try:
        cursor.execute("SELECT token FROM users WHERE userNumber = ?", (userNumber))
        data = cursor.fetchall()
        retrieved_list = json.loads(data[0])
        print(retrieved_list)
        # for key in retrieved_list:
        #     if key[0] == passKey:
        #         print("Llave correcta")
        #         cursor.execute("UPDATE FROM users WHERE userNumber = ? AND token[0]", (userNumber))
        #         return True
        #     else:
        #         return False
    except sqlite3.Error as e:
        print(f"Error al insertar el usuario: {e}")
    finally:
        # Asegúrate de cerrar la conexión al final
        conn.close()
    

