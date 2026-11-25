# LiteraMK-AI – Error Analysis

## 1. Objective

The objective of error analysis is to identify incorrect or less relevant recommendations, understand their potential causes, and identify opportunities for improving the recommendation system.

## 2. Identified Error

During the initial evaluation, 24 out of 25 recommendations were classified as relevant under the selected relevance criteria.

One recommendation was classified as not relevant.

| Parameter | Value |
|---|---|
| User Query | природа живот среќа |
| Recommended Work | Кодот на македонската книжевна историја |
| Author | Митрев Димитар |
| Genre | Проза |
| Recommendation Rank | 5 |
| Similarity Score | 0.0114759 |
| Relevance Label | 0 |

The literary work primarily focuses on Macedonian literary history, cultural development, and historical analysis rather than the requested thematic interests.

## 3. Analysis of the Error

The text review script identified the following keyword occurrences:

| Keyword | Number of Matches |
|---|---:|
| природа | 14 |
| живот | 295 |
| среќа | 11 |

Although these character sequences appear in the literary work, their presence does not necessarily indicate thematic relevance.

For example, the word "живот" appears in discussions about historical figures and the cultural life of different communities.

The word "природа" appears in literary analysis and descriptions of human characteristics.

The review script also identified words such as "среќаваат" and "среќавања" when searching for "среќа". These words have different meanings.

This last issue is a limitation of the substring-based review script and does not establish that the TF-IDF model matched these words as equivalent terms.

## 4. Potential Causes

The incorrect recommendation may be related to the following limitations:

### 4.1 Lexical Similarity

TF-IDF measures the importance of words based on their occurrence in documents. It does not directly understand the meaning or thematic context of literary works.

### 4.2 Contextual Ambiguity

The same word may appear in different contexts and express different meanings.

### 4.3 Macedonian Language Morphology

The current implementation does not use Macedonian-specific stemming or lemmatization. Consequently, different grammatical forms of the same word may be treated as separate terms.

### 4.4 General Keywords

Broad keywords such as "живот" may occur in many literary works regardless of their primary themes.

### 4.5 Limited Semantic Understanding

The current recommendation model cannot reliably distinguish between a central literary theme and a word mentioned in an unrelated context.

## 5. Expected vs. Actual Results

| Evaluation Aspect | Expected Result | Actual Result |
|---|---|---|
| Valid thematic queries | Return ranked recommendations | Achieved |
| Number of recommendations | Return up to five matching works | Five returned for each evaluation query |
| Recommendation relevance | Return thematically relevant works | 24 out of 25 classified as relevant |
| Empty input | Return no recommendations | Achieved |
| Unknown keywords | Return no matching recommendations | Achieved |
| Response time | Provide recommendations without noticeable delay | Average of 0.0456 seconds |
| Semantic understanding | Recognize thematic relationships | Partially achieved through lexical similarity |

These expected behaviors are qualitative evaluation expectations rather than previously established quantitative performance targets.

## 6. Proposed Improvements

The following improvements could reduce similar errors in future versions:

- Introduce Macedonian-specific stemming or lemmatization.
- Improve text preprocessing.
- Investigate Macedonian stop-word filtering.
- Introduce thematic metadata and literary descriptions.
- Explore semantic similarity using multilingual language models.
- Expand the evaluation dataset.
- Collect independent human relevance assessments.
- Investigate similarity thresholds for filtering weak recommendations.

These improvements are proposed for future development and have not yet been implemented.

## 7. Evaluation Limitations

The identified error was determined through AI-assisted analysis of selected text excerpts.

The evaluation was conducted using only five queries and a broad binary relevance criterion.

Recommendations classified as relevant may still contain weaknesses or match only part of the user's requested interests.

Therefore, the identified error should not be interpreted as the only possible error in the recommendation system.

## 8. Conclusion

The error analysis demonstrates that TF-IDF and Cosine Similarity provide a useful initial approach to Macedonian literary recommendations.

However, lexical similarity does not always correspond to thematic relevance.

The identified limitations provide a foundation for future improvements in Macedonian language processing, semantic understanding, and recommendation quality.