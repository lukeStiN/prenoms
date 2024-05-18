import streamlit as st
import pandas as pd
import numpy as np
from random import choice
import altair as alt

from utils import AREA_CHART, BAR_CHART

# sexe;preusuel;annais;nombre

if 'prenom' not in st.session_state :
    st.session_state.prenom = ''

@st.cache_data
def load_data(file_path: str = "prenoms.csv") -> pd.DataFrame:
    """
    Charge les données à partir d'un fichier CSV et les met en cache.
    """
    res = pd.read_csv(file_path, sep=";", header=0)
    res = res[(res["preusuel"] != "_PRENOMS_RARES") & (res["annais"] != "XXXX")]
    res["annais"] = pd.to_numeric(res["annais"], errors="coerce").astype("Int64")

    return res

@st.cache_data
def get_uniques(colanme: str) -> np.ndarray:
    """Retourne la liste des valeurs unique d'une colonne"""
    return load_data()[colanme].unique()

@st.cache_data
def top(n : int = 100) -> np.ndarray:
    """ Retourne les n prenoms les plus données """
    _top = load_data().groupby('preusuel')['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index()

    return _top['preusuel'][:n]

def set_prenom(value : str = ''):
    """ Definit le prenom (depuis la home) """
    if not value :
        value = st.session_state.home_prenom
    st.session_state.prenom = value.strip().upper()

st.set_page_config("Prénoms", "👥", "centered")
data = load_data()

# HOME
if st.session_state.prenom.strip().upper() not in get_uniques("preusuel") : 
    st.text_input(
        'Prénom', '', 
        placeholder=choice(top(200)).title(), 
        help='Entrez un prénom', 
        on_change=set_prenom, 
        key='home_prenom'
    )

    '---'
    st.markdown(1*'<br/>', unsafe_allow_html=True)
    '### 👧🏻 Top prénom féminin 2022'
    N = [3, 2]
    _top = data[(data["sexe"] == 2) & (data["annais"] == 2022)].groupby('preusuel')['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index()
    cols = st.columns(N[0])
    for i in range(N[0]*N[1]) :
        cols[i%N[0]].button(
            _top['preusuel'][i].title(), 
            use_container_width=True, 
            help="{:,.0f}".format(_top['nombre'][i]).replace(",", " ")+" naissances en 2022",
            on_click=set_prenom, args=[_top['preusuel'][i]]
            # type='secondary' if i%2 else 'primary'
        )

    st.markdown(1*'<br/>', unsafe_allow_html=True)
    '### 👦🏻 Top prénom masculin 2022'
    _top = data[(data["sexe"] == 1) & (data["annais"] == 2022)].groupby('preusuel')['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index()
    cols = st.columns(N[0])
    for i in range(N[0]*N[1]) :
        cols[i%N[0]].button(
            _top['preusuel'][i].title(), 
            use_container_width=True, 
            help="{:,.0f}".format(_top['nombre'][i]).replace(",", " ")+" naissances en 2022",
            on_click=set_prenom, args=[_top['preusuel'][i]]
            # type='secondary' if i%2 else 'primary'
        )

    '---'
    st.markdown(1*'<br/>', unsafe_allow_html=True)
    "### 🥇 Top selon l'année"
    an = st.slider("Année", int(get_uniques("annais").min()), int(get_uniques("annais").max()), int(get_uniques("annais").max()))
    
    N = 5
    data = data[data['annais'] == an]
    top10_h = data[data["sexe"] == 1].groupby(['preusuel', 'sexe'])['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index(drop=True).head(N)
    top10_f = data[data["sexe"] == 2].groupby(['preusuel', 'sexe'])['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index(drop=True).head(N)

    top10_h['position'] = top10_h.index + 1
    top10_f['position'] = top10_f.index + 1

    _top = pd.concat([top10_h, top10_f], ignore_index=True)
    # _top = data[data["annais"] == an].groupby(['preusuel', 'sexe'])['nombre'].sum().reset_index().sort_values(by='nombre', ascending=False).reset_index()[:10]
    # _top.to_json('res.json', orient='records')

    st.vega_lite_chart(_top, BAR_CHART, title={'text':str(an), "align": "right", "anchor": "middle"}, width=704)
    # _top['sexe_label'] = _top['sexe'].apply(lambda x: 'Garçons' if x == 1 else 'Filles')

    # chart = alt.Chart(_top).mark_bar(cornerRadiusEnd=8).encode(
    #     x=alt.X('position:N', 
    #             title='Top', 
    #             axis=alt.Axis(grid=True, tickMinStep=1, labelAngle=0),
    #             sort='-y'),
    #     y=alt.Y('nombre:Q', 
    #             title='', 
    #             axis=alt.Axis(format='~s')),
    #     color=alt.Color('sexe_label:N', 
    #                     legend=alt.Legend(title='', direction='horizontal', orient='top')),
    #     tooltip=[
    #         alt.Tooltip('preusuel:N', title='Prénom'),
    #         alt.Tooltip('nombre:Q', title='Naissances', format='~s')
    #     ],
    #     xOffset='sexe_label'
    # ).properties(
    #     width=704,
    #     padding={'bottom': 20}
    # )

    # st.altair_chart(chart)

#----------------------------------

# SEARCH
if st.session_state.prenom.strip().upper() in get_uniques("preusuel") :
    with st.sidebar:
        if st.button('Accueil', use_container_width=True) :
            st.session_state.prenom = ''
            st.rerun()

        prenom = st.text_input("Prénom", st.session_state.prenom.title()).upper().strip()
        annee = st.slider(
            "Année",
            int(get_uniques("annais").min()),
            int(get_uniques("annais").max()),
            [int(get_uniques("annais").min()), int(get_uniques("annais").max())],
        )

    if prenom:
        if prenom not in get_uniques("preusuel"):
            st.warning("Prénom inexistant")

        if prenom in get_uniques("preusuel"):
            st.session_state.prenom = prenom
            f'# {prenom.title()}'
            f"## Nombre de naissances"

            # selectionneer le prenom
            _data = data[
                (data["preusuel"] == prenom)
                & (annee[0] < data["annais"])
                & (annee[1] > data["annais"])
            ]

            st.vega_lite_chart(
                _data.groupby("annais")["nombre"].sum().reset_index(),
                AREA_CHART,
                theme=None, 
            )

