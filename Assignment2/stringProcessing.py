def process_text(paragraph):
    # Step 1: Count the number of vowels and consonants
    def count_vowels_consonants(text):
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowels_count = sum(1 for char in text if char in vowels)
        consonants_count = sum(1 for char in text if char in consonants)
        return vowels_count, consonants_count

    # Step 2: Replace a specific word with another
    def replace_word(text, old_word, new_word):
        return text.replace(old_word, new_word)

    # Step 3: Extract unique words and sort them alphabetically
    def extract_unique_words(text):
        # Remove punctuation manually
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        cleaned_text = ''.join(char if char not in punctuation else ' ' for char in text)
        words = cleaned_text.lower().split()
        return sorted(set(words))  # Return sorted unique words

    # Input for word replacement
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the replacement word: ")

    # Call functions
    vowels_count, consonants_count = count_vowels_consonants(paragraph)
    replaced_text = replace_word(paragraph, old_word, new_word)
    unique_words = extract_unique_words(paragraph)

    # Print results
    print("\nProcessed Text Results:")
    print(f"Vowels Count: {vowels_count}")
    print(f"Consonants Count: {consonants_count}")
    print(f"Text after Replacement: {replaced_text}")
    print(f"Unique Words (Alphabetical Order): {unique_words}")

# Example Paragraph
paragraph = "This is an example paragraph! It contains vowels, consonants, and punctuation. Replace words as you like."

# Call the function with the example paragraph
process_text(paragraph)
