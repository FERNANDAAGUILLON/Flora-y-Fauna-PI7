from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from conexion import get_connection

auth = Blueprint('auth', __name__)

@auth.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.")
    return redirect(url_for('auth.inicio_usuario'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contraseña']

        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE correo = %s AND contrasena = %s", (correo, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()

        if usuario:
            session['id_usuario'] = usuario['id']
            session['usuario'] = usuario['correo']            # Correo del usuario
            rol = usuario['rol'].strip().lower()              # Rol del usuario
            session['rol'] = rol

            flash("Inicio de sesión exitoso")
            print("Rol que llegó:", rol)

            if rol == 'admin':
                return redirect(url_for('admin.panel_admin'))
            else:
                return redirect(url_for('auth.inicio_usuario'))

        else:
            flash("Correo o contraseña incorrectos")
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        correo = request.form['correo']
        contrasena = request.form['contraseña']

        conexion = get_connection()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Usuarios (nombre, apellidoPaterno, apellidoMaternousuarios, correo, contrasena, rol) VALUES (%s, %s, %s, %s, %s, %s)

        """

    
        valores = (nombre, ap_paterno, ap_materno, correo, contrasena, 'usuario')
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

        flash("Registro exitoso. Ya puedes iniciar sesión.")
        return redirect(url_for('auth.login'))

    return render_template('registro.html')

@auth.route('/inicio_usuario')
def inicio_usuario():
    if 'usuario' not in session or session.get('rol') != 'usuario':
        flash("Acceso no autorizado.")
        return redirect(url_for('auth.login'))

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            COUNT(*) AS total_especies,
            COUNT(CASE WHEN tipo = 1 THEN 1 END) AS flora,
            COUNT(CASE WHEN tipo = 2 THEN 1 END) AS fauna,
            COUNT(CASE WHEN id_estado_conservacion IN (3,4,5) THEN 1 END) AS vulnerables
        FROM especies
    """)
    stats = cursor.fetchone()

    cursor.execute("SELECT COUNT(DISTINCT id_especie) AS fotografiadas FROM fotografia")
    fotos = cursor.fetchone()

    cursor.close()
    conexion.close()

    imagenes_zonas = [
        {'nombre': 'Jalpan de Serra', 'ruta': 'imagenes_zonas/jalpan.jpg'},
        {'nombre': 'Landa de Matamoros', 'ruta': 'imagenes_zonas/landa.jpg'},
        {'nombre': 'Pinal de Amoles', 'ruta': 'imagenes_zonas/pinal.jpg'},
        {'nombre': 'San Joaquín', 'ruta': 'imagenes_zonas/sanjoaquin.jpg'},
        {'nombre': 'Peñamiller', 'ruta': 'imagenes_zonas/penamiller.jpg'},
        {'nombre': 'Cadereyta de Montes', 'ruta': 'imagenes_zonas/cadereyta.png'},
        {'nombre': 'Amealco de Bonfil', 'ruta': 'imagenes_zonas/amealco.jpg'}
    ]

    return render_template('inicio_usuario.html', stats=stats, fotos=fotos, zonas=imagenes_zonas)
