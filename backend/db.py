import pymysql

# Función para conectar a MySQL
def connect_db():
    return pymysql.connect(
        host="localhost",   
        user="root",        
        password="12345",        
        database="userdb",  
        cursorclass=pymysql.cursors.DictCursor  
    )
