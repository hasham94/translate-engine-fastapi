import re
from collections import defaultdict

def simple_summarize(text: str, top_n=3) -> str:
    # Basic sentence tokenization
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # Word frequency analysis
    word_freq = defaultdict(int)
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        if word not in {'the', 'a', 'an', 'in', 'of', ...}:  # Add more stopwords
            word_freq[word] += 1
    
    # Score sentences
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        score = sum(word_freq[word.lower()] for word in re.findall(r'\b\w+\b', sentence))
        sentence_scores[i] = score
    
    # Get top sentences
    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]
    return ' '.join(sentences[i] for i in sorted(top_indices))