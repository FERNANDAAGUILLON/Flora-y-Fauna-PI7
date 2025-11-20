from flask import Blueprint, render_template, request, redirect, session
from conexion import get_connection

admin_comentarios_bp = Blueprint('admin_comentarios_bp', __name__)

@admin_comentarios_bp.route('/admin/comentarios')
def ver_comentarios_admin():
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    zona_id = request.args.get('zona', type=int)
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.ID, c.Contenido, c.Fecha_publicacion,
               CONCAT(u.nombre, ' ', u.apellidoPaterno, ' ', u.apellidoMaternousuarios) AS nombre,
               z.ID AS zona_id, z.nombre_region
        FROM Comentario c
        JOIN Usuarios u ON u.id = c.ID_usuario
        JOIN Zonas z ON z.ID = c.ID_zona
    """
    params = []
    if zona_id:
        query += " WHERE z.ID = %s"
        params.append(zona_id)

    query += " ORDER BY c.Fecha_publicacion DESC"
    cursor.execute(query, params)
    comentarios = cursor.fetchall()

    cursor.execute("SELECT ID, nombre_region FROM Zonas ORDER BY nombre_region")
    zonas = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('admin_comentarios.html', comentarios=comentarios, zonas=zonas, zona_seleccionada=zona_id)

@admin_comentarios_bp.route('/admin/comentario/eliminar/<int:id>', methods=['POST'])
def eliminar_comentario_admin(id):
    if session.get('rol') != 'admin':
        return "Acceso denegado", 403

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Comentario WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin/comentarios')
