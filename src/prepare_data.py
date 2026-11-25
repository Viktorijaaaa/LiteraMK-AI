import pandas as pd
from pathlib import Path
import re

raw_folder = Path("data/raw") # lokacija na originalni podatoci
processed_folder = Path("data/processed") # lokacija na obraboteni podatoci

excel_file = next(raw_folder.glob("*.xls"))

df = pd.read_excel(excel_file, engine="xlrd") # Ja chita Excel tabelata so pomosh na engine "xlrd" za da se obezbedi kompatibilnost so postari verziji na Excel fajlovi.

text_files = sorted(raw_folder.glob("*.txt"))

print("Excel records:", len(df)) # go broi vkupniot broj na zapisi vo Excel tabelata
print("Text files:", len(text_files)) # go broi vkupniot broj na tekstualni fajlovi

def clean_text(text): 
    text = text.lower()
    text = re.sub(r"\s+", " ", text) # Gi zamenuva povekjekratnite prazni mesta, tabulatori i novi redovi so edno prazno mesto.
    text = text.strip() # Gi ostranuva praznite mesta od pochetokot i krajot na tekstot.

    return text
    
sample_text = "  МАКЕДОНСКА\n\nЛИТЕРАТУРА   "

print("\nOriginal text:", repr(sample_text))
print("Cleaned text:", clean_text(sample_text))

files_by_code = {}

for file in text_files:
    match = re.match(r"\d+", file.name)

    if match:
        code = int(match.group())

        if code not in files_by_code:
            files_by_code[code] = []

        files_by_code[code].append(file)

print("\nSpecial Excel records:")

for index, row in df.iterrows(): # pominuva niz sekoj red od Excel tabelata
    if str(row["Код"]).strip() in ["6", "94", "95", "94/95"]:
        print(row.to_string()) # gi prikazhuva site vrednosti od toj red
        print()

print("\nSpecial text files:")

for code in [6, 94, 95]:
    print("Code:", code)

    for file in files_by_code.get(code, []): # gi pronaogja fajlovite za odreden kod
        print(file.name) # go prikazuva imeto na fajlot

books = []
skipped_books = [] # gi evidentira izostavenite podatoci

for index, row in df.iterrows(): # pominuva niz site redpvi od excel
    book_code = str(row["Код"]).strip()

    if book_code == "6":
        skipped_books.append(book_code)
        continue

    codes = re.findall(r"\d+", book_code) # gi izdvojuva numerickite kodovi

    matched_files = [] # lista na soodvetni tekstualni fajlovi

    for code in codes:
        matched_files.extend(
            files_by_code.get(int(code), [])
        )

    if not matched_files: # proveruva dali nedostasuva tekstualen fajl
        skipped_books.append(book_code)
        continue

    books.append({   # dodava nov zapis so podatocite za deloto
        "code": book_code,
        "title": row["Наслов"],
        "author": row["Автор"],
        "genre": row["Жанр"],
        "year": row["Година на издавање"],
        "files": matched_files
    })

print("\nDATA MATCHING RESULTS")
print("Matched records:", len(books))
print("Skipped records:", len(skipped_books))
print("Skipped codes:", skipped_books)

for book in books:
    full_text = "" # kreira prazen string za da gi spoi site tekstualni fajlovi

    for file in book["files"]:
        content = file.read_text(encoding="utf-8")
        full_text += content + "\n" # spoi gi site tekstualni fajlovi vo eden string, dodava nov red pomegju niv

    book["text"] = clean_text(full_text) # gi cisti znacite od tekstot
    book["word_count"] = len(book["text"].split()) # split go deli tekstot na zborovi, len gi broi zborovite

    book["source_files"] = "; ".join(
        file.name for file in book["files"]
    )

    del book["files"]

    books_df = pd.DataFrame(books) # ja pretvora listata vo tabela

processed_folder.mkdir(parents=True, exist_ok=True)

output_file = processed_folder / "books.csv"

books_df.to_csv( # ja zacuvuva tabelata vo CSV format so UTF-8 kodiranje i bez indeks kolona
    output_file,
    index=False, # ne dodava nepotrebni koloni so indeksi
    encoding="utf-8-sig" # go obezbeduva pravilno prikazhuvanje na kirilicata vo Excel
)

print("\nPROCESSED DATASET")
print("Dataset shape:", books_df.shape)
print("Columns:", books_df.columns.tolist())
print("Saved to:", output_file)

print("\nFirst 5 processed records:")
print(books_df[["title", "author", "genre", "word_count"]].head())