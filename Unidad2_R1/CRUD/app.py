import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Establece la conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect('R1.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para obtener todos los registros de la tabla peliculas
@app.route('/peliculas', methods=['GET'])
def get_peliculas():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM peliculas')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método GET para obtener todos los registros de la tabla actores
@app.route('/actores', methods=['GET'])
def get_actores():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM actores')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT para crear un registro en la tabla peliculas
@app.route('/peliculas', methods=['PUT'])
def create_pelicula():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO peliculas (codigo, titulo, genero, director, fecha_estreno, duracion, presupuesto, ingresos, sinopsis, fecha_estreno_pais) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['codigo'], record['titulo'], record['genero'], record['director'], record['fecha_estreno'], record['duracion'], record['presupuesto'], record['ingresos'], record['sinopsis'], record['fecha_estreno_pais']))
    conn.commit()
    return jsonify(record)

# Método PUT para crear un registro en la tabla actores
@app.route('/actores', methods=['PUT'])
def create_actor():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO actores (id_actor, nombre, apellido, fecha_nacimiento, pais_nacimiento, papel, premios) VALUES (?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['id_actor'], record['nombre'], record['apellido'], record['fecha_nacimiento'], record['pais_nacimiento'], record['papel'], record['premios']))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla peliculas
@app.route('/peliculas', methods=['DELETE'])
def delete_pelicula():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM peliculas WHERE codigo = ?'
    cursor.execute(delete, (record['codigo'],))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla actores
@app.route('/actores', methods=['DELETE'])
def delete_actor():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM actores WHERE id_actor = ?'
    cursor.execute(delete, (record['id_actor'],))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla peliculas
@app.route('/peliculas', methods=['POST'])
def update_pelicula():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE peliculas SET titulo = ?, genero = ?, director = ?, fecha_estreno = ?, duracion = ?, presupuesto = ?, ingresos = ?, sinopsis = ?, fecha_estreno_pais = ? WHERE codigo = ?'
    cursor.execute(update, (record['titulo'], record['genero'], record['director'], record['fecha_estreno'], record['duracion'], record['presupuesto'], record['ingresos'], record['sinopsis'], record['fecha_estreno_pais'], record['codigo']))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla actores
@app.route('/actores', methods=['POST'])
def update_actor():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE actores SET nombre = ?, apellido = ?, fecha_nacimiento = ?, pais_nacimiento = ?, papel = ?, premios = ? WHERE id_actor = ?'
    cursor.execute(update, (record['nombre'], record['apellido'], record['fecha_nacimiento'], record['pais_nacimiento'], record['papel'], record['premios'], record['id_actor']))
    conn.commit()
    return jsonify(record)

# Inicia el servicio
if __name__ == '__main__':
    app.run(debug=True)
