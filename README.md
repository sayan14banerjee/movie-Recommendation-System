# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on movie descriptions, genres, cast, crew, and other metadata using TMDB 5000 Movie Dataset.

## Overview

This project implements a movie recommendation system using natural language processing and machine learning techniques to analyze movie features and generate personalized movie recommendations.

## Features

- Content-based movie recommendations
- Processes movie metadata including:
  - Movie descriptions
  - Genres
  - Cast and crew information
  - Release dates
  - User ratings
- Uses advanced NLP techniques for text processing
- Generates similarity scores between movies
- Provides top N similar movie recommendations

## Dataset

The project uses the TMDB 5000 Movie Dataset, which includes:

- `tmdb_5000_movies.csv`: Contains movie metadata
- `tmdb_5000_credits.csv`: Contains cast and crew information

## Project Structure

```plaintext
├── data/
│   ├── processed/
│   │   ├── final_data.csv        # Final processed dataset
│   │   └── process_data.csv      # Intermediate processed data
│   └── raw/
│       ├── tmdb_5000_credits.csv # Original credits data
│       └── tmdb_5000_movies.csv  # Original movies data
├── models/
│   ├── movies.pkl               # Processed movies data
│   └── similarity.pkl           # Similarity matrix
├── src/
│   ├── data/
│   │   ├── data.ipynb          # Data loading notebook
│   │   └── preprocessing.ipynb  # Data preprocessing notebook
│   └── model/
│       └── genarate_embeding.ipynb  # Model training notebook
└── requirement.txt              # Project dependencies
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sayan14banerjee/movie-Recommendation-System.git
cd movie-Recommendation-System
```

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

1. Install required packages:

```bash
pip install -r requirement.txt
```

## Data Processing Pipeline

1. **Data Loading** (`src/data/data.ipynb`):
   - Loads raw TMDB movie and credits datasets
   - Performs initial data exploration
   - Handles missing values

2. **Data Preprocessing** (`src/data/preprocessing.ipynb`):
   - Cleans and processes text data
   - Extracts relevant features
   - Merges movies and credits data

3. **Model Generation** (`src/model/genarate_embeding.ipynb`):
   - Creates text embeddings
   - Generates similarity matrix
   - Saves processed data and models

## Usage

1. Run the notebooks in order:
   - First run `data.ipynb`
   - Then `preprocessing.ipynb`
   - Finally `genarate_embeding.ipynb`

2. The system will generate:
   - Processed datasets in `data/processed/`
   - Model files in `models/`

## Dependencies

- Python 3.8+
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Jupyter Notebook

See `requirement.txt` for complete list of dependencies.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Sayan Banerjee - [GitHub](https://github.com/sayan14banerjee)

Project Link: [https://github.com/sayan14banerjee/movie-Recommendation-System](https://github.com/sayan14banerjee/movie-Recommendation-System)
