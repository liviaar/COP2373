# This program uses the code in Section 7.4 of Supercharged Python and
# allows the user to enter a paragraph beginning with numbers. It also
# displays the amount of sentences in the paragraph. -Livia Augusto Razera,
# Assignment 7.

import re

# Function which splits the paragraph into sentences using a regular
# expression.
def split_into_sentences(paragraph):

    sentence_pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?!])\s+')

    sentences = sentence_pattern.split(paragraph.strip())
    return [s.strip() for s in sentences if s.strip()]

# Function that displays each sentence and the total amount of sentences.
def display_sentences(sentences):

    print('\n--- Sentences ---')
    for i, sentence in enumerate(sentences, start=1):
        print(f'{i}. {sentence}')

    print(f'\nTotal sentences: {len(sentences)}')

# Main function prompts user for paragraph, and displays results. 
def main():
    paragraph = input('Enter a paragraph:\n')
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)

# Calls out main function. 
if __name__ == '__main__':
    main()