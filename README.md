Yoruba Constituency Treebank (Version 1.0)

This repository contains the first prototype Yoruba Constituency Treebank, developed through manual linguistic annotation and AI-assisted parsing. It includes 1,000 Yoruba sentences from multiple genres, annotated for constituency structure to support research in Yoruba syntax and Natural Language Processing (NLP).

Contents

yoruba_treebank.xlsx – Excel file with annotated data including: Yoruba sentence, English translation, sentence type, POS tags, phrase structures, and notes.

yoruba_sentences.txt – Raw Yoruba sentences (plain text), suitable for parsing experiments.

scripts/ – Python scripts for training and testing the Benepar parser.

README.md – This file, explaining the project, dataset, and usage instructions.


Background on Yoruba Syntax

Yoruba is a Niger-Congo language with SVO (Subject–Verb–Object) word order and tonal distinctions that affect meaning. Key syntactic patterns include:

Serial Verb Constructions (SVCs) – sequences of verbs expressing one action.

Focus constructions using ni.

Relative clauses introduced by tí.

Embedded complement clauses.

Clause chaining.

Bare nominal subjects and objects.

Due to a lack of large annotated corpora, NLP tools for Yoruba have been limited. This treebank provides manually curated phrase-structure annotations to support both linguistic research and computational modeling.

Dataset Sources

The 1,000 Yoruba sentences were selected from diverse and balanced sources, including:
| Source Type         | Examples                          | Count | Notes                                       |
| ------------------- | --------------------------------- | ----- | ------------------------------------------- |
| Grammar Texts       | Awobuluyi (1978), Bamgbose (1990) | 200   | Canonical Yoruba structures                 |
| News & Media        | BBC Yoruba, Alaroye               | 200   | Modern syntax & contemporary usage          |
| Bible (Bibeli Mimo) | Psalms, Proverbs, Matthew         | 150   | Complex and formal constructions            |
| Literary Texts      | Fagunwa, Adebayo Faleti           | 150   | Embedded and recursive narrative structures |
| Spoken Yoruba       | Radio & interview transcripts     | 150   | Informal, elliptical speech patterns        |
| Academic Yoruba     | Textbooks, essays                 | 150   | Standard written syntax                     |

Using the Dataset

The Excel file includes:
| Column                | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| `sentence`            | Yoruba sentence with correct orthography and tone marks                       |
| `English Translation` | Clear translation of the sentence                                             |
| `Sentence Type`       | Type of sentence (simple, compound, complex, interrogative, imperative, etc.) |
| `POS Tags`            | Part-of-speech annotation for each word                                       |
| `Phrase Structure`    | Manually annotated bracketed phrase structure                                 |
| `Annotated Trees`     | Copy of the trees from Notepad for reference                                  |
| `Notes`               | Comments on serial verb constructions, focus, embedded clauses, etc.          |


Purpose of the Treebank

This treebank supports:

Yoruba syntax research

NLP resource creation for an under-resourced language

Benepar and transformer-based parser training

Machine translation improvements

Grammar checking tools

Educational technology for Yoruba learners

It also contributes to the documentation and computational modeling of Yoruba grammar.

How to Use This Dataset

You can:

Download the CSV or text file

Use the Yoruba sentences for parsing experiments

Train or evaluate constituency parsers (Benepar, spaCy, BERT-based models)

Build your own NLP models

Use the bracketed trees for linguistic analysis


Parsing Scripts (Benepar Yoruba Model)

The repository includes Python scripts for training and testing the Yoruba constituency parser:

benepar_training.py – trains Benepar on the manually annotated Yoruba treebank.

parse_with_benepar.py – loads the model and parses raw Yoruba sentences.

clean_text.py (optional) – preprocessing and normalization.


Citation

If you use this dataset, please cite:

Akindele, Victoria (2025). Yoruba Constituency Treebank (Version 1.0). GitHub Repository.

A full citation will be provided once the accompanying thesis is completed.

Contact

For questions, collaborations, or feedback:

Victoria Akindele
Email: akindeleabimbola2020@gmail.com

Field: Linguistics, Yoruba Syntax, NLP
