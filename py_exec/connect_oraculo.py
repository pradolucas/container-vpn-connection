import mysql.connector
import pandas as pd
from mysql.connector import errorcode


def extract_oraculo():
    ORACULO_CREDENTIALS = {
        }
    try:
        conn = mysql.connector.connect(**ORACULO_CREDENTIALS)
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")

            sql_query="""
            SELECT cliente, url_producao FROM `clientes` where status = 1 AND checa_plataforma = 1 order by cliente
            """
            cursor = conn.cursor()
            cursor.execute(sql_query)
            df = pd.DataFrame(cursor, columns=cursor.column_names)
            cursor.close()
            conn.close()
            print("MySQL connection is closed\n")
            return df[["cliente", "url_producao"]] 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    

if __name__ == "__main__":
    print("CONECTANDO...\n")
    df = extract_oraculo()
    df.to_csv('output/out.csv', index=False)
