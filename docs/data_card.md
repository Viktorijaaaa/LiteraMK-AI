# LiteraMK-AI – Data Card

## 1. Dataset Overview

The LiteraMK-AI dataset contains Macedonian literary works and their associated metadata. It is used to develop a content-based recommendation system that identifies literary works according to user-defined thematic interests.

The dataset includes poetry, prose, drama, literary criticism, and mixed literary genres.

## 2. Data Source

The original dataset consists of:

- 128 literary text files in TXT format.
- One Excel metadata file containing 134 records.
- Metadata describing literary titles, authors, genres, publishers, and publication years.

The exact original source, ownership, and licensing conditions require further verification before public distribution.

The original files are stored locally in `data/raw/`.

## 3. Intended Use

The dataset is intended for:

- Macedonian literary text analysis.
- Natural Language Processing.
- Content-based literary recommendations.
- TF-IDF vectorization.
- Cosine Similarity calculations.
- Academic research and educational purposes.

The dataset is not intended to provide a complete representation of Macedonian literature or authoritative literary classifications.

## 4. Dataset Statistics

| Parameter | Value |
|---|---:|
| Original metadata records | 134 |
| Original text files | 128 |
| Processed literary works | 123 |
| Excluded metadata records | 11 |
| Processed dataset columns | 8 |
| Total word count | 5,869,232 |
| Minimum document word count | 3,227 |
| Maximum document word count | 421,888 |
| Missing values | 0 |
| Duplicate codes | 0 |
| Empty texts | 0 |

The processed dataset is stored in `data/processed/books.csv`.

## 5. Original Metadata Structure

| Original Field | Description |
|---|---|
| Код | Literary work identifier |
| Наслов | Title of the literary work |
| Автор | Author |
| Издавачка куќа | Publishing house |
| Година на издавање | Publication year |
| Жанр | Literary genre |
| Оригинално издание | Original edition information |

The original metadata contains seven columns. Not all original metadata fields are required by the current recommendation model.

## 6. Data Dictionary

The processed dataset contains the following eight fields:

| Field | Data Type | Description |
|---|---|---|
| code | String | Unique identifier of the literary work |
| title | String | Title of the literary work |
| author | String | Name of the author |
| genre | String | Literary genre |
| year | Integer | Publication year |
| text | String | Cleaned textual content |
| word_count | Integer | Number of words in the processed text |
| source_files | String | Associated original text file names |

The `text` field is the primary input used by the TF-IDF recommendation model.

The title, author, and genre fields are used to display recommendation results.

## 7. Genre Distribution

| Genre | Number of Literary Works | Percentage |
|---|---:|---:|
| Poetry | 57 | 46.34% |
| Prose | 54 | 43.90% |
| Drama | 8 | 6.50% |
| Literary Criticism | 3 | 2.44% |
| Prose / Poetry | 1 | 0.81% |
| **Total** | **123** | **100%** |

Percentages are rounded.

The dataset contains substantially more poetry and prose than drama and literary criticism. This imbalance may influence the diversity of recommendation results.

## 8. Data Preprocessing

The following preprocessing steps were performed:

1. Inspection of the original Excel metadata.
2. Inspection of the original literary text files.
3. Matching literary texts with their corresponding metadata.
4. Identification of missing or inconsistent records.
5. Exclusion of records without reliable text matches.
6. Conversion of literary texts to lowercase.
7. Normalization of whitespace using regular expressions.
8. Removal of unnecessary leading and trailing whitespace.
9. Calculation of document word counts.
10. Export of the processed dataset to CSV.
11. Validation of the final dataset.

The preprocessing implementation is available in `src/prepare_data.py`.

## 9. Data Quality and Identified Problems

During dataset preparation, several inconsistencies were identified:

- Some metadata records did not have corresponding text files.
- Some text files could not be reliably matched to the metadata.
- Certain literary works were represented by multiple text files.
- Some original metadata fields contained missing values.

Records without reliable text matches were excluded to reduce the risk of incorrect associations.

Multiple text files were combined where they represented a single corresponding metadata record.

The final processed dataset contains 123 literary works.

## 10. Data Validation

The processed dataset was validated using `src/validate_data.py`.

The following checks were performed:

| Validation Check | Actual Result | Status |
|---|---:|---|
| Dataset dimensions | 123 × 8 | Passed |
| Missing values | 0 | Passed |
| Duplicate codes | 0 | Passed |
| Empty texts | 0 | Passed |
| Genre distribution | 123 works | Passed |
| Total word count | 5,869,232 | Passed |

These checks confirm the structural completeness of the processed dataset. They do not independently verify the literary accuracy of every metadata record.

## 11. Dataset Usage in the AI Model

The recommendation system uses the processed literary texts to generate numerical document representations.

The following configuration is used:

- Vectorization method: TF-IDF.
- Number of documents: 123.
- Maximum vocabulary size: 10,000.
- Generated matrix shape: (123, 10000).
- Similarity method: Cosine Similarity.
- Maximum number of recommendations: 5.

The system compares user queries with literary document vectors and ranks literary works according to their similarity scores.

## 12. Privacy and Ethical Considerations

The current recommendation system does not require user registration, personal profiles, or reading histories.

However, the following considerations remain relevant:

- Copyright and intellectual property rights.
- Permission to redistribute literary texts.
- Accurate attribution of literary authors.
- Fair representation of different literary genres.
- Transparency regarding recommendation limitations.
- Responsible use of literary content.

The literary dataset is excluded from the public Git repository until its redistribution rights are verified.

## 13. Dataset Limitations

- Limited number of literary works.
- Unequal representation of literary genres.
- Incomplete coverage of Macedonian literature.
- Significant differences in document length.
- Possible inconsistencies in original metadata.
- Absence of manually annotated thematic labels.
- Absence of user ratings and reading preferences.
- No Macedonian-specific stemming or lemmatization.
- Unverified copyright and redistribution conditions.

These limitations may influence recommendation relevance, diversity, and reliability.

## 14. Future Improvements

Potential improvements include:

- Expanding the dataset with additional Macedonian literary works.
- Improving metadata consistency.
- Introducing manually verified thematic labels.
- Improving genre balance.
- Applying Macedonian-specific language preprocessing.
- Investigating document segmentation.
- Verifying dataset ownership and licensing conditions.

## 15. Supporting Evidence

Dataset preparation and validation are supported by the following project files:

- `src/inspect_data.py`
- `src/inspect_text.py`
- `src/prepare_data.py`
- `src/validate_data.py`
- `data/processed/books.csv`
- `docs/evidence/01_data_validation.png`

## 16. Conclusion

The LiteraMK-AI dataset provides a structured foundation for developing and evaluating a Macedonian literature recommendation system.

Data preprocessing and validation have produced a dataset containing 123 literary works with no missing values, duplicate codes, or empty texts.

Although the dataset is suitable for the current prototype, further improvements in literary coverage, metadata verification, thematic annotation, and licensing verification are necessary.