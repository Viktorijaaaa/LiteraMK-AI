import pandas as pd  # Ja vkluchuva bibliotekata za rabota so podatoci.
from pathlib import Path  # Rabota so folderi i fajlovi.
import re # vgradena python bib za regular expressions 

data_folder = Path("data/raw")  # Kade se naogja datasetot.

excel_file = next(data_folder.glob("*.xls"))  # Go pronagja Excel fajlot.
df = pd.read_excel(excel_file)  # Ja chita Excel tabelata.

print("Dataset file:", excel_file.name)
print("Dataset shape:", df.shape)  # Broj na redovi i koloni.
print("Columns:", df.columns.tolist())  # Iminja na kolonite.

print("\nFirst 5 rows:")
print(df.head())  # Gi prikazhuva prvite pet redovi.

print("\nMissing values:") # Proveruva koi vrednosti nedostasuvaat.
print(df.isnull().sum()) # Gi broi praznite vrednosti vo sekoja kolona.

print("\nDuplicate rows:") # Proveruva dali ima duplikati vo datasetot.
print(df.duplicated().sum()) # Gi broi duplikatite vo datasetot.

print("\nGenre distribution:")
print(df["Жанр"].value_counts()) # Gi prikazhuva kolku ima od sekoja vrednost vo kolonata "Жанр".

print("\nFirst 15 book codes:") 
print(df[["Код", "Наслов"]].head(15)) # gi izdvojuva samo kodot i naslovot, head 15 gi prikazuva prvite 15 zapisi

text_files = sorted(data_folder.glob("*.txt")) # gi pronaogja site tekstualni fajlovi, sorted gi podreduva fajlovite po ime

print("\nNumber of text files:", len(text_files)) # go broi vkupniot broj na tekstualni fajlovi

print("\nFirst 15 text filenames:")

for file in text_files[:15]: # gi zema prvite 15 fajlovi, for file in - pominuva niz sekoj od izbranite fajlovi
    print(file.name) # go prikazuva imeto na fajlot


files_by_code = {} # kreira prazen dictionary

for file in text_files:  # pominuva niz site 128 fajlovi
    match = re.match(r"\d+", file.name) # go bara brojot na pochetokot od imeto

    if match:  # proveruva dali e pronajden broj
        code = int(match.group()) # go pretvora pronajdeniot string vo integer

        if code not in files_by_code:
            files_by_code[code] = []  # kreira prazen list za toj kod

        files_by_code[code].append(file.name) # gi dodava iminjata na fajlovite vo listata za toj kod
    else:
        print("File without code:", file.name)

excel_codes = set()

for value in df["Код"]:
    numbers = re.findall(r"\d+", str(value))

    for number in numbers:
        excel_codes.add(int(number))
text_codes = set(files_by_code.keys())

print("\nMatching codes:", len(excel_codes & text_codes))

print("\nExcel codes without text files:")
print(sorted(excel_codes - text_codes))

print("\nText codes without Excel records:")
print(sorted(text_codes - excel_codes))

print("\nCodes with multiple text files:")

for code, files in files_by_code.items():
    if len(files) > 1:
        print(code, files)