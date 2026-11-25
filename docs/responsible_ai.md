# LiteraMK-AI – Responsible AI and Ethical Considerations

## 1. Introduction

Responsible AI refers to the development and use of artificial intelligence systems in an ethical, transparent, fair, and reliable manner.

LiteraMK-AI is a content-based recommendation system designed to help users discover Macedonian literary works based on their thematic interests.

## 2. Data Privacy

The recommendation system uses a dataset containing 123 Macedonian literary works and their associated metadata.

The current implementation:

- Does not require user registration or authentication.
- Does not request personal information.
- Does not maintain individual user profiles.
- Generates recommendations based on the keywords entered by the user.
- Processes recommendations locally in the current development environment.

If the system is deployed publicly in the future, additional privacy and security considerations will be necessary.

## 3. Fairness and Bias

The recommendation system may contain biases related to the composition of the dataset and the selected recommendation algorithm.

Potential sources of bias include:

- Unequal representation of literary genres.
- Unequal representation of authors.
- Differences in the length of literary works.
- Limited coverage of Macedonian literature.
- Differences in vocabulary and writing styles.

The TF-IDF algorithm may favor literary works containing vocabulary similar to the user query, while overlooking works that express similar themes using different words.

Expanding and balancing the dataset could help reduce these limitations.

## 4. Transparency and Explainability

LiteraMK-AI uses TF-IDF vectorization and Cosine Similarity to generate recommendations.

The recommendation process consists of the following steps:

1. The user enters thematic keywords.
2. The input is transformed into a TF-IDF vector.
3. Cosine Similarity is calculated between the query vector and the literary work vectors.
4. Literary works are ranked according to their similarity scores.
5. The five highest-ranked works with positive similarity scores are returned.

The recommendation results include the title, author, genre, and similarity score.

The similarity score represents mathematical similarity between the query and the literary text. It does not represent a probability or guarantee of user satisfaction.

## 5. Human Oversight

The system is designed to support users in discovering literary works rather than making decisions on their behalf.

Users remain responsible for selecting which literary works they wish to read.

Human judgment is also important during the evaluation process, because keyword similarity alone cannot determine whether a literary work is thematically relevant.

The current relevance evaluation uses AI-assisted qualitative assessments of selected text excerpts. These assessments have not been independently validated by literary experts.

## 6. Reliability and Safety

The system was tested using valid queries, multiple keywords, uppercase input, empty input, and unknown keywords.

The recommendation system handles empty queries and queries without matching vocabulary by returning no recommendations.

However, the system cannot guarantee that every recommended literary work will fully satisfy the user's interests.

The reported average Precision@5 of 96% represents preliminary performance on five selected test queries under a broad relevance criterion.

## 7. Copyright and Intellectual Property

Literary works may be protected by copyright and intellectual property regulations.

The dataset is used for academic research and recommendation system development.

The current user interface presents recommendation information rather than displaying complete literary texts.

Before publicly distributing the dataset or deploying the application, the copyright status, licensing conditions, and permissions associated with the literary works must be verified.

## 8. Ethical Use of AI During Development

AI-assisted tools were used during the development process to support:

- Understanding programming concepts.
- Code development and debugging.
- Explanation of machine learning methods.
- Evaluation planning and interpretation.
- Preparation of project documentation.

AI assistance should be documented in the project's AI Usage Log.

The student remains responsible for understanding, reviewing, testing, and validating the implemented system and its documentation.

## 9. Future Responsible AI Improvements

Future improvements may include:

- Expanding and balancing the literary dataset.
- Improving recommendation explainability.
- Introducing independent relevance assessments.
- Collecting voluntary user feedback.
- Improving Macedonian language processing.
- Verifying dataset licensing before public distribution.
- Conducting additional fairness and reliability evaluations.

## 10. Conclusion

LiteraMK-AI represents an initial approach to responsible AI development in the domain of Macedonian literary recommendations.

The system aims to provide transparent and useful recommendations while recognizing its limitations regarding dataset coverage, thematic understanding, fairness, and evaluation reliability.

Further development should continue to prioritize transparency, human oversight, privacy, fairness, and responsible use of literary data.