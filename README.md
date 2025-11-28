Yoruba Constituency Treebank (Version 1.0)
Overview

This repository contains the Yoruba Constituency Treebank, a manually annotated collection of 1,000 Yoruba sentences. It is designed for linguistic and computational research, including natural language processing (NLP) tasks such as parsing, grammar analysis, and machine learning. The dataset captures diverse sentence types—simple, compound, complex, interrogative, imperative, and serial verb constructions—sourced from grammar books, the Yoruba Bible, BBC Yoruba articles, literary texts, and spoken Yoruba.

The project also provides training scripts for the Benepar parser, enabling AI-assisted syntactic analysis of Yoruba sentences.

| File                      | Description                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `yoruba_treebank.csv`     | Annotated dataset with columns for Yoruba sentences, English translations, sentence type, POS tags, phrase structure trees, and notes. |
| `yoruba_sentences.txt`    | Raw Yoruba sentences without annotations; used for parsing experiments.                                                                |
| `train_benepar_yoruba.py` | Python script for training Benepar with the annotated treebank.                                                                        |
| `requirements.txt`        | Lists Python libraries and versions needed for parsing and training.                                                                   |
| `README.md`               | This file, explaining the dataset, usage, and environment setup.     



Background on Yoruba Syntax

Yoruba is a Niger-Congo language with SVO (Subject–Verb–Object) word order and tonal distinctions that affect meaning. Key syntactic patterns include:

Serial Verb Constructions (SVCs) – sequences of verbs expressing one action.

Focus constructions using ni.

Relative clauses introduced by tí.

Embedded complement clauses.

Clause chaining.

Bare nominal subjects and objects.

Due to a lack of large annotated corpora, NLP tools for Yoruba have been limited. This treebank provides manually curated phrase-structure annotations to support both linguistic research and computational modeling.

Usage Instructions
Using the raw Yoruba sentences for parsing:

import spacy
import benepar

# Load base English model and add Benepar
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("benepar", config={"model": "benepar_yoruba"})

# Parse a sentence from yoruba_sentences.txt
doc = nlp("Mo ra aso tuntun")
print(doc._.parse_string)


Environment Requirements

Python: 3.10 (recommended)

Libraries:

pandas

numpy

spacy

benepar

Optional Tools: Jupyter Notebook or VS Code for running scripts interactively.

Install all dependencies with:
pip install -r requirements.txt

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
