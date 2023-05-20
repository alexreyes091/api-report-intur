import psycopg2
from os import getcwd
from fastapi.responses import FileResponse
from connections.conx import connection

cursor = connection()

def getRequestDocument(id, requestId):
    try:
        cursor.execute('SELECT * FROM "RequestAttach" where "requestId" = ' + str(requestId) + 'and "id" =' + str(id) + ';')
        file_data = cursor.fetchone()
        file_name = file_data[2]

        with open('tmp/' + str(requestId) + str(id) + '_' + file_name, 'wb') as file:
            file.write(file_data[4])
        
        return FileResponse(getcwd() + '/tmp/' + str(requestId) + str(id) + '_' + file_name)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return { 'ERROR': 'Error al obtener el documento, verificar la URL' }