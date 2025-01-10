# Read the input file and calculate word frequencies
def process_file(input_file, output_file):
    try:
        # Read the contents of the file
        with open(input_file, 'r') as file:
            content = file.read()

        # Split the content into words and calculate frequencies
        words = content.split()
        word_frequencies = {}
        for word in words:
            word = word.strip().lower()  # Normalize words to lowercase
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

        # Write the word frequencies to the output file
        with open(output_file, 'w') as file:
            for word, freq in word_frequencies.items():
                file.write(f"{word}: {freq}\n")

        print(f"Word frequencies have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the input and output file names
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function
process_file(input_file, output_file)
