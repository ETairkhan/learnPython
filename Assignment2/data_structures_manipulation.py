# 1. Define a list of integers and remove all odd numbers
def remove_odds(numbers):
    # Remove all odd numbers from the list.
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Example usage:
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = remove_odds(int_list)
print("Filtered list (no odd numbers):", filtered_list)

# 2. Define a set of strings and find common elements
def find_common_elements(set1, set2):
    # Find common elements between two sets.
    return set1.intersection(set2)

# Example usage:
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "date", "cherry"}
common = find_common_elements(set_a, set_b)
print("Common elements:", common)

# 3. Reverse dictionary key-value pairs
def reverse_dict(d):
    # Reverse the key-value pairs of a dictionary.
    result = {}
    for key, value in d.items():
        result[value] = key
    return result

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dict(sample_dict)
print("Reversed dictionary:", reversed_dict)

# 4. Tuples task
# a) Create a tuple of mixed data types
mixed_tuple = ('Python', 42, 3.14, True, 'Data', False, 3.14)

def count_types(t):
    # Count the number of elements of each data type in a tuple.
    type_count = {}
    for item in t:
        t_type = type(item)
        type_count[t_type] = type_count.get(t_type, 0) + 1
    return type_count

# Example usage:
type_counts = count_types(mixed_tuple)
print("Data type counts in tuple:", type_counts)

# b) Convert the tuple into a list, modify it, and convert back to tuple
def modify_tuple(t):
    # Convert tuple to list, modify it, and convert back to tuple.
    temp_list = list(t)
    temp_list.append("New Element")  # Add a new element
    temp_list.remove(42)  # Remove an existing element
    return tuple(temp_list)

# Example usage:
modified_tuple = modify_tuple(mixed_tuple)
print("Modified tuple:", modified_tuple)
