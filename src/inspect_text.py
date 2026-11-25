from pathlib import Path

data_folder = Path("data/raw")

text_files = sorted(data_folder.glob("*.txt"))

sample_file = text_files[0] # go zema prviot tekstualen fajl od listata , sample)file.name - go prikazuva imeto na fajlot

print("File name:", sample_file.name)

text = sample_file.read_text(encoding="utf-8") # odreduva kako da se prochitaat znacite,vklucuvajki ja kirilicata

print("\nNumber of characters:", len(text)) # go broi vkupniot broj na znaci vo tekstot

print("\nText preview:")
print(text[:500]) # gi prikazuva samo prvite 500 znaci

successful = 0  # brojach na uspesno procitani fajlovi
failed = 0 # brojach na neuspeshno procitani fajlovi
empty = 0 # brojach na prazni fajlovi

for file in text_files: # pominuva niz site tekstualni fajlovi
    try: # se obiduva da go izvrshi kodot
        content = file.read_text(encoding="utf-8")

        successful += 1 # go zgolemuva brojachot na uspesno procitani fajlovi

        if not content.strip(): # gi ostranuva praznite mesta od pochetokot i krajot
            empty += 1
            print("Empty file:", file.name)

    except UnicodeDecodeError: # ja obrabotuva greshkata pri citanje na tekstot
        failed += 1
        print("Encoding error:", file.name)

print("\nTEXT FILE VALIDATION")
print("Total files:", len(text_files))
print("Successfully read:", successful)
print("Failed to read:", failed)
print("Empty files:", empty)