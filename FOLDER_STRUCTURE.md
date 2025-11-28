Yoruba-Constituency-Treebank/
│
├── data/
│   ├── yoruba_treebank.csv          # Full annotated dataset
│   ├── yoruba_sentences.txt         # Raw Yoruba sentences only
│   └── sample_sentences/            # Optional: sample examples
│
├── scripts/
│   ├── benepar_training.py          # Script used to train Benepar Yoruba
│   ├── parse_with_benepar.py        # Script for parsing Yoruba sentences
│   └── utils/                       
│       └── cleaning_functions.py    # Optional preprocessing tools
│
├── models/
│   └── benepar_yoruba_model.pt      # Trained Benepar model (optional)
│
├── README.md                        # Project description
├── LICENSE                          # MIT license
├── CITATION.bib                     # Citation file
└── .gitignore                       # Files to ignore (e.g., large models)
