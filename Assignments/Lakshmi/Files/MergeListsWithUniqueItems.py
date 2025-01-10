# Define two lists
# list1 = [4, 2, 9, 5, 1]
# list2 = [9, 7, 1, 3, 6]

list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "date", "apple"]

# Merge the lists, remove duplicates, and sort the result
merged_list = sorted(set(list1 + list2))

# Write the sorted list to a file
output_file = 'merged.txt'
try:
    with open(output_file, 'w') as file:
        for item in merged_list:
            file.write(f"{item}\n")
    print(f"Sorted merged list has been written to {output_file}.")
except Exception as e:
    print(f"An error occurred: {e}")
