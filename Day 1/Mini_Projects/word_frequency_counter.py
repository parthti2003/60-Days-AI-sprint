import string

def word_frequency_counter(text):
    # Step 1: Convert to lowercase
    text = text.lower()

    # Step 2: Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Split into words
    words = text.split()

    # Step 4: Count word frequencies
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Step 5: Display results
    for word, count in frequency.items():
        print(f"{word}: {count}")

# Example usage:
input_text = input("Enter a paragraph: ")
word_frequency_counter(input_text)
