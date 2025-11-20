from flask import Blueprint, render_template
from conexion import get_connection

inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route('/inicio-usuario')
def inicio():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Estadísticas generales
    cursor.execute("""
        SELECT 
            COUNT(*) AS total_especies,
            COUNT(CASE WHEN tipo = 1 THEN 1 END) AS flora,
            COUNT(CASE WHEN tipo = 2 THEN 1 END) AS fauna,
            COUNT(CASE WHEN id_estado_conservacion IN (3,4,5) THEN 1 END) AS vulnerables
        FROM especies
    """)
    stats = cursor.fetchone()

    # Especies con fotografía
    cursor.execute("SELECT COUNT(DISTINCT id_especie) AS fotografiadas FROM fotografia")
    fotos = cursor.fetchone()

    conn.close()

    return render_template('inicio_usuario.html', stats=stats, fotos=fotos)
