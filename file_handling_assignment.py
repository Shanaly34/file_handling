try:
    # Open the file in write mode
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Hello, world!\n")
        file.write("This is line 2.\n")
        file.write("The answer is 42.\n")

    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print(content)

    # Open the file in append mode
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("This is line 4.\n")
        file.write("Appending more text.\n")
        file.write("Last line.\n")

    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the updated contents of the file
        updated_content = file.read()

    # Display the updated contents on the console
    print(updated_content)

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied when accessing the file!")

finally:
    print("Execution completed.")
