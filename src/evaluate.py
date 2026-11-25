import time # ni ovozmozuva merenje na vremeto na izvrsuvanje
import pandas as pd # ni ovozmozuva rabota so tabelarni podatoci
from recommender import recommend_books # ja importira funkcijata za preporacuvanje


# VCITUVANJE NA TEST PODATOCITE

evaluation_df = pd.read_csv("tests/evaluation_queries.csv") # go vcituva CSV fajlot vo koj se zachuvani test vnesovite

test_queries = evaluation_df["query"].tolist() # gi zema vrednostite od kolonata query i gi pretvora vo lista

print("\nNumber of test queries:", len(test_queries)) # go prikazuva vkupniot broj na test vnesovi


# TESTIRANJE NA AI ALGORITMOT

evaluation_results = [] # prazna lista vo koja ke gi zachuvuvame rezultatite od site testiranja
for query in test_queries: # pominuva niz sekoj test vnes od listata

    print("\nTest query:", query) # go prikazuva momentalniot test vnes

    start_time = time.perf_counter() # go zachuvuva vremeto pred povikuvanje na funkcijata

    recommendations = recommend_books(query) # ja povikuva funkcijata za dobivanje preporaki

    end_time = time.perf_counter() # go zachuvuva vremeto po dobivanje na preporakite

    execution_time = end_time - start_time # presmetuva kolku vreme bilo potrebno za dobivanje na rezultatite

    print("Number of recommendations:", len(recommendations)) # go prikazuva brojot na dobieni preporaki

    print("Execution time:", round(execution_time, 4), "seconds") # go prikazuva vremeto na izvrsuvanje vo sekundi

    print(recommendations.to_string(index=False)) # gi prikazuva dobienite preporaki

     # ZACHUVUVANJE NA PREPORAKITE

    for rank, (_, book) in enumerate(recommendations.iterrows(), start=1): # pominuva niz sekoja preporaka i go odreduva nejziniot rang

        evaluation_results.append({
            "query": query,
            "rank": rank,
            "title": book["title"],
            "author": book["author"],
            "genre": book["genre"],
            "similarity_score": book["similarity_score"],
            "relevant": ""
        }) # gi dodava podatocite za sekoja preporaka vo listata

     # KREIRANJE NA CSV FAJL SO REZULTATITE

results_df = pd.DataFrame(evaluation_results) # ja pretvora listata so rezultati vo tabela

results_df.to_csv(
    "tests/evaluation_results.csv",
    index=False,
    encoding="utf-8-sig"
) # gi zachuvuva rezultatite vo CSV fajl bez indeks na redovite

print("\nEvaluation results saved successfully.")

print("Total saved recommendations:", len(results_df)) # go prikazuva vkupniot broj na zachuvani preporaki      