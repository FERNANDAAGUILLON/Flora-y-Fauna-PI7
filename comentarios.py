from flask import Blueprint, render_template, request, redirect, session, jsonify
from conexion import get_connection
from datetime import date

comentarios_bp = Blueprint('comentarios_bp', __name__)

@comentarios_bp.route('/comentarios', methods=['GET', 'POST'])
def comentarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    id_usuario = session.get('id_usuario')

    if request.method == 'POST':
        if not id_usuario:
            return "Debes iniciar sesión para comentar", 403

        contenido = request.form['contenido']
        id_zona = request.form['id_zona']
        hoy = date.today()

        cursor.execute("""
            INSERT INTO Comentario (Contenido, Fecha_publicacion, ID_usuario, ID_zona, ID_estatus)
            VALUES (%s, %s, %s, %s, 1)
        """, (contenido, hoy, id_usuario, id_zona))
        conn.commit()
        return redirect('/comentarios')

    # Obtener comentarios activos
    cursor.execute("""
        SELECT c.ID, c.Contenido, c.Fecha_publicacion,
               CONCAT(u.nombre, ' ', u.apellidoPaterno, ' ', u.apellidoMaternousuarios) AS nombre,
               z.nombre_region,
               c.ID_usuario,
               (SELECT COUNT(*) FROM Likes WHERE id_comentario = c.ID) AS likes
        FROM Comentario c
        JOIN Usuarios u ON u.id = c.ID_usuario
        JOIN Zonas z ON z.ID = c.ID_zona
        WHERE c.ID_estatus = 1
        ORDER BY c.Fecha_publicacion DESC
    """)
    comentarios = cursor.fetchall()

    # Obtener zonas para el formulario
    cursor.execute("SELECT ID, nombre_region FROM Zonas")
    zonas = cursor.fetchall()

    return render_template('comentarios.html', comentarios=comentarios, zonas=zonas, id_usuario=id_usuario)

# Eliminar comentario solo si es del usuario actual
@comentarios_bp.route('/comentario/eliminar/<int:id>', methods=['POST'])
def eliminar_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        return "No autenticado", 403

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT ID_usuario FROM Comentario WHERE ID = %s", (id,))
    comentario = cursor.fetchone()

    if not comentario:
        return "Comentario no encontrado", 404

    if comentario['ID_usuario'] != id_usuario:
        return "No tienes permiso para eliminar este comentario", 403

    cursor.execute("DELETE FROM Comentario WHERE ID = %s", (id,))
    conn.commit()
    return redirect('/comentarios')

# Editar comentario solo si es del usuario actual
@comentarios_bp.route('/comentario/editar/<int:id>', methods=['POST'])
def editar_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        return "No autenticado", 403

    nuevo_contenido = request.form['contenido']
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT ID_usuario FROM Comentario WHERE ID = %s", (id,))
    comentario = cursor.fetchone()

    if not comentario:
        return "Comentario no encontrado", 404

    if comentario['ID_usuario'] != id_usuario:
        return "No tienes permiso para editar este comentario", 403

    cursor.execute("UPDATE Comentario SET Contenido = %s WHERE ID = %s", (nuevo_contenido, id))
    conn.commit()
    return redirect('/comentarios')

# Like solo si el usuario esta autenticado y no ha dado like antes
@comentarios_bp.route('/comentario/like/<int:id>', methods=['POST'])
def like_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        return jsonify({'success': False, 'error': 'No autenticado'}), 403

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Likes WHERE id_comentario = %s AND id_usuario = %s", (id, id_usuario))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Likes (id_comentario, id_usuario) VALUES (%s, %s)", (id, id_usuario))
        conn.commit()

    return jsonify({'success': True})
