import psycopg2

def connection():
    # Connect to an existing database
    try:
        conn = psycopg2.connect(database="intur_memos",
                                host="192.168.0.87",
                                user="postgres",
                                password="!Mem0s$$2021pg_u!",
                                port="5432")
        return conn.cursor()
    except:
        print("I am unable to connect to the database")