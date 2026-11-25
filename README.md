# LiteraMK-AI

## Macedonian Literature Recommendation System Based on Thematic Interests

**University:** South East European University (SEEU)  
**Faculty:** Faculty of Contemporary Sciences and Technologies  
**Study Program:** Computer Science  
**Course:** Introduction to Artificial Intelligence  
**Student:** Viktorija Ilievska  
**Academic Year:** 2026/2027

---

## 1. Project Overview

LiteraMK-AI is an artificial intelligence-based recommendation system designed to help users discover Macedonian literary works according to their thematic interests.

The system allows users to enter keywords describing their preferred literary themes and generates a ranked list of relevant Macedonian literary works.

The recommendation approach is based on Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity.

## 2. Problem Statement

Finding literary works that match specific thematic interests can be challenging, especially when available search systems primarily rely on titles, authors, or genres.

LiteraMK-AI addresses this problem by analyzing the textual content of Macedonian literary works and recommending works based on their lexical similarity to user-defined thematic keywords.

## 3. Project Objectives

- Develop a content-based recommendation system for Macedonian literature.
- Prepare and validate a structured literary dataset.
- Implement a baseline keyword search method.
- Apply TF-IDF for numerical text representation.
- Use Cosine Similarity to calculate relevance scores.
- Generate ranked literary recommendations.
- Develop an interactive and user-friendly interface.
- Evaluate recommendation relevance and response time.
- Document system limitations and responsible AI considerations.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing and analysis |
| Scikit-learn | TF-IDF and Cosine Similarity |
| Streamlit | Interactive user interface |
| Regular Expressions | Text cleaning and keyword inspection |
| CSV | Structured data storage |
| Visual Studio Code | Development environment |
| Python Virtual Environment | Dependency management |

## 5. Dataset

The original dataset consists of Macedonian literary text files and an Excel metadata file containing information about literary works.

Following data inspection, preprocessing, metadata matching, and validation, the processed dataset contains 123 literary works.

### Dataset Statistics

| Parameter | Value |
|---|---:|
| Original metadata records | 134 |
| Original text files | 128 |
| Processed literary works | 123 |
| Dataset columns | 8 |
| Total word count | 5,869,232 |
| Missing values | 0 |
| Duplicate codes | 0 |
| Empty texts | 0 |

### Genre Distribution

| Genre | Number of Works |
|---|---:|
| Poetry | 57 |
| Prose | 54 |
| Drama | 8 |
| Literary Criticism | 3 |
| Prose / Poetry | 1 |
| **Total** | **123** |

### Dataset Attributes

- `code` – Unique literary work identifier.
- `title` – Title of the literary work.
- `author` – Author of the literary work.
- `genre` – Literary genre.
- `year` – Publication year.
- `text` – Processed literary text.
- `word_count` – Number of words.
- `source_files` – Associated original text files.

## 6. Data Preprocessing

The preprocessing process includes:

1. Inspection of the original metadata and text files.
2. Matching literary texts with their corresponding metadata.
3. Exclusion of records without reliable text matches.
4. Conversion of text to lowercase.
5. Removal of unnecessary whitespace.
6. Calculation of word counts.
7. Export of the processed dataset to CSV.
8. Validation of the generated dataset.

The processed dataset is stored in `data/processed/books.csv`.

## 7. Recommendation Methodology

### 7.1 Baseline Keyword Search

The baseline model searches literary texts for a user-defined keyword.

For example, searching for the Macedonian keyword "љубов" returns 92 matching literary works.

This approach provides a simple reference method for text retrieval.

### 7.2 TF-IDF Vectorization

Term Frequency–Inverse Document Frequency (TF-IDF) converts textual documents into numerical vectors based on word frequency and importance across the dataset.

The current implementation uses a maximum vocabulary size of 10,000 features.

The generated TF-IDF matrix has the following dimensions:

- Number of documents: 123
- Number of features: 10,000
- Matrix shape: (123, 10000)

### 7.3 Cosine Similarity

Cosine Similarity measures the directional similarity between the user query vector and the literary document vectors.

Each literary work receives a similarity score.

Works with positive similarity scores are ranked in descending order, and the five highest-ranked results are returned.

### 7.4 Recommendation Workflow

1. Load the processed literary dataset.
2. Fit the TF-IDF vectorizer.
3. Generate document vectors.
4. Receive thematic keywords from the user.
5. Transform the query into a numerical vector.
6. Calculate Cosine Similarity.
7. Filter results with zero similarity.
8. Rank matching literary works.
9. Display up to five recommendations.

## 8. Application Features

- Macedonian-language thematic keyword input.
- Support for multiple keywords.
- Case-insensitive input processing.
- Content-based literary recommendations.
- Ranked recommendation results.
- Display of titles, authors, genres, and similarity scores.
- Empty input handling.
- Unknown keyword handling.
- Interactive Streamlit interface.

LiteraMK-AI/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── books.csv
│
├── docs/
│   ├── evidence/
│   ├── ai_usage_log.md
│   ├── architecture.md
│   ├── data_card.md
│   ├── decision_log.md
│   ├── error_analysis.md
│   ├── evaluation.md
│   ├── responsible_ai.md
│   └── source_list.md
│
├── src/
│   ├── baseline.py
│   ├── calculate_metrics.py
│   ├── evaluate.py
│   ├── inspect_data.py
│   ├── inspect_text.py
│   ├── prepare_data.py
│   ├── recommender.py
│   ├── review_relevance.py
│   └── validate_data.py
│
├── tests/
│   ├── evaluation_queries.csv
│   └── evaluation_results.csv
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt


## 10. Installation and Execution

### 10.1 Create a Virtual Environment

Open a terminal in the project directory.

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 10.2 Install Required Libraries

```powershell
pip install pandas scikit-learn streamlit xlrd
```

### 10.3 Prepare the Dataset

If the processed dataset is unavailable, the original dataset files must first be placed in the appropriate raw data directory.

Run:

```powershell
python src/prepare_data.py
```

### 10.4 Validate the Dataset

```powershell
python src/validate_data.py
```

### 10.5 Run the Baseline Model

```powershell
python src/baseline.py
```

### 10.6 Run the Recommendation Model

```powershell
python src/recommender.py
```

### 10.7 Launch the Streamlit Application

```powershell
streamlit run app.py
```

The application will open in the default web browser.

## 11. Example User Queries

Users can enter thematic keywords such as:

- љубов семејство традиција
- војна историја Македонија
- природа живот среќа
- пријателство детство
- слобода татковина

The system generates up to five ranked literary recommendations based on the entered keywords.

## 12. Evaluation Results

The initial evaluation was conducted using five thematic queries and 25 recommendations.

Precision@5 was selected as the primary recommendation relevance metric.

| Evaluation Query | Precision@5 |
|---|---:|
| љубов семејство традиција | 100% |
| војна историја Македонија | 100% |
| природа живот среќа | 80% |
| пријателство детство | 100% |
| слобода татковина | 100% |
| **Average Precision@5** | **96%** |

### Performance Summary

| Metric | Result |
|---|---:|
| Evaluation queries | 5 |
| Total recommendations | 25 |
| Recommendations classified as relevant | 24 |
| Recommendations classified as not relevant | 1 |
| Average Precision@5 | 96% |
| Average recommendation execution time | 0.0456 seconds |

The execution time was measured during the initial evaluation run and excludes dataset loading and TF-IDF model fitting.

The relevance labels were assigned through AI-assisted qualitative analysis of selected text excerpts. A recommendation was considered relevant if it demonstrated a meaningful connection to at least one requested theme.

The reported results represent a preliminary evaluation rather than a general measure of system accuracy.

## 13. Evaluation Execution

To generate evaluation recommendations:

```powershell
python src/evaluate.py
```

To calculate Precision@5:

```powershell
python src/calculate_metrics.py
```

**Important:** Running `evaluate.py` regenerates the evaluation results CSV and overwrites existing relevance labels. Relevance assessments must be checked before recalculating metrics, particularly if the dataset, queries, or recommendation rankings have changed.

## 14. System Limitations

- Limited dataset size and literary coverage.
- Unequal representation of literary genres.
- Dependence on lexical similarity.
- Limited understanding of semantic relationships.
- Absence of Macedonian-specific stemming and lemmatization.
- No personalized user profiles.
- Limited evaluation query set.
- Subjective and AI-assisted relevance assessments.
- No independent expert evaluation.
- No quantitative performance comparison against the baseline model.

## 15. Responsible AI

LiteraMK-AI considers privacy, fairness, transparency, explainability, reliability, and human oversight.

The current application does not require user registration or personal information.

Similarity scores are mathematical indicators of lexical similarity and should not be interpreted as probabilities or guarantees of thematic relevance.

Dataset copyright and licensing conditions must be verified before public distribution or deployment.

Further information is available in `docs/responsible_ai.md`.

## 16. Project Documentation

Additional documentation is available in the following files:

- [Data Card and Data Dictionary](docs/data_card.md)
- [Source List](docs/source_list.md)
- [System Architecture](docs/architecture.md)
- [System Evaluation](docs/evaluation.md)
- [Responsible AI](docs/responsible_ai.md)
- [Error Analysis](docs/error_analysis.md)
- [AI Usage Log](docs/ai_usage_log.md)
- [Decision Log](docs/decision_log.md)
- [Project Evidence](docs/evidence/)

## 17. Future Improvements

- Expand the Macedonian literary dataset.
- Introduce Macedonian-specific language preprocessing.
- Investigate semantic text embeddings.
- Improve thematic and contextual understanding.
- Optimize recommendation model parameters.
- Compare the recommendation model against the baseline.
- Expand the evaluation query set.
- Conduct independent human relevance assessments.
- Improve recommendation explainability.
- Collect user feedback.

## 18. AI Assistance Disclosure

OpenAI ChatGPT was used during project development to provide substantial assistance with technical explanations, code generation, debugging, evaluation design, relevance assessment, and documentation drafting.

The student executed the implementation, tested the application, examined the generated results, and collected project evidence.

Further details are documented in `docs/ai_usage_log.md`.

## 19. Current Project Status

The project currently provides a functional local prototype of a Macedonian literature recommendation system, including data preprocessing, a baseline model, TF-IDF recommendations, an interactive interface, and preliminary evaluation.

Further development and validation will be conducted according to the course requirements.

## 20. Conclusion

LiteraMK-AI demonstrates the application of Natural Language Processing and content-based recommendation techniques to Macedonian literature.

The project provides a functional foundation for thematic literary discovery and demonstrates the practical application of TF-IDF, Cosine Similarity, data preprocessing, recommendation ranking, and system evaluation.