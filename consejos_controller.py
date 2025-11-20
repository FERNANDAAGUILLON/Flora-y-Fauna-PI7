from flask import Blueprint, render_template
from conexion import get_connection

consejos_bp = Blueprint('consejos_bp', __name__)


imagenes_consejos = {
    'Protección del Mirlo café': 'imgconsejos/mirlo.jpg',
    'Cuidado del Chamal': 'imgconsejos/chamal.jpg',
    'Control de residuos': 'imgconsejos/residuos.jpg',
    'Senderos responsables': 'imgconsejos/senderos.jpg',
    'Respeto a la fauna': 'imgconsejos/fauna.jpg',
    'Protección de la Tangara Azulgrís': 'imgconsejos/tangara.jpg',
    'Cuidado del Mirto coral': 'imgconsejos/mirto.jpg',
    'Arañas benéficas': 'imgconsejos/arana.jpg',
    'Reforestación responsable': 'imgconsejos/reforestacion.jpg',   
    'Guacamayas verdes': 'imgconsejos/guacamaya.jpg',
    'Hormigas chicatanas': 'imgconsejos/hormiga.jpg',
    'Alacrancillo medicinal': 'imgconsejos/alacrancillo.jpg',
    'Control de incendios': 'imgconsejos/incendios.jpg',
    'Protección de ranas': 'imgconsejos/rana.jpg',
    'Mariposas en peligro': 'imgconsejos/mariposa.jpg',
    'Álamos blancos': 'imgconsejos/alamo.jpg',
    'Turismo responsable': 'imgconsejos/turismo.jpg',
    'Chara pecho gris': 'imgconsejos/chara.jpg',
    'Carpinteros belloteros': 'imgconsejos/encino.jpeg', #checar porque no la agarra
    'Mirto chico': 'imgconsejos/mirtochico.jpg',
    'Senderismo responsable': 'imgconsejos/senderismo.jpg', 
    'Peyote protegido': 'imgconsejos/peyote.jpg',
    'Aves insectívoras': 'imgconsejos/aves.jpg',
    'Zopilotes benéficos': 'imgconsejos/zopilote.jpg',
    'Conservación de suelos': 'imgconsejos/suelos.jpg', 
    'Garambullo comestible': 'imgconsejos/garambullo.jpg',
    'Colibríes en peligro': 'imgconsejos/colibri.jpg',
    'Carpinteros cheje': 'imgconsejos/cheje.jpg',
    'Cactáceas nativas': 'imgconsejos/cactaceas.jpg',
    'Biznagas endémicas': 'imgconsejos/biznagas.jpg',
    'Reptiles protegidos': 'imgconsejos/reptiles.jpg',
    'Turismo ecológico': 'imgconsejos/ecoturismo.jpg',
    'Manzanilla de llano': 'imgconsejos/manzanilla.jpg',
    'Gallito de monte': 'imgconsejos/gallito.jpg',
    'Control de especies invasoras': 'imgconsejos/invasoras.jpg',
    'Consumo responsable': 'imgconsejos/consumo.jpg',
    'Kalanchoe ornamental': 'imgconsejos/kalanchoe.jpg',
    'Biznaga de acitrón': 'imgconsejos/acitron.jpeg', 
    'Chapulín arcoíris': 'imgconsejos/chapulin.jpg',
    'Mariposa Monarca': 'imgconsejos/monarca.jpg',
    'Biznaga ganchuda': 'imgconsejos/ganchuda.jpg',
    'Centzontle norteño': 'imgconsejos/centzontle.jpg',
    'Conservación de humedales': 'imgconsejos/humedales.jpg',
    'Agricultura sostenible': 'imgconsejos/agricultura.jpg',
    'Jardines polinizadores': 'imgconsejos/polinizadores.jpg', 
    'Árboles nativos': 'imgconsejos/arboles.jpg',
    'Control de plagas natural': 'imgconsejos/plagas.jpg',
    'Setos vivos': 'imgconsejos/setos.jpg',
    'Agua de lluvia': 'imgconsejos/lluvia.png',
    'Biodiversidad agrícola': 'imgconsejos/biodiversidad.jpg',
    'Corredores biológicos': 'imgconsejos/corredores.jpeg',
    'Techos verdes': 'imgconsejos/techos.jpg',
    'Humedales artificiales': 'imgconsejos/humedales_artificiales.jpg',
    'Control biológico': 'imgconsejos/biologico.jpg',
    'Educación ambiental': 'imgconsejos/educacion.jpg',
    'Jardines urbanos': 'imgconsejos/jardines.jpg',
    'Aves urbanas': 'imgconsejos/avesurbanas.jpg',
    'Movilidad sostenible': 'imgconsejos/movilidad.jpeg',
    'Árboles urbanos': 'imgconsejos/arbolesurbanos.jpg',
    'Reciclaje comunitario': 'imgconsejos/reciclaje.jpg',
    'Corredores verdes': 'imgconsejos/corredoresverdes.jpg',
    'Reforestación urbana': 'imgconsejos/reforestacionurbana.jpeg',
    'Conservación de cerros': 'imgconsejos/cerros.jpeg',
    'Agricultura periurbana': 'imgconsejos/periurbana.jpg', 
    'Flor de gallito': 'imgconsejos/florgallito.jpg',
    'Zafiro orejas blancas': 'imgconsejos/zafiro.jpg',
    'Capulinero gris': 'imgconsejos/capulinero.jpg',
    'Ranita de cañón': 'imgconsejos/ranita.jpg',
    'Carpintero bellotero': 'imgconsejos/carpintero.jpg',
    'Camaleón de montaña': 'imgconsejos/camaleon.jpg',
    'Junco ojos de lumbre': 'imgconsejos/junco.jpg',
    'Pingüica': 'imgconsejos/pinguica.jpg'
}

@consejos_bp.route('/consejos')
def mostrar_consejos():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT c.titulo, c.consejo, c.fecha, c.hora, z.nombre_region AS zona
            FROM consejos c
            JOIN zonas z ON c.zona = z.ID
            ORDER BY c.fecha DESC, c.hora DESC
        """
        cursor.execute(query)
        consejos = cursor.fetchall()

        for consejo in consejos:
            consejo['imagen'] = imagenes_consejos.get(consejo['titulo'], 'imgconsejos/default.jpg')

        cursor.close()
        conn.close()
        return render_template("consejos.html", consejos=consejos)
    except Exception as e:
        return f"Ocurrió un error al obtener los consejos: {e}"
