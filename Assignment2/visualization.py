import matplotlib.pyplot as plt
from collections import Counter

# Task 1: Bar Chart for Letter Frequency
def bar_chart():
    text = "Data Science is Amazing"
    text = text.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    letter_counts = Counter(text)  # Count frequency of each letter

    # Extract letters and their frequencies
    letters = sorted(letter_counts.keys())  # Sort letters alphabetically
    frequencies = [letter_counts[letter] for letter in letters]

    # Create the bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(letters, frequencies)
    plt.title("Letter Frequency in 'Data Science is Amazing'")
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.show()

# Task 2: Line Chart
def line_chart():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create the line chart
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o')
    plt.title("Line Chart Example")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Call the functions
bar_chart()
line_chart()
