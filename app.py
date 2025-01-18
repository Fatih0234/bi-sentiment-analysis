import pandas as pd
import re

# Load AFINN-111 sentiment lexicon
def load_afinn(file_path):
    afinn = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word, score = line.strip().split('\t')
            afinn[word] = int(score)
    return afinn

def load_stopwords(file_path):
    """Load stop words from the given file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = set(line.strip() for line in f)
    return stopwords

def preprocess_text(text):
    """Preprocess text by removing non-alphanumeric characters and converting to lowercase."""
    return re.sub(r'[^a-zA-Z\s]', '', text).lower().split()

def calculate_sentiment(text, afinn):
    """Calculate sentiment score of a given text using the AFINN lexicon."""
    words = preprocess_text(text)
    sentiment_score = sum(afinn.get(word, 0) for word in words)
    return sentiment_score

def classify_sentiment(score):
    """Classify sentiment based on the sentiment score."""
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def identify_new_terms(text, afinn, stopwords):
    """Identify terms not present in the AFINN lexicon and not in the stop words list."""
    words = preprocess_text(text)
    new_terms = [word for word in words if word not in afinn and word not in stopwords]
    return new_terms

def assign_new_term_sentiment(text, afinn, stopwords):
    """Assign sentiment to new terms based on the overall sentiment of the text."""
    new_terms = identify_new_terms(text, afinn, stopwords)
    sentiment_score = calculate_sentiment(text, afinn)
    sentiment_value = sentiment_score / max(1, len(new_terms)) if new_terms else 0
    return {term: round(sentiment_value, 2) for term in new_terms}

# Load AFINN lexicon and stop words
affin_file_path = "AFINN-111.txt"  # Replace with actual file path
stopwords_file_path = "stop_words/stop-words_english_1_en.txt"  # Replace with actual file path

afinn_lexicon = load_afinn(affin_file_path)
stopwords = load_stopwords(stopwords_file_path)

# Sample input/output texts
texts = [
    "I really like new book of that author.",
    "I hate new regulations about importing policies.",
    "Look at that door, it’s still open."
]

# Analyze new terms and assign sentiment
new_terms_results = []
for text in texts:
    new_terms_sentiment = assign_new_term_sentiment(text, afinn_lexicon, stopwords)
    for term, sentiment in new_terms_sentiment.items():
        new_terms_results.append((text, term, sentiment))

# Create DataFrame for display
new_terms_df = pd.DataFrame(new_terms_results, columns=["Text", "New Term", "Sentiment"])
print(new_terms_df)

# Save results to CSV
new_terms_df.to_csv("sentiments_new.csv", index=False)

# Markdown explanation for each section
# 1. Load AFINN lexicon and stop words: Load the lexicon and stop words list for use in sentiment analysis.
# 2. Preprocess text: Clean and tokenize the text.
# 3. Calculate sentiment: Compute the sentiment score for a given text.
# 4. Identify new terms: Extract terms not in the AFINN lexicon or stop words list.
# 5. Assign sentiment to new terms: Use the overall sentiment of the text to assign a score to the new terms.
# 6. Analyze sample texts: Process sample texts to extract and assign sentiment to new terms.
# 7. Save results: Save the analysis results to a CSV file for further use.
