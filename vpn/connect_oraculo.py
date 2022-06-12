import time
import mysql.connector
import csv
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
            with open(r'/output/output.csv', 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames = ['clientes', 'url_producao'])
                for (clientes, url_producao) in cursor:
                    writer.writerow({'clientes':clientes, 'url_producao': url_producao})
                    print(clientes, url_producao)
                
            return
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
    # df.to_csv('out.csv', index=False)
