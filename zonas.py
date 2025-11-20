from flask import Flask, render_template
from conexion import get_connection
from auth import auth
from admin import admin
from zonasAdmi import zonas_admi
from perfil import perfil_bp
from inicio import inicio_bp
from comentarios import comentarios_bp
from consejos_controller import consejos_bp
from admin_comentarios import admin_comentarios_bp
from admin_consejos import admin_consejos_bp

app = Flask(__name__)

app.secret_key = 'floraYfauna123'
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(zonas_admi)
app.register_blueprint(perfil_bp)
app.register_blueprint(inicio_bp)
app.register_blueprint(comentarios_bp)
app.register_blueprint(consejos_bp)
app.register_blueprint(admin_comentarios_bp)
app.register_blueprint(admin_consejos_bp)


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/inicio-usuario')
def inicio():
    return render_template('inicio_usuario.html')

@app.route('/adminpanel')
def panel_admin():
    return render_template('admiPanel.html')


@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/mapa-usuario')
def mapa2():
    return render_template('mapa2.html')

@app.route('/login-inicial')
def mostrar_login():
    return render_template('login.html')

@app.route("/zona1")
def ZONA1():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 3
    GROUP BY e.ID;

    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA1.html", especies=especies)


@app.route("/zona2")
def ZONA2():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 1
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA2.html", especies=especies)

@app.route("/zona3")
def ZONA3():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 2
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA3.html", especies=especies)

@app.route("/zona4")
def ZONA4():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 4
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA4.html", especies=especies)

@app.route("/zona5")
def ZONA5():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 5
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA5.html", especies=especies)

@app.route("/zona6")
def ZONA6():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 6
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA6.html", especies=especies)

@app.route("/zona7")
def ZONA7():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 7
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA7.html", especies=especies)

@app.route("/zona8")
def ZONA8():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 8
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA8.html", especies=especies)

@app.route("/zona9")
def ZONA9():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 10
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA9.html", especies=especies)

@app.route("/zona10")
def ZONA10():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 9
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA10.html", especies=especies)


@app.route("/zona11")
def ZONA11():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 11
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA11.html", especies=especies)

@app.route("/zona12")
def ZONA12():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 12
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA12.html", especies=especies)

@app.route("/zona13")
def ZONA13():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 13
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA13.html", especies=especies)

@app.route("/zona14")
def ZONA14():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 14
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA14.html", especies=especies)

@app.route("/zona15")
def ZONA15():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 15
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA15.html", especies=especies)


@app.route("/zona16")
def ZONA16():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 16
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA16.html", especies=especies)

@app.route("/zona17")
def ZONA17():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 17
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA17.html", especies=especies)

@app.route("/zona18")
def ZONA18():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
    e.Nombre_comun, 
    e.nombre_cientifico, 
    f.nombre_familia, 
    ec.categoria, 
    z.nombre_region,
    MIN(ft.url_imagen) as imagen
    FROM especies e
    JOIN familia f ON e.id_familia = f.ID
    JOIN estado_conservacion ec ON e.id_estado_conservacion = ec.ID
    JOIN zonas z ON e.id_zonas = z.ID
    LEFT JOIN fotografia ft ON ft.id_especie = e.ID
    WHERE z.ID = 18
    GROUP BY e.ID;
    """
    cursor.execute(query)
    especies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("ZONA18.html", especies=especies)

if __name__ == '__main__':
    app.run(debug=True)
