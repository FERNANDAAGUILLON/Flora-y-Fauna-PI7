from flask import Blueprint, render_template, request, redirect, session
from conexion import get_connection

admin_consejos_bp = Blueprint('admin_consejos_bp', __name__)

@admin_consejos_bp.route('/admin/consejos')
def listar_consejos():
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT c.id, c.titulo, c.consejo, c.fecha, c.hora, z.ID AS zona_id, z.nombre_region
        FROM consejos c
        JOIN zonas z ON c.zona = z.ID
        ORDER BY c.fecha DESC, c.hora DESC
    """)
    consejos = cursor.fetchall()

    cursor.execute("SELECT ID, nombre_region FROM zonas ORDER BY nombre_region")
    zonas = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("admin_consejos.html", consejos=consejos, zonas=zonas)

@admin_consejos_bp.route('/admin/consejo/crear', methods=['POST'])
def crear_consejo():
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    titulo = request.form['titulo']
    consejo = request.form['consejo']
    fecha = request.form['fecha']
    hora = request.form['hora']
    zona = request.form['zona']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO consejos (titulo, consejo, fecha, hora, zona)
        VALUES (%s, %s, %s, %s, %s)
    """, (titulo, consejo, fecha, hora, zona))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/admin/consejos')

@admin_consejos_bp.route('/admin/consejo/editar/<int:id>', methods=['POST'])
def editar_consejo(id):
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    titulo = request.form['titulo']
    consejo = request.form['consejo']
    fecha = request.form['fecha']
    hora = request.form['hora']
    zona = request.form['zona']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE consejos SET titulo=%s, consejo=%s, fecha=%s, hora=%s, zona=%s
        WHERE id=%s
    """, (titulo, consejo, fecha, hora, zona, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/admin/consejos')

@admin_consejos_bp.route('/admin/consejo/eliminar/<int:id>', methods=['POST'])
def eliminar_consejo(id):
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM consejos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/admin/consejos')
