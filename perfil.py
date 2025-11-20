from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from conexion import get_connection

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/perfil')
def perfil():
    if 'id_usuario' not in session:
        return redirect(url_for('auth.login'))

    id_usuario = session['id_usuario']
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT nombre, apellidoPaterno, apellidoMaternousuarios, correo
        FROM Usuarios
        WHERE id = %s
    """, (id_usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    if usuario:
        return render_template('perfil.html', usuario=usuario)
    else:
        flash("Usuario no encontrado.")
        return redirect(url_for('index'))

@perfil_bp.route('/actualizar-perfil', methods=['POST'])
def actualizar_perfil():
    if 'id_usuario' not in session:
        return redirect(url_for('auth.login'))

    id_usuario = session['id_usuario']
    nombre = request.form['nombre']
    apellido_paterno = request.form['apellido_paterno']
    apellido_maternousuarios = request.form['apellido_materno']  # nombre del input en el HTML
    correo = request.form['correo']
    contrasena = request.form['contrasena']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Usuarios 
        SET nombre=%s, apellidoPaterno=%s, apellidoMaternousuarios=%s, correo=%s, contrasena=%s
        WHERE id=%s
    """, (nombre, apellido_paterno, apellido_maternousuarios, correo, contrasena, id_usuario))

    conn.commit()
    cursor.close()
    conn.close()

    flash('Perfil actualizado correctamente.')
    return redirect(url_for('perfil.perfil'))
