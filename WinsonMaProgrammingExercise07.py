# WinsonMaProgrammingExercise07.py
import re

def split_sentences(paragraph):
    # Splits paragraph into individual numbers
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s' 
    sentences = re.split(sentence_pattern, paragraph)
    return [s.strip() for s in sentences if s.strip()]
    
def count_and_display_sentences(paragraph):
    # Counts and display
    sentences = split_sentences(paragraph)
    sentence_count = len(sentences)
    
    print(f"There are {sentence_count} sentences in the paragraph:\n")
    for sentences in sentences:
        print(sentences)
        
def main():
    # Input from user and display sentences
    paragraph = input("Enter paragraph: ")
    count_and_display_sentences(paragraph)
    
if __name__ == "__main__":
    main()