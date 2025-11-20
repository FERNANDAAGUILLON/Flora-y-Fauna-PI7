from flask import Blueprint, render_template, request, redirect, url_for
from conexion import get_connection

zonas_admi = Blueprint('zonas_admi', __name__, url_prefix='/especies')

def obtener_zonas():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT ID, nombre_region FROM zonas")
    zonas = cursor.fetchall()
    cursor.close()
    db.close()
    return zonas

def obtener_familias():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT ID, nombre_familia FROM familia")
    familias = cursor.fetchall()
    cursor.close()
    db.close()
    return familias

def obtener_estados_conservacion():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT ID, categoria FROM estado_conservacion")
    estados = cursor.fetchall()
    cursor.close()
    db.close()
    return estados

@zonas_admi.route('/', methods=['GET', 'POST'])
def mostrar_especies_admin():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    zonas = obtener_zonas()
    familias = obtener_familias()
    estados_conservacion = obtener_estados_conservacion()
    zona_id = request.form.get('zona') if request.method == 'POST' else '3'

    cursor.execute("""
        SELECT 
            e.ID,
            e.Nombre_comun, 
            e.nombre_cientifico, 
            f.nombre_familia, 
            ec.categoria, 
            z.nombre_region
        FROM especies e
        JOIN familia f ON e.id_familia = f.ID
        JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
        JOIN zonas z ON e.id_zonas = z.ID
        WHERE z.ID = %s
    """, (zona_id,))
    especies = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template("especiesAdmin.html", especies=especies, zonas=zonas, zona_actual=zona_id,
                           familias=familias, estados_conservacion=estados_conservacion)

@zonas_admi.route('/agregar', methods=['POST'])
def agregar_especie():
    db = get_connection()
    cursor = db.cursor()
    nombre_comun = request.form['nombre_comun']
    nombre_cientifico = request.form['nombre_cientifico']
    id_familia = request.form['id_familia']
    id_estado_conservacion = request.form['id_estado_conservacion']
    id_zonas = request.form['zona']

    cursor.execute("""
        INSERT INTO especies (Nombre_comun, nombre_cientifico, id_familia, id_estado_conservacion, id_zonas)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre_comun, nombre_cientifico, id_familia, id_estado_conservacion, id_zonas))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('zonas_admi.mostrar_especies_admin'))

@zonas_admi.route('/eliminar/<int:id>')
def eliminar_especie(id):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM especies WHERE ID = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('zonas_admi.mostrar_especies_admin'))

@zonas_admi.route('/editar/<int:id>')
def editar_especie(id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    # Obtener especie
    cursor.execute("SELECT * FROM Especies WHERE ID = %s", (id,))
    especie = cursor.fetchone()

    # Obtener zonas
    zonas = obtener_zonas()

    # Obtener familias (tabla se llama 'Familia', no 'familias')
    cursor.execute("SELECT * FROM Familia")
    familias = cursor.fetchall()

    # Obtener estados de conservación (tabla se llama 'Estado_Conservacion')
    cursor.execute("SELECT * FROM Estado_Conservacion")
    estados_conservacion = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        'editar_especie.html',
        especie=especie,
        zonas=zonas,
        familias=familias,
        estados_conservacion=estados_conservacion
    )



@zonas_admi.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_especie(id):
    db = get_connection()
    cursor = db.cursor()
    nombre_comun = request.form['nombre_comun']
    nombre_cientifico = request.form['nombre_cientifico']
    id_familia = request.form['id_familia']
    id_estado_conservacion = request.form['id_estado_conservacion']
    id_zonas = request.form['zona']

    cursor.execute("""
        UPDATE especies 
        SET Nombre_comun=%s, nombre_cientifico=%s, id_familia=%s, id_estado_conservacion=%s, id_zonas=%s
        WHERE ID=%s
    """, (nombre_comun, nombre_cientifico, id_familia, id_estado_conservacion, id_zonas, id))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('zonas_admi.mostrar_especies_admin'))
