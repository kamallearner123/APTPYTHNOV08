# Function to check if a word is a palindrome
def is_palindrome(word):
    word = word.strip().lower()  # Normalize word: strip whitespace and convert to lowercase
    return word == word[::-1]


# Read words from words.txt and write palindromes to palindromes.txt
def process_palindromes(input_file, output_file):
    try:
        # Read words from the input file
        with open(input_file, 'r') as infile:
            words = infile.read().split()  # Split content into words

        # Identify palindromic words
        palindromes = [word for word in words if is_palindrome(word)]

        # Write palindromic words to the output file
        with open(output_file, 'w') as outfile:
            for word in palindromes:
                outfile.write(word + '\n')

        print(f"Palindromic words have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the input and output file names
input_file = 'words.txt'
output_file = 'palindromes.txt'

# Call the function
process_palindromes(input_file, output_file)
