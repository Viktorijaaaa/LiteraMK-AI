import pandas as pd # ni ovozmozuva rabota so tabelarni podatoci
import re # ni ovozmozuva prebaruvanje niz tekstot


# VCITUVANJE NA PODATOCITE

books_df = pd.read_csv("data/processed/books.csv") # go vcituva obraboteniot dataset so literaturni dela

results_df = pd.read_csv("tests/evaluation_results.csv") # gi vcituva rezultatite od testiranjata


# IZBOR NA VTORIOT TEST VNOS

query = "слобода татковина"

keywords = query.split()
recommendations = results_df[results_df["query"] == query] # gi zema samo preporakite za izbraniot test vnes


# PROVERKA NA SODRZINATA NA DELATA

for _, recommendation in recommendations.iterrows(): # pominuva niz sekoe preporacano literaturno delo

    title = recommendation["title"] # go zema naslovot na deloto

    author = recommendation["author"] # go zema avtorot na deloto

    book = books_df[
        (books_df["title"] == title) &
        (books_df["author"] == author)
    ] # go pronagja deloto vo originalniot obraboten dataset

    if book.empty: # proveruva dali deloto e pronajdeno
        continue

    text = book.iloc[0]["text"] # ja zema tekstualnata sodrzina na deloto

    print("\n" + "=" * 70)

    print("Title:", title)

    print("Author:", author)


    # PREBARUVANJE NA KLUCNITE ZBOROVI

    for keyword in keywords: # pominuva niz sekoj klucen zbor

        matches = list(re.finditer(re.escape(keyword), text, re.IGNORECASE)) # gi pronagja pojavuvanjata na zborot vo tekstot

        print("\nKeyword:", keyword)

        print("Number of matches:", len(matches)) # go prikazuva brojot na pronajdeni pojavuvanja


        # PRIKAZUVANJE NA DELOVI OD TEKSTOT

        for match in matches[:3]: # gi zema prvite tri pojavuvanja na zborot

            start = max(0, match.start() - 150) # odreduva pocetna pozicija pred pronajdeniot zbor

            end = min(len(text), match.end() + 150) # odreduva krajna pozicija po pronajdeniot zbor

            context = text[start:end] # go izdvojuva delot od tekstot okolu zborot

            print("Context:", context)