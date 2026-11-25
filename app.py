import streamlit as st # ni ovozmozuva kreiranje na web aplikacija
from src.recommender import recommend_books # ja importira funkcijata za preporacuvanje na literaturni dela


# KONFIGURACIJA NA WEB APLIKACIJATA

st.set_page_config(
    page_title="LiteraMK-AI", # go odreduva naslovot na web stranicata
    page_icon="📚", # ja odreduva ikonata na web stranicata
    layout="wide" # ovozmozuva koristeње na pogolema shirina na ekranot
)


# NASLOV I OPIS NA APLIKACIJATA

st.title("📚 LiteraMK-AI") # go prikazuva glavniot naslov na aplikacijata

st.subheader("Откриј ја македонската литература") # prikazuva podnaslov

st.write(
    "Пронајди литературни дела според твоите интереси "
    "со помош на вештачка интелигенција."
) # prikazuva kratok opis za namenata na aplikacijata


# KORISNICKI VNES

interests = st.text_input(
    "Внеси ги твоите интереси:",
    placeholder="Пример: љубов, семејство, традиција"
) # kreira pole za vnesuvanje tekst i go zachuvuva vnesot vo promenlivata interests


# KOPCHE ZA DOBIVANJE PREPORAKI

if st.button("Пронајди препораки"): # proveruva dali korisnikot go kliknal kopcheto

    # VALIDACIJA NA KORISNICKIOT VNES

    if not interests.strip(): # gi otstranuva praznite mesta i proveruva dali vnesot e prazen

        st.warning("Ве молиме внесете ги вашите интереси.") # prikazuva predupreduvanje dokolku nema validen vnes

    else:

        # POVIKUVANJE NA AI ALGORITMOT

        recommendations = recommend_books(interests) # ja povikuva funkcijata i gi isprakja interesite na korisnikot do AI algoritmot


        # PROVERKA NA REZULTATITE

        if recommendations.empty: # proveruva dali tabelata so preporaki e prazna

            st.info("Не се пронајдени релевантни препораки.") # prikazuva poraka dokolku nema soodvetni rezultati

        else:

            # PRIKAZUVANJE NA PREPORAKITE

            st.success("Успешно се пронајдени препораки!") # prikazuva poraka za uspesno pronajdeni rezultati

            st.subheader("Препорачани литературни дела") # prikazuva naslov nad tabelata

            st.dataframe(
                recommendations,
                hide_index=True # go sokriva indeksot na redovite vo tabelata
            ) # gi prikazuva preporačanite literaturni dela vo interaktivna tabela