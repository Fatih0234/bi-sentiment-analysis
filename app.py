import pandas as pd
import re
import os

def combine_stop_words(input_dir, output_file):
    """
    Combines all unique stop words from text files in a given directory into a single output file.

    Args:
        input_dir (str): Directory containing stop-word text files.
        output_file (str): Path to the output file where the combined stop words will be saved.
    """
    # Initialize a set to hold all unique stop words
    unique_stop_words = set()

    # Loop through all files in the directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Check if the file is a .txt file
        if file_name.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    word = line.strip()  # Remove any extra whitespace or newline characters
                    unique_stop_words.add(word)  # Add the word to the set

    # Write all unique stop words into the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        for word in sorted(unique_stop_words):  # Sort words alphabetically before writing
            output.write(word + '\n')

    print(f"Combined stop-words file created at: {output_file}")

# Load AFINN-111 sentiment lexicon
def load_afinn(file_path):
    """
    Load the AFINN-111 lexicon from a file.

    Args:
        file_path (str): Path to the file containing the AFINN lexicon.

    Returns:
        dict: A dictionary where keys are words and values are their sentiment scores.
    """
    afinn = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word, score = line.strip().split('\t')
            afinn[word] = int(score)
    return afinn

def load_stopwords(file_path):
    """
    Load stop words from the given file.

    Args:
        file_path (str): Path to the file containing stop words.

    Returns:
        set: A set of stop words.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = set(line.strip() for line in f)
    return stopwords

def preprocess_text(text):
    """
    Preprocess text by removing non-alphanumeric characters and converting to lowercase.

    Args:
        text (str): Input text to preprocess.

    Returns:
        list: A list of cleaned and tokenized words.
    """
    return re.sub(r'[^a-zA-Z\s]', '', text).lower().split()

def calculate_sentiment(text, afinn):
    """
    Calculate sentiment score of a given text using the AFINN lexicon.

    Args:
        text (str): Input text to analyze.
        afinn (dict): AFINN lexicon dictionary with words and their sentiment scores.

    Returns:
        int: The total sentiment score for the text.
    """
    words = preprocess_text(text)
    sentiment_score = sum(afinn.get(word, 0) for word in words)
    return sentiment_score

def classify_sentiment(score):
    """
    Classify sentiment based on the sentiment score.

    Args:
        score (int): Sentiment score.

    Returns:
        str: The sentiment category ("Positive", "Negative", or "Neutral").
    """
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def identify_new_terms(text, afinn, stopwords):
    """
    Identify terms not present in the AFINN lexicon and not in the stop words list.

    Args:
        text (str): Input text to analyze.
        afinn (dict): AFINN lexicon dictionary with words and their sentiment scores.
        stopwords (set): Set of stop words to ignore.

    Returns:
        list: A list of new terms not present in the AFINN lexicon or stop words.
    """
    words = preprocess_text(text)
    new_terms = [word for word in words if word not in afinn and word not in stopwords]
    return new_terms

def assign_new_term_sentiment(text, afinn, stopwords):
    """
    Assign sentiment to new terms based on the overall sentiment of the text.

    Args:
        text (str): Input text to analyze.
        afinn (dict): AFINN lexicon dictionary with words and their sentiment scores.
        stopwords (set): Set of stop words to ignore.

    Returns:
        dict: A dictionary of new terms and their assigned sentiment values.

    Explanation:
        - The overall sentiment score is divided by the number of new terms to distribute sentiment proportionally.
        - If there are no new terms, the sentiment value defaults to 0.
        - This ensures a fair distribution of sentiment among new terms.
    """
    new_terms = identify_new_terms(text, afinn, stopwords)
    sentiment_score = calculate_sentiment(text, afinn)

    # Divide sentiment score by the number of new terms to distribute sentiment proportionally
    # If there are no new terms, default sentiment value to 0
    sentiment_value = sentiment_score / max(1, len(new_terms)) if new_terms else 0

    # Return a dictionary of new terms and their assigned sentiment value (rounded to 2 decimals)
    return {term: round(sentiment_value, 2) for term in new_terms}

# Load AFINN lexicon and stop words
affin_file_path = "AFINN-111.txt"  # Replace with actual file path
stopwords_file_path = "stop-words-english.txt"  # Replace with actual file path

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
# 5. Assign sentiment to new terms:
#    - The sentiment score is divided by the number of new terms to distribute the sentiment proportionally.
#    - This ensures that the overall sentiment is fairly shared among the new terms.
#    - If no new terms are found, a default sentiment value of 0 is assigned.
#    - Each term's sentiment is rounded to 2 decimal places for clarity.
# 6. Analyze sample texts: Process sample texts to extract and assign sentiment to new terms.
# 7. Save results: Save the analysis results to a CSV file for further use.
