import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

link = r"C:\Documents\Wild code school\Python\Projet 2\fusion_cinema_csp_cccso.csv"
fusion_cinema_CSP_CCCSO = pd.read_csv(link)

st.title('Etude de la population de Communauté de communes Creuse Sud-Ouest')

st.write("Cinéma Claude Miller")

st.image('https://tse4.mm.bing.net/th/id/OIP.7pGYUVpSdpg2j2Bxa6wlaAHaEM?w=318&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7')
       
st.write('La commune de Bourganeuf est située à 33 km de Guéret, à 50 km de Limoges et compte 2450 hab.')

st.image('https://tse2.mm.bing.net/th/id/OLC.zKK2TDfoMPOphA480x360?&rs=1&pid=ImgDetMain')

st.write('la Communauté de communes Creuse Sud-Ouest dont elle fait partie compte 13500 hab.')

st.write("Sur les 13500 hab. de la communauté de communes en se basant sur les chiffres de l'INSEE on peut estimer que environ 3600 vont au cinemas de 1 à 3 fois par an et 1800 plus de 3 fois soit 5400 personnes")

df = fusion_cinema_CSP_CCCSO.drop([0],axis=0)

fig = px.pie(df, values='cinemas_total', names='CSP_pop_creuse',title='Répartition de la population allant au cinemas', color='CSP_pop_creuse')

st.plotly_chart(fig, use_container_width=True)

fig_1 = px.bar(df, y=['de 1 à 3 fois','plus de 3 fois'],
                x='CSP_pop_creuse',
                labels={'CSP_pop_creuse': "Population de la communauté de commune","value": "Nombre habitant apetant"}
               )

st.plotly_chart(fig_1, use_container_width=True)


