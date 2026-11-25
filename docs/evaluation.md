# LiteraMK-AI – System Evaluation

## 1. Evaluation Objective

The objective of this evaluation is to assess the effectiveness of the LiteraMK-AI recommendation system in recommending relevant Macedonian literary works based on user-defined keywords and thematic interests.

The evaluation focuses on recommendation relevance, ranking performance, and response time.

## 2. Evaluation Methodology

The recommendation system was evaluated using a processed dataset containing 123 Macedonian literary works.

The system uses TF-IDF vectorization and Cosine Similarity to calculate the similarity between the user query and the literary works in the dataset.

The evaluation process consisted of the following steps:

1. Preparation of five different thematic user queries.
2. Generation of the top five recommendations for each query.
3. Recording similarity scores and recommendation rankings.
4. Examination of text excerpts from the recommended literary works.
5. Assignment of binary relevance labels.
6. Calculation of Precision@5 and average response time.

A total of 25 recommendations were evaluated.

## 3. Test Queries

The following queries were selected to represent different literary interests:

| Query ID | User Query | Themes |
|---|---|---|
| 1 | љубов семејство традиција | Love, family, tradition |
| 2 | војна историја Македонија | War, history, Macedonia |
| 3 | природа живот среќа | Nature, life, happiness |
| 4 | пријателство детство | Friendship, childhood |
| 5 | слобода татковина | Freedom, homeland |

## 4. Relevance Criteria

Each recommendation was assigned a binary relevance label:

- **1 – Relevant:** The literary work demonstrates a meaningful thematic connection to at least one of the themes included in the user query.
- **0 – Not Relevant:** The literary work does not demonstrate a meaningful thematic connection, or the matching keywords appear only incidentally or in an unrelated context.

The relevance assessment was based on the examination of text excerpts extracted using the `review_relevance.py` script.

Keyword frequency was used as supporting information rather than as the sole criterion for determining relevance.

The relevance labels were developed through AI-assisted qualitative analysis and are subjective rather than independently validated expert annotations.

## 5. Evaluation Metric – Precision@5

Precision@5 measures the proportion of relevant recommendations among the first five results returned by the recommendation system.

**Formula:**

Precision@5 = Number of relevant recommendations in the top 5 / 5

The average Precision@5 is calculated by taking the mean of the Precision@5 values across all five test queries.

## 6. Evaluation Results

| Query ID | Relevant Recommendations | Total Recommendations | Precision@5 |
|---|---:|---:|---:|
| 1 | 5 | 5 | 100% |
| 2 | 5 | 5 | 100% |
| 3 | 4 | 5 | 80% |
| 4 | 5 | 5 | 100% |
| 5 | 5 | 5 | 100% |
| **Total / Average** | **24** | **25** | **96%** |

The recommendation system returned five literary works for each test query.

According to the assigned relevance labels, 24 out of 25 recommendations were classified as relevant.

**Average Precision@5 = (1.00 + 1.00 + 0.80 + 1.00 + 1.00) / 5 = 0.96**

The resulting average Precision@5 was 96% under the defined relevance criteria.

## 7. Response Time Evaluation

The execution time of the recommendation function was measured using Python's `time.perf_counter()` function.

| Query ID | Response Time (seconds) |
|---|---:|
| 1 | 0.0635 |
| 2 | 0.0373 |
| 3 | 0.0390 |
| 4 | 0.0405 |
| 5 | 0.0477 |
| **Average** | **0.0456** |

The average recommendation response time was approximately 45.6 milliseconds.

These measurements indicate that the recommendation function can return results quickly for the current dataset and testing environment.

The measurements exclude the initial loading of the dataset and the fitting of the TF-IDF vectorizer.

## 8. Functional Testing

Additional functional tests were performed to verify the behavior of the recommendation system.

| Test Case | Expected Behavior | Result |
|---|---|---|
| Valid Macedonian query | Return relevant ranked recommendations | Passed |
| Multiple keywords | Process multiple thematic keywords | Passed |
| Uppercase input | Process input regardless of capitalization | Passed |
| Empty input | Return no recommendations and display an appropriate message | Passed |
| Unknown keywords | Return no matching recommendations | Passed |
| Streamlit interface | Display recommendations to the user | Passed |

## 9. Evaluation Files

The following files were used during the evaluation process:

- `tests/evaluation_queries.csv` – Contains the five evaluation queries.
- `tests/evaluation_results.csv` – Contains recommendation rankings, similarity scores, and relevance labels.
- `src/evaluate.py` – Generates evaluation recommendations and measures response time.
- `src/review_relevance.py` – Extracts keyword occurrences and surrounding text excerpts.
- `src/calculate_metrics.py` – Records the assigned relevance labels and calculates Precision@5.

## 10. System Limitations

Although the initial evaluation produced promising results, several limitations were identified:

- The dataset contains only 123 Macedonian literary works.
- TF-IDF primarily relies on lexical similarity rather than deep semantic understanding.
- The system may not recognize synonyms or different grammatical forms of Macedonian words.
- Keywords with multiple meanings may lead to less relevant recommendations.
- The relevance review script uses substring matching, which may identify unrelated words containing the same sequence of characters.
- The evaluation includes only five test queries and 25 recommendations.
- Relevance labels are subjective and were assigned using selected text excerpts rather than complete literary works.
- A recommendation can be classified as relevant even if it matches only one of several requested themes.
- No independent expert or external user evaluation was conducted.

Therefore, the reported Precision@5 should be interpreted as a preliminary evaluation result rather than a general measure of system accuracy.

## 11. Future Improvements

Potential improvements to the recommendation system include:

- Expanding the Macedonian literary dataset.
- Applying Macedonian language stemming or lemmatization.
- Introducing semantic similarity methods and multilingual language models.
- Improving the recognition of synonyms and thematic relationships.
- Introducing more detailed relevance criteria.
- Evaluating the system using a larger and more diverse set of queries.
- Collecting independent relevance assessments and user feedback.

## 12. Conclusion

The initial evaluation demonstrates that LiteraMK-AI can generate ranked recommendations for Macedonian literary works based on user-defined thematic keywords.

Under the selected evaluation criteria, the system achieved an average Precision@5 of 96%, with 24 out of 25 recommendations classified as relevant and an average recommendation response time of approximately 0.0456 seconds.

The results demonstrate the potential of TF-IDF and Cosine Similarity as an initial approach to content-based literary recommendation.

However, further evaluation with a larger test set and independent relevance assessments is necessary to establish the reliability and generalizability of the system.