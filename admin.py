from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from conexion import get_connection


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.before_request
def verificar_admin():
    if session.get('rol') != 'admin':
        flash("Acceso restringido solo para administradoras", "danger")
        return redirect(url_for('auth.login'))

@admin.route('/')
def panel_admin():
    return render_template('admiPanel.html')

@admin.route('/usuarios')
def ver_usuarios():
    from conexion import get_connection
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, apellidoPaterno, apellidoMaternousuarios, correo, rol FROM Usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()

    return render_template('usuarios.html', usuarios=usuarios)


@admin.route('/usuarios/eliminar/<int:usuario_id>')
def eliminar_usuario(usuario_id):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id = %s", (usuario_id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    flash("Usuario eliminado correctamente.")
    return redirect(url_for('admin.ver_usuarios'))



@admin.route('/usuarios/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar_rol(usuario_id):
    conexion = get_connection()
    cursor = conexion.cursor()

    if request.method == 'POST':
        nuevo_rol = request.form['rol']
        cursor.execute("UPDATE Usuarios SET rol = %s WHERE id = %s", (nuevo_rol, usuario_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        flash("Rol actualizado correctamente.")
        return redirect(url_for('admin.ver_usuarios'))

    cursor.execute("SELECT id, nombre, correo, rol FROM Usuarios WHERE id = %s", (usuario_id,))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return render_template('editar_rol.html', usuario=usuario)

