def process_text(paragraph):
    # Step 1: Count the number of vowels and consonants
    def count_vowels_consonants(text):
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowels_count = 0
        consonants_count = 0
        
        for char in text:
            if char in vowels:
                vowels_count += 1
            elif char in consonants:
                consonants_count += 1
        
        return vowels_count, consonants_count

    # Step 2: Replace all occurrences of a specific word with another word
    def replace_word(text, old_word, new_word):
        words = text.split()  # Split text into a list of words
        replaced_words = []  
    
        for word in words:
            if word == old_word:
                replaced_words.append(new_word)  # Replace the exact match with the new word
            else:
                replaced_words.append(word)  # Keep the word unchanged if it's not a match
    
        return ' '.join(replaced_words)  # Join the list back into a single string

    # Step 3: Extract all unique words and sort them alphabetically
    def extract_unique_words(text):
        # Manually remove punctuation
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        cleaned_text = ""
        for char in text:
            if char not in punctuation:
                cleaned_text += char  # Add the character if it's not punctuation
            else:
                cleaned_text += " "  # Replace punctuation with a space
        words = cleaned_text.lower().split()
        return sorted(set(words))

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
