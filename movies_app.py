import streamlit as st
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )

# Función para consultar datos de películas
def fetch_movies_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies ORDER BY Rating DESC")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

# Función para consultar datos de series
def fetch_series_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM series ORDER BY Rating DESC")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

# Función para mostrar la página de bienvenida
def welcome_page():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .welcome-title {
            color: #ff6347;
            font-size: 36px; /* Modificar el tamaño del título aquí */
        }
        .welcome-text {
            color: #FFFFFF;
        }
        .ranking-title {
            color: #FFFFFF;
        }
        .ranking-card {
            background-color: #333333;
            color: #FFFFFF;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .info-container {
            margin-left: 20px; /* Ajusta el margen izquierdo del contenido */
        }
        @media (prefers-color-scheme: light) {
            body {
                background-color: #FFFFFF;
                color: #000000;
            }
            .welcome-title {
                color: #ff6347;
                font-size: 36px; /* Modificar el tamaño del título aquí */
            }
            .welcome-text {
                color: #000000;
            }
            .ranking-title {
                color: #000000;
            }
            .ranking-card {
                background-color: #F0F0F0;
                color: #000000;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="welcome-title">Bienvenido a MovieRank 🎬</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="welcome-text">
        ¿Eres un amante del cine y las series? ¡Estás en el lugar perfecto! En MovieRank, te ofrecemos los rankings más actualizados de las mejores películas y series. Descubre nuevas producciones, explora los éxitos más recientes y encuentra tus próximas favoritas.
        <br><br>
        ¿Qué Ofrecemos?
        <ul>
            <li><b>Rankings de Películas y Series:</b> Los mejores títulos, ordenados por su popularidad y críticas.</li>
            <li><b>Detalles y Reseñas:</b> Información completa sobre cada título, incluyendo sinopsis, ratings y más.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

    st.image("C:/Users/Aleja/Downloads/view-3d-cinema-elements.jpg", use_column_width=True)

    st.markdown(
        """
        <div class="welcome-text">
        ¿Estás listo para descubrir los rankings?
        </div>
        """, unsafe_allow_html=True
    )

    # Botón para ir a los rankings
    if st.button("Explorar Rankings"):
        st.session_state.show_rankings = True
        st.experimental_rerun()

# Función para mostrar los rankings de películas y series
def show_rankings():
    st.markdown(
        """
        <style>
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #000000;
                color: #FFFFFF;
            }
            .ranking-title {
                color: #FFFFFF;
            }
            .ranking-card {
                background-color: #333333;
                color: #FFFFFF;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .info-container {
                margin-left: 20px; /* Ajusta el margen izquierdo del contenido */
            }
        }
        @media (prefers-color-scheme: light) {
            body {
                background-color: #FFFFFF;
                color: #000000;
            }
            .ranking-title {
                color: #000000;
            }
            .ranking-card {
                background-color: #F0F0F0;
                color: #000000;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            }
            .info-container {
                margin-left: 20px; /* Ajusta el margen izquierdo del contenido */
            }
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.title("Rankings 💫")

    st.sidebar.title("¿Qué deseas ver? 👀")
    option = st.sidebar.radio("", ("Selecciona una opción", "Películas", "Series"), key="ranking_option")

    if option == "Películas":
        show_movies_data()
    elif option == "Series":
        show_series_data()
    else:
        st.write("Selecciona una opción en la barra lateral para ver el ranking correspondiente.")

# Función para mostrar datos de películas
def show_movies_data():
    movies_data = fetch_movies_data()
    if movies_data:
        for index, movie in enumerate(movies_data, start=1):
            st.markdown(
                f"""
                <div class="ranking-card">
                    <h2 class="ranking-title">Ranking #{index}</h2>
                    <div class="info-container">
                        <ul style='list-style-type: none; padding-left: 0;'>
                            <li><b>Título:</b> {movie[0]}</li>
                            <li><b>Año:</b> {movie[1]}</li>
                            <li><b>Duración:</b> {movie[2]} minutos</li>
                            <li><b>Rating:</b> {movie[3]}</li>
                            <li><b>Descripción:</b> {movie[4]}</li>
                            <li><b>Géneros:</b> {movie[5]}</li>
                            <li><b>Creadores:</b> {movie[6]}</li>
                            <li><b>Elenco Principal:</b> {movie[7]}</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.write("No hay datos de películas disponibles.")

# Función para mostrar datos de series
def show_series_data():
    series_data = fetch_series_data()
    if series_data:
        for index, serie in enumerate(series_data, start=1):
            st.markdown(
                f"""
                <div class="ranking-card">
                    <h2 class="ranking-title">Ranking #{index}</h2>
                    <div class="info-container">
                        <ul style='list-style-type: none; padding-left: 0;'>
                            <li><b>Título:</b> {serie[0]}</li>
                            <li><b>Año:</b> {serie[1]}</li>
                            <li><b>Duración:</b> {serie[2]} minutos por episodio</li>
                            <li><b>Rating:</b> {serie[3]}</li>
                            <li><b>Descripción:</b> {serie[4]}</li>
                            <li><b>Géneros:</b> {serie[5]}</li>
                            <li><b>Creadores:</b> {serie[6]}</li>
                            <li><b>Elenco Principal:</b> {serie[7]}</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.write("No hay datos de series disponibles.")

# Ejecutar la aplicación
if __name__ == "__main__":
    if "show_rankings" not in st.session_state:
        st.session_state.show_rankings = False

    if st.session_state.show_rankings:
        show_rankings()
    else:
        welcome_page()
