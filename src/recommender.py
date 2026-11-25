import pandas as pd # ni ovozmozuva rabota so tabelarni podatoci
from sklearn.feature_extraction.text import TfidfVectorizer # go pretvora tekstot vo numericki vektori so TF-IDF
from sklearn.metrics.pairwise import cosine_similarity # presmetuva slichnost megju vektori


# VCITUVANJE NA DATASETOT

df = pd.read_csv("data/processed/books.csv", dtype={"code": str}) # go vcituva nashiot obraboten dataset

print("Books loaded:", len(df)) # go prikazuva brojot na vcitani literaturni dela


# KREIRANJE NA TF-IDF MODEL

vectorizer = TfidfVectorizer(
    max_features=10000 # go ogranicuva vokabularot na najmnogu 10 000 termini
)

tfidf_matrix = vectorizer.fit_transform(df["text"]) # go uci vokabularot i gi pretvora tekstovite vo numericki vektori

print("\nTF-IDF MODEL")
print("Matrix shape:", tfidf_matrix.shape) # go prikazuva brojot na redovi i koloni vo matricata
print("Vocabulary size:", len(vectorizer.vocabulary_)) # go prikazuva brojot na termini vo vokabularot


# FUNKCIJA ZA PREPORACUVANJE NA LITERATURNI DELA

def recommend_books(query): # funkcijata gi prima interesite na korisnikot

    query = query.strip().lower() # gi otstranuva praznite mesta od pocetokot i krajot i gi pretvora golemite bukvi vo mali

    if not query: # proveruva dali korisnikot vnese prazen tekst
        return pd.DataFrame() # vrakja prazna tabela dokolku nema validen vnes

    query_vector = vectorizer.transform([query]) # go pretvora korisnickiot vnes vo numericki vektor koristejki go vekje nauceniot vokabular

    print("Query vector shape:", query_vector.shape) # ja prikazuva dimenzijata na vektorot na korisnickiot vnes


    # PRESMETUVANJE NA SLICHNOST

    similarity_scores = cosine_similarity(
        query_vector, tfidf_matrix # presmetuva slichnost megju korisnickiot vnes i site literaturni dela
    ).flatten() # go pretvora dvodimenzionalniot rezultat vo ednodimenzionalen niz

    print("Number of similarity scores:", len(similarity_scores)) # go prikazuva brojot na presmetani vrednosti na slichnost

    print("First 5 similarity scores:", similarity_scores[:5]) # gi prikazuva prvite pet vrednosti na slichnost


    # PODGOTOVKA NA REZULTATITE

    results = df.copy() # kreira kopija od originalniot dataset za da ne go menuvame pri sekoe novo prebaruvanje

    results["similarity_score"] = similarity_scores # dodava nova kolona so presmetanite vrednosti na slichnost

    recommendations = results[results["similarity_score"] > 0] # gi zema samo delata koi imaat slichnost pogolema od 0


    # RANGIRANJE NA PREPORAKITE

    recommendations = recommendations.sort_values(
        by="similarity_score", # odreduva spored koja kolona ke se sortiraat rezultatite
        ascending=False # gi sortira rezultatite od najgolema kon najmala vrednost
    ).head(5) # gi zema prvite pet najvisoko rangirani literaturni dela


    # VRAKJANJE NA REZULTATITE

    return recommendations[
        ["title", "author", "genre", "similarity_score"]
    ] # gi vrakja samo kolonite koi sakame da mu gi prikazeme na korisnikot


# STARTUVANJE NA PROGRAMATA PREKU TERMINAL

if __name__ == "__main__": # ovoj del se izvrsuva samo koga direktno go startuvame recommender.py

    query = input("\nEnter your interests: ") # mu ovozmozuva na korisnikot da vnese interesi preku terminalot

    recommendations = recommend_books(query) # ja povikuva funkcijata za dobivanje preporaki

    if not query.strip(): # proveruva dali korisnikot vnese prazen tekst

        print("Please enter valid interests.")

    elif recommendations.empty: # proveruva dali sistemot pronashel relevantni rezultati

        print("\nNo relevant recommendations found.")

    else:

        print("\nTOP 5 RECOMMENDATIONS")

        print(recommendations.to_string(index=False)) # gi prikazuva preporakite bez indeksot na redovite