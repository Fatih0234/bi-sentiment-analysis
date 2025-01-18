# Sentiment Analysis Using AFINN and Custom Techniques

## Project Overview
This project demonstrates a simple and educational approach to sentiment analysis using Python. The primary goal is to analyze text data by calculating sentiment scores for known words using the **AFINN-111 lexicon**, identifying new terms in the text, and assigning sentiment values to these new terms based on their context.

The project is implemented for learning purposes and showcases:
- The usage of **AFINN lexicon** for sentiment scoring.
- The exclusion of common stop words to focus on meaningful terms.
- The process of identifying and estimating sentiment for new, unknown terms in a text.
- The ability to save results for further analysis.

This project is designed to be fun and insightful for anyone learning natural language processing (NLP) or sentiment analysis.

---

## Key Functionalities
1. **Loading AFINN Lexicon**:
   - Loads a predefined lexicon of words and their associated sentiment scores from a file.
2. **Stop Words Management**:
   - Reads stop words from a file to exclude them from analysis.
3. **Text Preprocessing**:
   - Cleans and tokenizes text by removing special characters and converting it to lowercase.
4. **Sentiment Scoring**:
   - Computes a sentiment score for a given text using the AFINN lexicon.
5. **Identifying New Terms**:
   - Extracts terms from the text that are not in the AFINN lexicon or stop words.
6. **Assigning Sentiment to New Terms**:
   - Distributes the overall sentiment score proportionally among the identified new terms.
7. **Results Output**:
   - Displays results and saves them to a CSV file for further use.

---

## Repository Structure
- **`app.py`**: Main Python script for executing the sentiment analysis tasks.
- **`AFINN-111.txt`**: The AFINN lexicon file containing words and their sentiment scores.
- **`stop_words/`**: Directory containing multiple stop-word files and a combined output file.
- **`sentiments_new.csv`**: Output file storing the results of new terms and their assigned sentiment scores.

---

## How It Works
### Step 1: Load Required Data
- Load the AFINN lexicon to analyze known words.
- Combine stop words from multiple files to ignore common, irrelevant words.

### Step 2: Preprocess Text
- Clean input text by removing punctuation and converting it to lowercase.
- Tokenize the text into individual words.

### Step 3: Perform Sentiment Analysis
1. **Calculate Sentiment for Known Words**:
   - Use the AFINN lexicon to sum the sentiment scores of known words in the text.
2. **Identify New Terms**:
   - Extract words not present in the AFINN lexicon or stop words list.
3. **Assign Sentiment to New Terms**:
   - Proportionally distribute the overall sentiment score of the text to the new terms.

### Step 4: Save and Visualize Results
- Create a table showing the text, new terms, and their sentiment values.
- Save the results to a CSV file for further analysis or reporting.

---

## Requirements
- Python 3.7+
- Required libraries:
  - `pandas`
  - `re`

---

## Installation and Execution
1. Clone the repository.
2. Ensure the required libraries are installed.
   ```bash
   pip install pandas
   ```
3. Run the main script:
   ```bash
   python app.py
   ```
4. View the results in the terminal or in the generated CSV file (`sentiments_new.csv`).

---

## Learning Objectives
- Understand how lexicons like AFINN can be used for sentiment analysis.
- Learn how to preprocess text and manage stop words.
- Practice identifying and handling new, unknown terms in a text.
- Gain experience in saving and visualizing results.

---

## Acknowledgements
- The **AFINN lexicon** was developed by Finn Årup Nielsen and is used here for educational purposes.
- The stop words used in this project come from freely available resources.

---

## Disclaimer
This project is for **learning purposes only**. The sentiment analysis implementation here is basic and not suitable for production use. For more robust NLP solutions, consider using libraries like `NLTK`, `spaCy`, or `Hugging Face`.

