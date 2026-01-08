# Yoruba Constituency Treebank (Version 1.0)

## Overview

This repository contains the **Yoruba Constituency Treebank**, a manually annotated collection of **1,000 Yoruba sentences** developed as part of an undergraduate research project in linguistics. The treebank is intended to support both **theoretical syntactic analysis** and **computational experiments** for an under-resourced language.

The dataset captures a wide range of Yoruba sentence types, including simple, compound, complex, interrogative, imperative constructions, and serial verb constructions. Sentences were drawn from grammar books, the Yoruba Bible, BBC Yoruba articles, literary texts, and naturally occurring spoken Yoruba. Each sentence was manually annotated with constituency-based phrase structure trees, making the dataset suitable for linguistic analysis and machine learning applications.

In addition to the treebank, the project experimented with **fine-tuning a transformer-based constituency parser** using the manually annotated data. This approach differs from traditional rule-based or English-trained parsers and reflects a data-driven method adapted to Yoruba syntax.

---

## Repository Contents

| File                   | Description                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `yoruba_treebank.csv`  | The annotated dataset containing Yoruba sentences, English translations, sentence types, POS tags, constituency trees, and annotation notes. |
| `yoruba_sentences.txt` | Raw Yoruba sentences without annotations; used as input for computational parsing experiments.                                               |
| `yoruba_eval.json`     | Evaluation file derived from the treebank, used for testing parser outputs against gold-standard trees.                                      |
| `training_scripts/`    | Python scripts used for data preparation, model fine-tuning, and evaluation in Google Colab.                                                 |
| `requirements.txt`     | Python libraries and versions used in the project environment.                                                                               |
| `README.md`            | Project documentation and usage guide (this file).                                                                                           |

---

## Background on Yoruba Syntax

Yoruba is a Niger-Congo language with a basic **Subject–Verb–Object (SVO)** word order and a rich tonal system in which tone plays a grammatical and lexical role. Key syntactic features represented in the treebank include:

* Serial Verb Constructions (SVCs)
* Focus constructions (e.g., *ni*)
* Relative clauses introduced by *tí*
* Embedded complement clauses (e.g., *pé*, *kí*)
* Clause chaining and coordination
* Bare nominal subjects and objects

Due to the limited availability of large, annotated corpora for Yoruba, most existing NLP tools struggle to handle these structures accurately. This treebank addresses that gap by providing **carefully curated, human-annotated constituency structures** grounded in linguistic theory.

---

## Annotation Methodology

All 1,000 sentences were **manually annotated** using a constituency-based framework. Phrase labels such as **IP, NP, VP, CP**, and related projections were applied consistently across the dataset. Annotation decisions were guided by standard Yoruba grammatical descriptions and validated through repeated manual review.

The treebank prioritizes:

* Structural consistency
* Accurate representation of Yoruba-specific constructions
* Clear alignment between surface form and syntactic structure

This manual approach ensures that the dataset reflects human linguistic intuition rather than assumptions imposed by pre-trained models.

---

## Computational Parsing Experiments

Rather than relying solely on existing parsers trained on English, this project explored a **transformer-based sequence-to-sequence approach** to constituency parsing. A multilingual T5-style model was fine-tuned using the Yoruba treebank, where:

* **Input**: Raw Yoruba sentences
* **Output**: Bracketed constituency trees

The experiments were conducted in **Google Colab** using Python and Hugging Face libraries. The aim was not to produce a fully accurate production-level parser, but to examine:

* Whether a transformer model can learn Yoruba syntactic patterns from limited data
* How closely machine-generated trees resemble manual annotations
* Which Yoruba constructions pose the greatest challenges for automatic parsing

Evaluation focused primarily on **qualitative analysis**, with exact-match scores reported only as supplementary indicators of model behaviour.

---

## Environment and Tools

* **Python version**: 3.10 (recommended)
* **Core libraries**:

  * pandas
  * numpy
  * torch
  * transformers
  * sentencepiece

Experiments were run in **Google Colab**, with models and outputs saved to Google Drive for persistence across sessions.

Dependencies can be installed using:

```bash
pip install -r requirements.txt
```

---

## Dataset Sources

The 1,000 sentences were sampled to ensure diversity and representativeness:

| Source Type         | Examples                          | Count | Notes                             |
| ------------------- | --------------------------------- | ----- | --------------------------------- |
| Grammar Texts       | Awobuluyi (1978), Bamgbose (1990) | 200   | Canonical Yoruba structures       |
| News & Media        | BBC Yoruba, Alaroye               | 200   | Contemporary usage                |
| Bible (Bibeli Mimo) | Psalms, Proverbs, Matthew         | 150   | Formal and complex constructions  |
| Literary Texts      | D.O. Fagunwa, Adebayo Faleti      | 150   | Embedded and narrative structures |
| Spoken Yoruba       | Radio & interview transcripts     | 150   | Informal and elliptical patterns  |
| Academic Yoruba     | Textbooks, essays                 | 150   | Standard written syntax           |

---

## Purpose of the Treebank

This treebank is intended to support:

* Yoruba syntactic research
* NLP resource development for under-resourced languages
* Experimental training and evaluation of constituency parsers
* Machine translation and grammar-checking research
* Educational tools for Yoruba language learning

The primary contribution of the project lies in the **manually annotated dataset**, which can serve as a foundation for future computational and linguistic work.

---

## Citation

If you use this dataset, please cite:

Akindele, Victoria A. and Nweya, Gerald (2025). *Yoruba Constituency Treebank (Version 1.0).* GitHub Repository.

A fuller citation will be provided upon completion of the accompanying undergraduate thesis.

---

For questions, collaborations, or feedback:
Victoria Akindele Email: akindeleabimbola2020@gmail.com
Field: Linguistics, Yoruba Syntax, NLP
Field: Linguistics (Yoruba Syntax & NLP)
Email: [akindeleabimbola2020@gmail.com](mailto:akindeleabimbola2020@gmail.com)
