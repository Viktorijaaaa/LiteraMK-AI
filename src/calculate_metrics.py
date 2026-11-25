import pandas as pd

# Go citame fajlot so rezultatite od evaluacijata
df = pd.read_csv("tests/evaluation_results.csv")

# Racno odredeni ocenki za relevantnost
# 1 oznacuva relevantna preporaka
# 0 oznacuva nerelevantna preporaka

relevance_labels = {
    "љубов семејство традиција": [1, 1, 1, 1, 1],
    "војна историја Македонија": [1, 1, 1, 1, 1],
    "природа живот среќа": [1, 1, 1, 1, 0],
    "пријателство детство": [1, 1, 1, 1, 1],
    "слобода татковина": [1, 1, 1, 1, 1]
}

# Gi vnesuvame ocenkite spored query i rank
for query, labels in relevance_labels.items():
    for rank, label in enumerate(labels, start=1):
        df.loc[
            (df["query"] == query) &
            (df["rank"] == rank),
            "relevant"
        ] = label

# Proveruvame dali site 25 preporaki se oceneti
if len(df) != 25 or df["relevant"].isna().any():
    raise ValueError("Evaluation results are incomplete.")

# Gi pretvorame ocenkite vo celi broevi
df["relevant"] = df["relevant"].astype(int)

# Gi zacuvuvame rezultatite so ocenkite
df.to_csv(
    "tests/evaluation_results.csv",
    index=False,
    encoding="utf-8-sig"
)

# Presmetuvame Precision@5 za sekoj query
precision_scores = df.groupby("query")["relevant"].sum() / 5

print("\n===== EVALUATION RESULTS =====")

# Gi prikazuvame rezultatite za sekoj query
for query, precision in precision_scores.items():
    print(f"\nQuery: {query}")
    print(f"Precision@5: {precision:.2%}")

# Presmetuvame prosecna Precision@5
average_precision = precision_scores.mean()

# Presmetuvame broj na relevantni preporaki
total_relevant = df["relevant"].sum()
total_recommendations = len(df)

print("\n===== FINAL RESULTS =====")

print("Total recommendations:", total_recommendations)
print("Relevant recommendations:", total_relevant)
print(f"Average Precision@5: {average_precision:.2%}")