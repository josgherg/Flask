from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)
CORS(app)

######Estos son los métodos para la tabla autores (1)#######
@app.route('/libreria/autor/crear_autor', methods=['POST'])
def agregarAutor():
    nombreAutor = request.json['nombreAutor']       
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO autores (nombreAutores) VALUES(%s)', (nombreAutor,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Autor agregado exitosamente."})

@app.route('/libreria/autor/ver', methods=['GET'])
def verAutores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores")
    columnas = [columna[0] for columna in cursor.description]
    autores = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memAutores = jsonify(autores)
    memAutores.headers.add("Acces-Control-Allow-Origin","*")
    return memAutores

@app.route('/libreria/autor/ver/<id>', methods=['GET'])
def verAutor(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memAutor = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memAutor:
        return jsonify(memAutor)
    else:
        return jsonify({"resultado":"El autor no fue encontrado."}), 404

@app.route('/libreria/autor/eliminar/<id>', methods = ['DELETE'] )
def eliminarAutor(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from autores WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"El genero fue eliminado exitosamente."})

@app.route('/libreria/autor/editar/<id>', methods = ['PATCH'] )
def actualizarAutor(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE autores SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["nombreAutores"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data) )
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado el autor exitosamente."})




######Estos son los métodos para la tabla generos (2)#######
@app.route('/libreria/genero/crear_genero', methods=['POST'])
def agregarGenero():
    nombreGenero = request.json['nombreGenero']      
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO generos (nombreGeneros) VALUES(%s)', (nombreGenero,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({'mensaje':'Género agregado exitosamente'})

@app.route('/libreria/genero/ver', methods=['GET'])
def verGeneros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos")
    columnas = [columna[0] for columna in cursor.description]
    generos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memGeneros = jsonify(generos)
    memGeneros.headers.add("Acces-Control-Allow-Origin","*")
    return memGeneros

@app.route('/libreria/genero/ver/<id>', methods=['GET'])
def verGenero(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memAutor = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memAutor:
        return jsonify(memAutor)
    else:
        return jsonify({"resultado":"El género no fue encontrado."}), 404

@app.route('/libreria/genero/eliminar/<id>', methods = ['DELETE'] )
def eliminarGenero(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from generos WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"El género fue eliminado exitosamente."})

@app.route('/libreria/genero/editar/<id>', methods = ['PATCH'] )
def actualizarGenero(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE generos SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["nombreGeneros"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado el género exitosamente."})



######Estos son los métodos para la tabla editoriales (3)#######
@app.route('/libreria/editorial/crear_editorial', methods=['POST'])
def agregarEditorial():
    nombreEditoriales = request.json['nombreEditoriales']       
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO editoriales (nombreEditoriales) VALUES(%s)', (nombreEditoriales,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Editorial agregada exitosamente"})

@app.route('/libreria/editorial/ver', methods=['GET'])
def verEditoriales():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales")
    columnas = [columna[0] for columna in cursor.description]
    editoriales = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memEditoriales = jsonify(editoriales)
    memEditoriales.headers.add("Acces-Control-Allow-Origin","*")

    return memEditoriales

@app.route('/libreria/editorial/ver/<id>', methods=['GET'])
def verEditorial(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memEditorial = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memEditorial:
        return jsonify(memEditorial)
    else:
        return jsonify({"resultado":"La editorial no fue encontrada."}), 404

@app.route('/libreria/editorial/eliminar/<id>', methods = ['DELETE'] )
def eliminarEditorial(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from editoriales WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"La editorial fue eliminada exitosamente."})

@app.route('/libreria/editorial/editar/<id>', methods = ['PATCH'] )
def actualizarEditorial(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE editoriales SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["nombreEditoriales"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado la editorial exitosamente."})




######Estos son los métodos para la tabla libros (4)#######
@app.route('/libreria/libro/crear_libro', methods=['POST'])
def agregarLibro():
    titulo = request.json['titulo']
    anoPublicacion = request.json['anoPublicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO libros (titulo, anoPublicacion, autor_id, genero_id, editorial_id) VALUES(%s, %s, %s, %s, %s)', (titulo, anoPublicacion, autor_id, genero_id, editorial_id))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({'mensaje':'Libro agregado exitosamente.'})

@app.route('/libreria/libro/ver', methods=['GET'])
def verLibros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros")
    columnas = [columna[0] for columna in cursor.description]
    libros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memLibros = jsonify(libros)
    memLibros.headers.add("Acces-Control-Allow-Origin","*")

    return memLibros

@app.route('/libreria/libro/ver/<id>', methods=['GET'])
def verLibro(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memLibros = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memLibros:
        return jsonify(memLibros)
    else:
        return jsonify({"resultado":"El Libro no fue encontrado."}), 404

@app.route('/libreria/libro/eliminar/<id>', methods = ['DELETE'] )
def eliminarLibro(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from libros WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"El libro fue eliminado exitosamente."})

@app.route('/libreria/libro/editar/<id>', methods = ['PATCH'] )
def actualizarLibro(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE libros SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["titulo", "anoPublicacion", "autor_id", "genero_id", "editorial_id"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado el libro exitosamente."})



######Estos son los métodos para la tabla Resena (5)#######
@app.route('/libreria/resena/crear_resena', methods=['POST'])
def agregarResena():
    contenido = request.json['contenido']
    libro_id  = request.json['libro_id']
    usuario_id  = request.json['usuario_id']
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO resenas (contenido, libro_id, usuario_id) VALUES(%s, %s, %s)', (contenido, libro_id, usuario_id))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({'mensaje':'Reseña agregada exitosamente.'})

@app.route('/libreria/resena/ver', methods=['GET'])
def verResenas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM resenas")
    columnas = [columna[0] for columna in cursor.description]
    resenas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memResenas = jsonify(resenas)
    memResenas.headers.add("Acces-Control-Allow-Origin","*")

    return memResenas

@app.route('/libreria/resena/ver/<id>', methods=['GET'])
def verResena(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM resenas WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memResena = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memResena:
        return jsonify(memResena)
    else:
        return jsonify({"resultado":"La reeseña no fue encontrada."}), 404

@app.route('/libreria/resena/eliminar/<id>', methods = ['DELETE'] )
def eliminarResena(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from resenas WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"La reseña fue eliminada exitosamente."})

@app.route('/libreria/resena/editar/<id>', methods = ['PATCH'] )
def actualizarResena(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE resenas SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["contenido"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado la reseña exitosamente."})

######Estos son los métodos para la tabla usuarios (6)#######
@app.route('/libreria/usuario/crear_usuario', methods=['POST'])
def agregarUsuarios():
    nombre = request.json['nombre']       
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO usuarios (nombre) VALUES(%s)', (nombre,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Usuario agregado exitosamente."})

@app.route('/libreria/usuario/ver', methods=['GET'])
def verUsuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    columnas = [columna[0] for columna in cursor.description]
    usuarios = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memUsuarios = jsonify(usuarios)
    memUsuarios.headers.add("Acces-Control-Allow-Origin","*")
    return memUsuarios

@app.route('/libreria/usuario/ver/<id>', methods=['GET'])
def verUsuario(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    memUsuario = dict(zip(columnas, cursor.fetchone())) 
    
    cursor.close()
    if memUsuario:
        return jsonify(memUsuario)
    else:
        return jsonify({"resultado":"El usuario no fue encontrado."}), 404

@app.route('/libreria/usuario/eliminar/<id>', methods = ['DELETE'] )
def eliminarUsuario(id):
    cursor = mysql.connection.cursor()    
    cursor.execute("DELETE from usuarios WHERE id= %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"Resultado":"El usuario fue eliminado exitosamente."})

@app.route('/libreria/usuario/editar/<id>', methods = ['PATCH'] )
def actualizarUsuario(id):
    datos = request.json
    if not datos:
        return jsonify({'Error':"No se enviaron los datos a actualizar."})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE usuarios SET "
    update_data = []
    for campo, valor in datos.items():
        if campo in["nombre"]:
            update_query += f'{campo} = %s, '
            update_data.append(valor)
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios."})

    update_query = update_query.rstrip(", ")    
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit() 
    cursor.close()
    return jsonify({"mensaje":"Se ha editado el usuario exitosamente."})

######Copnsulta Especial#########
@app.route('/libreria/ver/info', methods=['GET'])
def verInfoLibro():
    cursor = mysql.connection.cursor()
    command= "SELECT libros.id, libros.titulo, autores.nombreAutores, generos.nombreGeneros, resenas.contenido, usuarios.nombre\n"
    command +="FROM libros\n"
    command +="LEFT JOIN autores ON libros.autor_id = autores.id\n"
    command +="LEFT JOIN generos ON libros.genero_id = generos.id\n"
    command +="lEFT JOIN resenas ON libros.id = resenas.libro_id\n"
    command +="LEFT JOIN usuarios ON resenas.usuario_id = usuarios.id\n"
    cursor.execute(command)
    columnas = [columna[0] for columna in cursor.description]
    infoLibros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    memInfoLibros = jsonify(infoLibros)
    memInfoLibros.headers.add("Acces-Control-Allow-Origin","*")
    return memInfoLibros

if __name__ == '__main__':
    app.run(debug=True, port=7500)