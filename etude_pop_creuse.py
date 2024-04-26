import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

fusion_cinema_CSP_CCCSO = pd.read_csv ("https://raw.githubusercontent.com/Raul01982/Projet_2/main/fusion_cinema_csp_cccso.csv")
estimation_spectateur = pd.read_csv("https://raw.githubusercontent.com/Raul01982/Projet_2/main/estimation_spectateur.csv")

st.title("Cinéma Claude Miller")

st.write('Etude de la population de la Communauté de Communes Creuse Sud-Ouest')

st.image('https://tse4.mm.bing.net/th/id/OIP.7pGYUVpSdpg2j2Bxa6wlaAHaEM?w=318&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7')
       
st.write('La commune de Bourganeuf est située à 33 km de Guéret, à 50 km de Limoges et compte 2 450 hab.')

st.image('https://tse2.mm.bing.net/th/id/OLC.zKK2TDfoMPOphA480x360?&rs=1&pid=ImgDetMain')

st.write('La Communauté de Communes Creuse Sud-Ouest dont elle fait partie compte 13 500 hab.')

st.write("Sur les 13 500 hab. de la Communauté de Communes, en se basant sur les chiffres de l'INSEE, on estime à environ 3 600 personnes allant au cinema de 1 à 3 fois par an et 1 800 personnes allant plus de 3 fois par an soit 5 400 personnes.")

df = fusion_cinema_CSP_CCCSO.drop([0],axis=0)

fig = px.pie(df, values='cinemas_total', names='CSP_pop_creuse',title='Répartition de la population allant au cinéma', color='CSP_pop_creuse')

st.plotly_chart(fig, use_container_width=True)

fig_1 = px.bar(df, y=['de 1 à 3 fois','plus de 3 fois'],
                x='CSP_pop_creuse',
                labels={'CSP_pop_creuse': "Population de la Communauté de Commune","value": "Estimation en nombre habitant"},
                title='Fréquence de sortie au cinéma en fonction de la catégorie socio-professionnelle'
               )

st.plotly_chart(fig_1, use_container_width=True)

df_1 = estimation_spectateur.drop([0],axis=0)

st.write('Estimations des entrées potentielles du cinéma')

fig_2 = go.Figure(data=[
        go.Bar(name='Estimation haute',
           x=df_1['CSP_pop_creuse'], 
           y=df_1['estimation haute'],
           text=df_1['estimation haute'],
           textposition="outside",),
           go.Bar(name='Estimation basse', 
           x=df_1['CSP_pop_creuse'], 
           y=df_1['estimation basse'],
           text=df_1['estimation basse'],
           textposition="outside",)
        ])
# Change the bar mode
fig_2.update_layout(barmode='group')

st.plotly_chart(fig_2, use_container_width=True)

st.write("En 2022, Le cinèma Claude Miller a fait 8 820 entrées, ce qui est en dessous de l'estimation basse sur le potentiel d'entrée sur le secteur (environ 10 900).")

st.write("Nous pouvons constater que les retraités et les personnes sans activité représentent le potentiel d'entrée le plus important, 41% environ.")

st.write("Ces deux catégories ont des points communs et peuvent être travaillées avec une même stratégie, d'une part tarifaire et d'autre part avec une offre de film spécifique !")
