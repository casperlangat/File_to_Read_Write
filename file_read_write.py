def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file and read its contents
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = content.upper()  # convert text to uppercase
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content from '{input_filename}' has been modified and written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
     
    except IOError:
        print(f"Error: Unable to read from '{input_filename}' or write to '{output_filename}'.")

# Prompt the user for the filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the new file to write the modified content: ")

# Call the function with the provided filenames
read_and_modify_file(input_filename, output_filename)
