import pandas as pd

df = pd.read_csv("data/processed/books.csv", dtype={"code": str})

print("Books loaded:", len(df))

keyword = input("Enter a keyword: ").strip().lower() # input mu voozmozuva na korisnikot da vnese tekst, strio gi ostranuva nepotrebnite prazni mesta, lower gi pretvora bukvite vo mali , 

print("Search keyword:", keyword) # keyword promenliva vo koja go chuvame vneseniot zbor

if not keyword: # proveruva dali promenlivata e prazna
    print("Please enter a valid keyword.")
    exit() # go prekinuva izvrshuvanjeto na programta

results = df[df["text"].str.contains( # ja zema kolonata so literaturnite tekstovi, str.containts proveruva dali tekstot go sodrzi vneseniot zbor
    keyword, # zzborot shto go vnesuva korisnikot
    case=False, # ne pravi razlika megju golemi i mali bukvi
    regex=False, # go tretira vnesot kako obichen tekst
    na=False # gi ignorira vrednostite shto nedostasuvaat
)]

print("\nMatching books:", len(results))

if results.empty:
    print("No matching books found.")
else:
    print("\nSearch results:")
    print(results[["title", "author", "genre"]].head(10).to_string(index=False))