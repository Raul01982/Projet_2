import streamlit as st
import pandas as pd
import seaborn as sns

link="https://www.insee.fr/fr/statistiques/2011101?geo=DEP-23#chiffre-cle-1"
link_1="https://www.insee.fr/fr/statistiques/2407676#graphique-figure1_radio1"
pop_creuse = pd.read_html(link)
culturel_creuse = pd.read_html(link_1)

def refaire_tx(df):
    df = df/10
    return df

# recuperer le tableau de la population de la creuse par CSP (2020) et le rendre exploitable

pop_creuse_csp = pop_creuse[7]
titre_1 = ['CSP_pop_creuse','2009','%_2009','2014','%_2014','2020','%_2020']
pop_creuse_csp.columns = titre_1
for x in pop_creuse_csp:
        if x == '%_2009'or  x == '%_2014'or x == '%_2020':
                #print(pop_creuse_csp[x])
                pop_creuse_csp[x] = pop_creuse_csp[x].apply(refaire_tx)
pop_creuse_csp  

# recuperer le tableau de la population de la creuse par Age (2020) et le rendre exploitable

pop_creuse_age = pop_creuse[0]
titre_2 = ['Age_pop_creuse','2009','%_2009','2014','%_2014','2020','%_2020']
pop_creuse_age.columns = titre_2
for x in pop_creuse_age:
        if x == '%_2009'or  x == '%_2014'or x == '%_2020':
                #print(pop_creuse_csp[x])
                pop_creuse_age[x] = pop_creuse_age[x].apply(refaire_tx)
pop_creuse_age

# recuperer le tableau fracantation cinemas par CSP (2022) et le rendre exploitable

culturel_creuse_csp = culturel_creuse[0]
for x in culturel_creuse_csp:
        if x == 'Catégorie socioprofessionnelle':
                pass
        else:
                culturel_creuse_csp[x] = culturel_creuse_csp[x].apply(refaire_tx)   
culturel_creuse_csp

# recuperer le tableau fracantation cinemas par Age (2022) et le rendre exploitable

culturel_creuse_age = culturel_creuse[1]
titre=[]
for x in culturel_creuse_age:
        x = x[1]
        titre.append(x)
print(titre)
print(type(titre))

culturel_creuse_age.columns = titre
culturel_creuse_age = culturel_creuse_age.drop(columns='Unnamed: 5_level_1').drop(columns='Unnamed: 6_level_1')
for x in culturel_creuse_age:
        if x == 'Âge et sexe':
                pass
        else:
                culturel_creuse_age[x] = culturel_creuse_age[x].apply(refaire_tx)
culturel_creuse_age['Âge et sexe'][16] = 'Tout ages'
titre_4 =['Age','Genre','Aucune fois','De 1 à 3 fois','Plus de 3 fois','Ne sait pas / Refus']
culturel_creuse_age['Age'] = culturel_creuse_age['Âge et sexe']

col = culturel_creuse_age.pop("Age")
culturel_creuse_age.insert(loc=0, column="Age", value=col)

culturel_creuse_age.columns = titre_4
culturel_creuse_age['Age'] = culturel_creuse_age['Age'].replace('Femmes','X').replace('Hommes','X').replace('Ensemble','X')
culturel_creuse_age['Genre'] = culturel_creuse_age['Genre'].replace('16-24 ans','X').replace('25-39 ans','X').replace('40-59 ans','X').replace('60 ans ou plus','X').replace('Tout ages','X')

for x in range(0,20):
    if culturel_creuse_age['Age'][x] == 'X':
        culturel_creuse_age['Age'][x]=culturel_creuse_age['Age'][x-1]

liste = []
for x in range(0,20):
        if culturel_creuse_age['Genre'][x] == 'X':
            liste.append(x)
print(liste)

culturel_creuse_age = culturel_creuse_age.drop(culturel_creuse_age.index[liste], axis=0)
            
culturel_creuse_age