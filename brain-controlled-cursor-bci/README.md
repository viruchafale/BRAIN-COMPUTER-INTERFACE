brain-controlled-cursor-bci/
│
├── data/
│   ├── raw/
│   │   ├── subject01/
│   │   │   ├── S01T.mat
│   │   │   ├── S01E.mat
│   │   ├── subject02/
│   │
│   ├── processed/
│   │   ├── subject01_epochs.npy
│   │   ├── subject01_features.npy
│
│   └── README.md
│
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── feature_extraction.py
│   ├── train_model.py
│   ├── evaluate.py
│   └── realtime_simulation.py
│
├── models/
│   ├── lda_model.pkl
│   ├── svm_model.pkl
│
├── notebooks/
│   ├── 01_explore_eeg.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_features_csp.ipynb
│   └── 04_classification.ipynb
│
├── results/
│   ├── plots/
│   │   ├── raw_eeg.png
│   │   ├── psd.png
│   │   └── confusion_matrix.png
│   │
│   └── metrics.json
│
├── configs/
│   ├── eeg_config.yaml
│
├── requirements.txt
├── main.py
├── README.md
└── .gitignore






