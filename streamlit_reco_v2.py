import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

df_fusion = pd.read_csv(r"C:\Documents\Wild code school\Python\Projet 2\df_fusion_v2.csv")
df_ml = pd.read_csv(r"C:\Documents\Wild code school\Python\Projet 2\df_ml.csv")
df_name_actors = pd.read_csv(r"C:\Documents\Wild code school\Python\Projet 2\df_name_actors_updated.csv")
df_concat_actors_director = pd.read_csv(r"C:\Documents\Wild code school\Python\Projet 2\df_concat_actors_director.csv")
df_director = pd.read_csv("C:\Documents\Wild code school\Python\Projet 2\df_director.csv")
df_actor = pd.read_csv("C:\Documents\Wild code school\Python\Projet 2\df_actor.csv")
df_actress = pd.read_csv("C:\Documents\Wild code school\Python\Projet 2\df_actress.csv")

df_actor_actress = pd.concat([df_actor,df_actress])

header ={"User_Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0") }

# Pour les pages: 

def tab_home():

    # Titre de la page
    st.title("Bienvenue au Cinéma Claude Miller situé dans la Creuse")


    # Image d'accueil (remplacez l'URL par le chemin de votre image)
    st.image(r"C:\Documents\Wild code school\Python\Projet 2\cinemaclaudeM.jpg", caption="Cinéma Claude Miller", use_column_width=True)

    # Section à propos
    st.subheader("À propos de nous")
    st.markdown("###### Le Cinéma Claude Miller, situé au cœur de la Creuse, est un lieu de rencontre pour les amateurs de films de tous genres. Nous proposons une large sélection de films, allant des derniers blockbusters aux films d'auteur, en passant par des classiques du cinéma.")

    # Section Programmation
    st.subheader("Programmation")
    st.markdown("###### Découvrez notre programmation hebdomadaire et ne manquez pas les dernières sorties ainsi que nos événements spéciaux.")

    # Section Suivez-nous
    st.subheader("Suivez-nous")
    st.markdown("###### Restez informé de nos dernières nouveautés et événements en nous suivant sur les réseaux sociaux :")
    st.write("""
     - [Facebook](https://www.facebook.com/people/Cin%C3%A9ma-Claude-Miller-Bourganeuf/100068268782137/)
     - [Instagram](https://www.instagram.com/explore/locations/347408022526239/cinema-claude-miller-bourganeuf/)
     - [Twitter](https://twitter.com/cinemaclaudemiller)
             
    """)


    # Exemple de programmation (ajoutez les informations réelles de votre cinéma)
    st.subheader("les horaires d'ouverture")
    st.write("""
    - **Lundi** : 8h30 - 12h30 ; après-midi fermé
    - **Mardi** : 8h30 - 12h30 ; 13h15 - 17h
    - **Mercredi** : 8h30 - 12h30 ; 13h15 - 17h
    - **Jeudi** : 8h30 - 12 h30 ; après-midi fermé 
    - **Vendredi** : 8h30 – 12h30 ; 13h15 - 17h
    """)
    st.markdown("###### L’accès handicapé s’effectue derrière la mairie (cour intérieure du château)")

    # Section Tarifs
    st.subheader("Tarifs")
    st.write(""" 
    
    - **Tarif Normal** : 6,00 €
    - **Tarif Réduit 1** : 5,00 € (étudiants, Tarif réduit le mercredi et lundi à 21h)
    - **Tarif Réduit 2** : 4,00 € (Tarif réduit le mercredi aprés-midi)
    - **Tarif Enfant** : 4,00 € (moins de 12 ans)
    - **Tarif Famille** : 18,00 € (1 couple + 2 enfants de -12 ans)
    - **Tarif Lunettes 3D** : 1,00 € (Pour les projections de films en 3D (location de lunettes)) 
    - **Tarif Groupe scolaire** : 3,00 € (Groupe scolaire de 70 à 150 élèves)
    - **Tarif Grooupe scolaire** : 4,00 € (Groupe scolaire < 70 élèves)
    - **Tarif Groupe scolaire** : 2,00 € (Groupe scolaire >150) 
    - **Tarif Etablissement public** : 3,00 € (Centres de loisirs, centre hospitalier, commune) 
    - **Tarif Soirée thématique** : 9,00 € (Diffusion de 2 films consécutifs (tarif pour 2 films) - Enfant de moins de 14 ans : 8€)
      
    """)

    # Section Contact
    st.subheader("Contact")
    st.markdown("###### Vous avez des questions ou souhaitez réserver une séance privée ? N'hésitez pas à nous contacter !")
    st.write(""" 
    
    - **Adresse** : Place de l’Hôtel de Ville, 23400 BOURGANEUF
    - **Téléphone** : 05 55 64 02 26
    - **Fax** : 05 55 64 02 12
    - **Email** : contact@cinemaclaudemiller.fr, contact@bourganeuf.fr
    """)

def tab_films():
    # Interface utilisateur
    st.title("Système de recommandation de films")
    st.markdown("<hr>", unsafe_allow_html=True)

    # CSS pour styliser les boutons avec du texte blanc
    st.markdown("""
        <style>
        .stButton button {
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)
    

    # Collecte des préférences de l'utilisateur
    favorite_film = st.selectbox(
        "",
        (df_fusion["affichage"]),
        index=None,
        placeholder="Choisissez votre film préféré",
    )

    # Affichage des recommandations
    if st.button("Obtenir des recommandations"):


        # Fonction pour afficher les étoiles en fonction de la note
        def display_stars(rating):
            stars_full = int(rating / 2)
            stars_half = int((rating / 2 - stars_full) >= 0.5)
            stars_empty = 5 - stars_full - stars_half
            return "★" * stars_full + "" * stars_half + "☆" * stars_empty

        # CSS pour styliser les étoiles de notation et le synopsis
        st.markdown("""
        <style>
        .star-rating {
            color: #640F13;
            font-size: 30px;
        }
        .synopsis-title {
            font-size: 25px;
            color: #333;
            margin-top: 27px;
            margin-bottom: 10px;
        }
        .synopsis-text {
            font-size: 16px;
            color: #070707;
        }
        </style>
        """, unsafe_allow_html=True)

        # Logique de recommandation en fonction des préférences de l'utilisateur

        film = df_fusion.copy(deep=True)[df_fusion["affichage"] == favorite_film]

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://image.tmdb.org/t/p/w500/" + film['poster_path'].values[0])  # Remplacez par le chemin vers l'image du film

        with col2:
            st.subheader(f"{film['French_Title'].values[0]}")
            st.markdown(f"###### Année de sortie : {film['startYear'].values[0]}")
            st.markdown(f"###### Durée : {film['Run_Time'].values[0]} min")
            st.markdown(f"###### Genres : {film['genres'].values[0]}")

            df_a = df_concat_actors_director[df_concat_actors_director['tconst'] == film['imdb_id'].values[0]]
            df_1 = df_a[df_a['category'] == 'director']
            df_2 = df_a[df_a['ordering'] < 5]
            list_director = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_1['nconst'].values[x]].values[0] for x in range(len(df_1))]
            list_actor = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_2['nconst'].values[x]].values[0] for x in range(len(df_2))]

            st.markdown(f"###### De {', '.join(list_director)}")
            st.markdown(f"###### Avec " + ', '.join(list_actor))
            st.markdown(f"###### Note: <span class='star-rating'>{display_stars(film['vote_average'].values[0])}</span> ", unsafe_allow_html=True)
            
            movie_id = film['id'].values[0]
            url = "https://www.themoviedb.org/movie/" + str(movie_id)
            reponse = requests.get(url)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            synopsis = soup.find('div', {"class": "overview"}).text.replace("\n", "")
            st.markdown(f"<div class='synopsis-title'>Synopsis</div><div class='synopsis-text'>{synopsis}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

        st.subheader("Voici nos recommandations en fonction de votre film préféré : ")
        st.markdown("<hr>", unsafe_allow_html=True)


    # Machine learning :

        ligne_film = df_ml.copy(deep=True)[df_fusion["affichage"] == favorite_film]
        X = df_ml.drop(columns=['origin_country', 'imdb_id', 'genres', 'French_Title','startYear' ,'Original_Title','affichage', 'Run_Time', 'vote_average','vote_count', 'Region'])
        from sklearn.neighbors import NearestNeighbors

        distanceKNN = NearestNeighbors(n_neighbors=11).fit(X)

        ligne_film.drop(columns=['origin_country', 'imdb_id', 'genres', 'vote_average','startYear', 'vote_count', 'French_Title', 'Original_Title', 'affichage','Run_Time','Region'], axis=1,inplace = True)

        neighbors = distanceKNN.kneighbors(ligne_film)

        df_propo = df_fusion[df_fusion['imdb_id'] == 0]

        for x in range(1, 11):
            id_propo = df_ml[['imdb_id']].iloc[neighbors[1][0][x]]
            id_propo = id_propo.values[0]
            propo = df_fusion[df_fusion['imdb_id'] == id_propo]
            df_propo = pd.concat([df_propo, propo])
            
        df_propo = df_propo[df_propo["affichage"] != favorite_film]
        df_propo.sort_values(by=['vote_average'], ignore_index=True, ascending=False, inplace=True)

        # Afficher les recommandations 1, 2 et 3 en colonnes

        st.subheader("Top 3 Recommandations")
        cols = st.columns(3)
    
        for idx in range(0,3):
            propo_film = df_propo[idx:idx+1]
            col = cols[idx]
            col.markdown(f"###### Recommandation numéro {idx+1} :")
            
            df_a = df_concat_actors_director[df_concat_actors_director['tconst'] == propo_film['imdb_id'].values[0]]
            df_1 = df_a[df_a['category'] == 'director']
            df_2 = df_a[df_a['ordering'] < 5]
            list_director = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_1['nconst'].values[x]].values[0] for x in range(len(df_1))]
            list_actor = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_2['nconst'].values[x]].values[0] for x in range(len(df_2))]

            movie_id = propo_film['id'].values[0]
            url = "https://www.themoviedb.org/movie/" + str(movie_id)
            reponse = requests.get(url)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            synopsis = soup.find('div', {"class": "overview"}).text.replace("\n", "")
       
            with col:
                col.image("https://image.tmdb.org/t/p/w500/" + propo_film['poster_path'].values[0])  
                col.subheader(f"{propo_film['French_Title'].values[0]}")
                col.markdown(f"###### Année de sortie : {propo_film['startYear'].values[0]}")
                col.markdown(f"###### Durée : {propo_film['Run_Time'].values[0]} min")
                col.markdown(f"###### Genres : {propo_film['genres'].values[0]}")
                col.markdown(f"###### De {', '.join(list_director)}")
                col.markdown(f"###### Avec " + ', '.join(list_actor))
                col.markdown(f"###### Note: <span class='star-rating'>{display_stars(propo_film['vote_average'].values[0])}</span> ", unsafe_allow_html=True)
                col.markdown(f"<div class='synopsis-title'>Synopsis</div><div class='synopsis-text'>{synopsis}</div>", unsafe_allow_html=True)
                
        st.markdown("<hr>", unsafe_allow_html=True)

        # Afficher les recommandations 4, 5 et 6 en colonnes

        cols = st.columns(3)
        
        for idx, col in enumerate(cols):
            propo_film = df_propo[idx+3:idx+4]
            col.write(f"###### Recommandation numéro {idx+4} :")
            
            df_a = df_concat_actors_director[df_concat_actors_director['tconst'] == propo_film['imdb_id'].values[0]]
            df_1 = df_a[df_a['category'] == 'director']
            df_2 = df_a[df_a['ordering'] < 5]
            list_director = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_1['nconst'].values[x]].values[0] for x in range(len(df_1))]
            list_actor = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_2['nconst'].values[x]].values[0] for x in range(len(df_2))]

            movie_id = propo_film['id'].values[0]
            url = "https://www.themoviedb.org/movie/" + str(movie_id)
            reponse = requests.get(url)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            synopsis = soup.find('div', {"class": "overview"}).text.replace("\n", "")
        
            with col: 
                    col.image("https://image.tmdb.org/t/p/w500/" + propo_film['poster_path'].values[0])
                    col.subheader(f"{propo_film['French_Title'].values[0]}")
                    col.markdown(f"###### Année de sortie : {propo_film['startYear'].values[0]}")
                    col.markdown(f"###### Durée : {propo_film['Run_Time'].values[0]} min")
                    col.markdown(f"###### Genres : {propo_film['genres'].values[0]}")
                    col.markdown(f"###### De {', '.join(list_director)}")
                    col.markdown(f"###### Avec " + ', '.join(list_actor))
                    col.markdown(f"###### Note: <span class='star-rating'>{display_stars(propo_film['vote_average'].values[0])}</span> ", unsafe_allow_html=True)
                    col.markdown(f"<div class='synopsis-title'>Synopsis</div><div class='synopsis-text'>{synopsis}</div>", unsafe_allow_html=True)
                
        st.markdown("<hr>", unsafe_allow_html=True)


# Afficher les recommandations 7, 8 et 9 en colonnes

        cols = st.columns(3)
        
        for idx, col in enumerate(cols):
            propo_film = df_propo[idx+6:idx+10]
            col.markdown(f"###### Recommandation numéro {idx+7} :")
            
            df_a = df_concat_actors_director[df_concat_actors_director['tconst'] == propo_film['imdb_id'].values[0]]
            df_1 = df_a[df_a['category'] == 'director']
            df_2 = df_a[df_a['ordering'] < 5]
            list_director = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_1['nconst'].values[x]].values[0] for x in range(len(df_1))]
            list_actor = [df_name_actors['primaryName'][df_name_actors['nconst'] == df_2['nconst'].values[x]].values[0] for x in range(len(df_2))]

            movie_id = propo_film['id'].values[0]
            url = "https://www.themoviedb.org/movie/" + str(movie_id)
            reponse = requests.get(url)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            synopsis = soup.find('div', {"class": "overview"}).text.replace("\n", "")
            
            with col:
                col.image("https://image.tmdb.org/t/p/w500/" + propo_film['poster_path'].values[0])
                col.subheader(f"{propo_film['French_Title'].values[0]}")
                col.markdown(f"###### Année de sortie : {propo_film['startYear'].values[0]}")
                col.markdown(f"###### Durée : {propo_film['Run_Time'].values[0]} min")
                col.markdown(f"###### Genres : {propo_film['genres'].values[0]}")
                col.markdown(f"###### De {', '.join(list_director)}")
                col.markdown(f"###### Avec " + ', '.join(list_actor))
                col.markdown(f"###### Note: <span class='star-rating'>{display_stars(propo_film['vote_average'].values[0])}</span> ", unsafe_allow_html=True)
                col.markdown(f"<div class='synopsis-title'>Synopsis</div><div class='synopsis-text'>{synopsis}</div>", unsafe_allow_html=True)

#-----------------------

def tab_acteurs():
    st.title("Acteurs")

    df_name_act = pd.merge(df_name_actors,df_actor_actress['nconst'], how= 'right', left_on='nconst', right_on='nconst')
    df_name_act = df_name_act[~df_name_act.duplicated(subset=['nconst'])]
    
    favorite_Acteurs = st.selectbox(
        "",
        (df_name_act["affichage"]),
        index=None,
        placeholder="Choisissez votre acteur préféré",
        )
    if st.button("Obtenir des infos"):
        df_favorite_Acteurs = df_name_actors[df_name_actors["affichage"]== favorite_Acteurs]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(df_favorite_Acteurs['photo'].values[0])

        with col2:
            id = df_favorite_Acteurs['nconst'].values[0]
            url = "https://www.imdb.com/name/" + str(id)+"/bio"
            reponse = requests.get(url, headers=header)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            d_n = soup.find_all('div', {"class": "ipc-html-content-inner-div"})
            naissance = d_n[0].text

            df_t = df_actor_actress[df_actor_actress['nconst'] == id]
            df_fin = df_t[~df_t.duplicated(subset=['tconst'])]
            nb_film= len(df_fin)

            df_f_tri = df_fusion[df_fusion['imdb_id']== 0]
            for ind, var in enumerate(df_fin['tconst']):
                df_f = df_fusion[df_fusion['imdb_id']== var]
                df_f_tri = pd.concat([df_f_tri,df_f])

            df_n = df_name_actors[df_name_actors['nconst'] == id]
            list_tconst = df_n['knownForTitles'].values[0].split(",")
            list_films =[]
            for val in list_tconst:
                film = df_fusion[df_fusion['imdb_id'] == val]
                list_films.append(film['French_Title'].values[0])

            st.subheader(f"{df_favorite_Acteurs['primaryName'].values[0]}")
            st.markdown(f"###### Né(e) le : {naissance}")
            st.markdown(f"###### A joué dans {nb_film} films sur la periode de {df_f_tri['startYear'].min()} à {df_f_tri['startYear'].max()}")
            st.markdown(f"###### Connue entre autre pour ses rôles dans : ")
            st.markdown(f"###### {list_films[0]} ")
            st.markdown(f"###### {list_films[1]} ")
            st.markdown(f"###### {list_films[2]} ")
            st.markdown(f"###### {list_films[3]} ")    

        st.markdown(f"###### Mini-biographie : ")
        st.markdown(f"###### {df_favorite_Acteurs['describe'].values[0]}")
#----------------------- 

def tab_realisateurs():

    st.title("Réalisateurs")
    df_name_dir = pd.merge(df_name_actors, df_director['nconst'], how= 'right', left_on='nconst', right_on='nconst')
    df_name_dir = df_name_dir[~df_name_dir.duplicated(subset=['nconst'])]
    favorite_Réal = st.selectbox(
        "",
        (df_name_dir["affichage"]),
        index=None,
        placeholder="Choisissez votre réalisateur préféré",
        )
    
    if st.button("Obtenir des infos"):
        df_favorite_Réal = df_name_actors[df_name_actors["affichage"]== favorite_Réal]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(df_favorite_Réal['photo'].values[0])

        with col2:
            id = df_favorite_Réal['nconst'].values[0]
            url = "https://www.imdb.com/name/" + str(id)+"/bio"
            reponse = requests.get(url, headers=header)
            soup = BeautifulSoup(reponse.text, 'html.parser')
            d_n = soup.find_all('div', {"class": "ipc-html-content-inner-div"})
            naissance = d_n[0].text

            df_d = df_director[df_director['nconst'] == id]
            df_fin_d = df_d[~df_d.duplicated(subset=['tconst'])]
            nb_film_d= len(df_fin_d)

            df_f_tri_d = df_fusion[df_fusion['imdb_id']== 0]
            for ind, var in enumerate(df_fin_d['tconst']):
                df_f_d = df_fusion[df_fusion['imdb_id']== var]
                df_f_tri_d = pd.concat([df_f_tri_d,df_f_d])

            df_n = df_name_actors[df_name_actors['nconst'] == id]
            list_tconst = df_n['knownForTitles'].values[0].split(",")
            list_films =[]
            for val in list_tconst:
                film = df_fusion[df_fusion['imdb_id'] == val]
                list_films.append(film['French_Title'].values[0])

            st.subheader(f"{df_favorite_Réal['primaryName'].values[0]}")
            st.markdown(f"###### Né(e) le : {naissance}")
            st.markdown(f"###### A réalisé {nb_film_d} films sur la periode de {df_f_tri_d['startYear'].min()} à {df_f_tri_d['startYear'].max()}")
            st.markdown(f"###### Connue entre autre pour avoir réalisé :")
            st.markdown(f"###### {list_films[0]} ")
            st.markdown(f"###### {list_films[1]} ")
            st.markdown(f"###### {list_films[2]} ")
            st.markdown(f"###### {list_films[3]} ")
        st.markdown(f"###### Mini-biographie : ")
        st.markdown(f"###### {df_favorite_Réal['describe'].values[0]}")


# Configuration des onglets
tabs = {
    "Accueil🎞️": tab_home,
    "Recommandations de films📽️": tab_films,
    "Acteurs✨": tab_acteurs,
    "Réalisateurs🎬": tab_realisateurs
    }

# Création des onglets
def main():
    st.sidebar.header("Navigation")
    selected_tab = st.sidebar.radio("", list(tabs.keys()))
    tabs[selected_tab]()


 # Afficher l'image de la sidebar( totem)
    st.sidebar.image(r"C:\Documents\Wild code school\Python\Projet 2\Capture_decran_2024-05-24_094554.png", use_column_width=True)
 

# pour mettre la couleur de sidebar
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
                background-color : #640F13 ;
                background-size: cover;
        }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
        <style>
            h2, p {
                color : #ffffff ;
                },
                h6, p {
                color : #000000 ;
                }
    </style>
    """, unsafe_allow_html=True)



    st.markdown("""
        <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://i.ibb.co/q99qg2S/Capture-d-cran-2024-05-27-171659.png" );
    background-size: cover;
    }
      </style>
        """, unsafe_allow_html=True)
    


if __name__ == "__main__":
    main()
