# LiteraMK-AI – Decision Log

## 1. Introduction

This document records the main technical and methodological decisions made during the development of LiteraMK-AI.

The purpose of the decision log is to explain the selected approaches, their rationale, advantages, limitations, and potential alternatives.

## 2. Decision Records

### Decision 1 – Project Scope

- **Decision:** Develop a recommendation system focused on Macedonian literature.
- **Alternative:** Develop a general book recommendation system.
- **Rationale:** A narrower domain provides a more manageable project scope and addresses the discovery of Macedonian literary works.
- **Outcome:** A specialized content-based literary recommendation system.

### Decision 2 – Content-Based Recommendation

- **Decision:** Use a content-based recommendation approach.
- **Alternatives:** Collaborative filtering and hybrid recommendation systems.
- **Rationale:** The available dataset contains literary texts and metadata but does not contain user ratings, reading histories, or interaction data.
- **Advantage:** Recommendations can be generated without collecting personal user information.
- **Limitation:** The system does not learn individual user preferences over time.

### Decision 3 – Python Programming Language

- **Decision:** Use Python as the main programming language.
- **Alternatives:** Java and JavaScript.
- **Rationale:** Python provides accessible libraries for data processing, machine learning, text analysis, and application development.
- **Outcome:** Integration of Pandas, Scikit-learn, and Streamlit within a single development environment.

### Decision 4 – Dataset Selection

- **Decision:** Use Macedonian literary texts and their associated metadata.
- **Rationale:** Full literary texts provide textual information that can be used to identify similarities between user queries and literary content.
- **Outcome:** A dataset containing literary titles, authors, genres, publication years, and textual content.
- **Limitation:** The dataset does not represent the entirety of Macedonian literature.

### Decision 5 – Data Cleaning and Validation

- **Decision:** Normalize text, remove unnecessary whitespace, and exclude records without reliable matching text files.
- **Rationale:** Consistent and complete data is necessary for reliable text processing.
- **Outcome:** A processed dataset containing 123 literary works and eight columns, with no missing values, duplicate codes, or empty texts.
- **Limitation:** Some literary works were excluded because their text files were missing or could not be reliably matched to the metadata.

### Decision 6 – CSV Data Storage

- **Decision:** Store the processed dataset in a CSV file.
- **Alternatives:** JSON, SQLite, and relational databases.
- **Rationale:** CSV provides a simple format that can be easily inspected and processed using Pandas.
- **Outcome:** Creation of `data/processed/books.csv`.
- **Limitation:** CSV may become less efficient when working with significantly larger datasets.

### Decision 7 – Baseline Keyword Search

- **Decision:** Implement a basic keyword search before developing the recommendation model.
- **Rationale:** A baseline provides a simple reference method for understanding the behavior of text-based retrieval.
- **Outcome:** A functional keyword search system.
- **Limitation:** Keyword matching does not provide advanced thematic understanding or similarity-based ranking.

A quantitative comparison between the baseline and the TF-IDF model has not yet been conducted.

### Decision 8 – TF-IDF Vectorization

- **Decision:** Use Term Frequency–Inverse Document Frequency (TF-IDF).
- **Alternatives:** Bag of Words, Word2Vec, and transformer-based text embeddings.
- **Rationale:** TF-IDF provides a computationally efficient and interpretable method for representing literary texts numerically.
- **Advantage:** It considers both word frequency within documents and word importance across the dataset.
- **Limitation:** It does not directly capture semantic meaning or contextual relationships between words.

### Decision 9 – Maximum Vocabulary Size

- **Decision:** Set `max_features=10000` in the TF-IDF vectorizer.
- **Alternatives:** Smaller vocabulary sizes or an unrestricted vocabulary.
- **Rationale:** Limiting the vocabulary provides a practical balance between textual representation and computational requirements.
- **Outcome:** A TF-IDF matrix with dimensions of 123 × 10,000.
- **Limitation:** Potentially useful vocabulary may be excluded.

The selected value is an initial configuration and has not been optimized through systematic parameter testing.

### Decision 10 – Cosine Similarity

- **Decision:** Use Cosine Similarity to calculate similarity between user queries and literary texts.
- **Alternatives:** Euclidean Distance and Jaccard Similarity.
- **Rationale:** Cosine Similarity is suitable for comparing high-dimensional text vectors because it measures their directional similarity rather than relying directly on vector magnitude.
- **Outcome:** A similarity score for each literary work in the dataset.
- **Limitation:** Mathematical similarity does not necessarily indicate complete thematic relevance.

### Decision 11 – Top Five Recommendations

- **Decision:** Return a maximum of five literary recommendations.
- **Alternatives:** Return three, ten, or all matching literary works.
- **Rationale:** A short recommendation list is easier for users to review and provides a consistent basis for evaluation.
- **Outcome:** Up to five literary works ranked by descending similarity score.
- **Limitation:** Relevant literary works outside the first five positions are not displayed.

### Decision 12 – Positive Similarity Filtering

- **Decision:** Exclude literary works with similarity scores equal to zero.
- **Rationale:** Works without detected lexical similarity should not be presented as matching recommendations.
- **Outcome:** The system returns no recommendations when the query has no matching vocabulary.
- **Limitation:** A positive similarity score alone does not guarantee thematic relevance.

### Decision 13 – Streamlit User Interface

- **Decision:** Use Streamlit to develop the application interface.
- **Alternatives:** Flask, Django, and a separate frontend application.
- **Rationale:** Streamlit allows the development of an interactive interface directly in Python without requiring a separate frontend implementation.
- **Outcome:** A functional browser-based recommendation interface.
- **Limitation:** Streamlit provides less flexibility for advanced interface customization than dedicated frontend frameworks.

### Decision 14 – Precision@5 Evaluation Metric

- **Decision:** Use Precision@5 as the primary recommendation relevance metric.
- **Alternatives:** Recall@5, Mean Average Precision, and Normalized Discounted Cumulative Gain.
- **Rationale:** The system returns up to five recommendations, making Precision@5 a suitable initial metric for measuring the proportion of relevant results.
- **Outcome:** An average Precision@5 of 96% across five selected evaluation queries.
- **Limitation:** Precision@5 does not measure how many relevant literary works were missed or distinguish between different positions within the top five results.

### Decision 15 – Binary Relevance Assessment

- **Decision:** Assign binary relevance labels of 0 or 1.
- **Alternatives:** Multi-level relevance ratings and independent expert assessments.
- **Rationale:** Binary labels provide a straightforward method for calculating Precision@5 during the initial evaluation.
- **Outcome:** 24 recommendations classified as relevant and one classified as not relevant.
- **Limitation:** The assessment is subjective, AI-assisted, and based on selected text excerpts rather than complete literary works.

A recommendation was considered relevant when it demonstrated a meaningful connection to at least one requested theme.

### Decision 16 – Response Time Measurement

- **Decision:** Use Python's `time.perf_counter()` to measure recommendation execution time.
- **Rationale:** This function provides a high-resolution timer suitable for measuring short execution intervals.
- **Outcome:** An average recommendation execution time of approximately 0.0456 seconds during the initial evaluation run.
- **Limitation:** The measurement excludes initial dataset loading and TF-IDF model fitting.

### Decision 17 – Local Application Development

- **Decision:** Develop and test the application locally before considering public deployment.
- **Rationale:** Local development simplifies debugging, testing, and verification of system functionality.
- **Outcome:** A functional local application developed using Visual Studio Code and a Python virtual environment.
- **Limitation:** Public accessibility, deployment performance, and production security have not yet been evaluated.

### Decision 18 – Responsible AI and Documentation

- **Decision:** Document system limitations, ethical considerations, evaluation results, AI assistance, and technical decisions.
- **Rationale:** Transparent documentation supports reproducibility, responsible AI development, and academic integrity.
- **Outcome:** Separate documentation files covering evaluation, responsible AI, error analysis, AI usage, and technical decisions.

## 3. Future Technical Decisions

Potential decisions for future development include:

- Introducing Macedonian-specific stemming or lemmatization.
- Investigating semantic text embeddings.
- Optimizing the TF-IDF vocabulary size.
- Introducing a minimum similarity threshold.
- Expanding the literary dataset.
- Comparing recommendation performance against the baseline.
- Conducting independent relevance assessments.
- Improving recommendation explainability.

These decisions remain open and have not yet been implemented.

## 4. Conclusion

The technical decisions made during the development of LiteraMK-AI prioritize simplicity, interpretability, computational efficiency, and suitability for the available Macedonian literary dataset.

The selected approaches provide a functional foundation for content-based literary recommendations while allowing future improvements in semantic understanding, evaluation reliability, and recommendation quality.