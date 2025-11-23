from flask import Blueprint, render_template, request, redirect, session, jsonify, flash
from conexion import get_connection
from datetime import date

comentarios_bp = Blueprint('comentarios_bp', __name__)
@comentarios_bp.route('/comentarios', methods=['GET', 'POST'])
def comentarios():
    id_usuario = session.get('id_usuario')
    
    if not id_usuario:
        flash('Debes iniciar sesión para acceder a la comunidad.', 'error')
        return redirect('/login') 

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        contenido = request.form['contenido']
        id_zona = request.form['id_zona']
        hoy = date.today()

        if not contenido or not id_zona:
            flash('Por favor completa todos los campos.', 'error')
            return redirect('/comentarios')

        try:
            cursor.execute("""
                INSERT INTO Comentario (Contenido, Fecha_publicacion, ID_usuario, ID_zona, ID_estatus)
                VALUES (%s, %s, %s, %s, 1)
            """, (contenido, hoy, id_usuario, id_zona))
            conn.commit()
            flash('¡Tu aporte ha sido publicado correctamente!', 'success')
        except Exception as e:
            conn.rollback()
            print(e)
            flash('Error al guardar el comentario.', 'error')

        conn.close()
        return redirect('/comentarios')

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

    cursor.execute("SELECT ID, nombre_region FROM Zonas")
    zonas = cursor.fetchall()
    
    conn.close()
    return render_template('comentarios.html', comentarios=comentarios, zonas=zonas, id_usuario=id_usuario)

@comentarios_bp.route('/comentario/eliminar/<int:id>', methods=['POST'])
def eliminar_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        flash('Acceso denegado.', 'error')
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT ID_usuario FROM Comentario WHERE ID = %s", (id,))
    comentario = cursor.fetchone()

    if not comentario or comentario['ID_usuario'] != id_usuario:
        flash('No tienes permiso para eliminar esto.', 'error')
        conn.close()
        return redirect('/comentarios')

    try:
        cursor.execute("DELETE FROM Likes WHERE id_comentario = %s", (id,))
        cursor.execute("DELETE FROM Comentario WHERE ID = %s", (id,))
        conn.commit()
        flash('Comentario eliminado.', 'success')
    except Exception as e:
        conn.rollback()
        flash('Error al eliminar.', 'error')
    
    conn.close()
    return redirect('/comentarios')

@comentarios_bp.route('/comentario/editar/<int:id>', methods=['POST'])
def editar_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        flash('Acceso denegado.', 'error')
        return redirect('/login')

    nuevo_contenido = request.form['contenido']
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT ID_usuario FROM Comentario WHERE ID = %s", (id,))
    comentario = cursor.fetchone()

    if not comentario or comentario['ID_usuario'] != id_usuario:
        flash('No tienes permiso para editar esto.', 'error')
        conn.close()
        return redirect('/comentarios')

    try:
        cursor.execute("UPDATE Comentario SET Contenido = %s WHERE ID = %s", (nuevo_contenido, id))
        conn.commit()
        flash('Comentario actualizado.', 'success')
    except Exception as e:
        conn.rollback()
        flash('Error al actualizar.', 'error')

    conn.close()
    return redirect('/comentarios')

@comentarios_bp.route('/comentario/like/<int:id>', methods=['POST'])
def like_comentario(id):
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        return jsonify({'success': False, 'error': 'No autenticado'}), 403

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Likes WHERE id_comentario = %s AND id_usuario = %s", (id, id_usuario))
        if cursor.fetchone():
            cursor.execute("DELETE FROM Likes WHERE id_comentario = %s AND id_usuario = %s", (id, id_usuario))
        else:
            cursor.execute("INSERT INTO Likes (id_comentario, id_usuario) VALUES (%s, %s)", (id, id_usuario))
        
        conn.commit()
        conn.close()
        return jsonify({'success': True})
        
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'success': False, 'error': str(e)}), 500