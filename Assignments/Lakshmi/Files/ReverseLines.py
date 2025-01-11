# Function to reverse the content of each line
def reverse_lines(input_file, output_file):
    try:
        # Open the input file and read lines
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Reverse the content of each line
        reversed_lines = [line.strip()[::-1] for line in lines]

        # Write the reversed lines to the output file
        with open(output_file, 'w') as outfile:
            for line in reversed_lines:
                outfile.write(line + '\n')

        print(f"Reversed lines have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the input and output file names
input_file = 'reverse_input.txt'
output_file = 'reverse_output.txt'

# Call the function
reverse_lines(input_file, output_file)
