import pandas as pd

df = pd.read_csv("data/processed/books.csv", dtype={"code": str}) # dtype code:str - gi zachuvuva kodovite kako tekst vklucuvajki go 94/95

print("DATASET VALIDATION")

print("\nDataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum()) # proveruva dali nedostasuvaat vrednosti

print("\nDuplicate codes:")
print(df["code"].duplicated().sum()) # proveruva dali ima povtoreni kodovi

print("\nEmpty texts:")
print(df["text"].fillna("").str.strip().eq("").sum()) # 	Gi zamenuva vrednostite shto nedostasuvaat so prazen tekst za potrebite na proverkata, str.strip eq proveruva dali tekstot e prazen

print("\nGenre distribution:")
print(df["genre"].value_counts()) # go broi brojot na zapisi vo sekoj zhanr

print("\nTotal word count:")
print(df["word_count"].sum()) # go presmetuva vkupniot broj na zborovi

print("\nMinimum word count:")
print(df["word_count"].min()) # gi pronaogja najkratkiot tekst spored brojot na zborovi

print("\nMaximum word count:")
print(df["word_count"].max()) # go pronaogja najdolgiot tekst spored brojot na zborovi