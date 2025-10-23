'''
Write functions to process a list of words entered by the user as a single string.
The words may be separated by commas, spaces, tabs, semicolons, or any combination of these delimiters.
Your program should:
- Convert the input string into a list of clean words split by any of these delimiters.
- Use a while loop to repeatedly ask the user to enter new words to add to the list until the user enters 'stop'.
- After each addition, convert the updated list back into a comma-separated string and print it.
- Finally, return the concatenated comma-separated string.

Example:
Initial input: apple, banana;cherry\tdate
User adds: elderberry
Current list string: apple,banana,cherry,date,elderberry
User adds: fig
Current list string: apple,banana,cherry,date,elderberry,fig
User inputs: stop
Final list string: apple,banana,cherry,date,elderberry,fig

Functions:
- get_initial_input: Ask the user to enter a string of words separated by commas, spaces, tabs, or semicolons. Return the list of words.
- add_word_to_list: Take the current list and a new word, add the word to the list.
- list_to_comma_string: Convert a list of words to a comma-separated string.
- list_string_manager: Main function using a while loop to add words until 'stop' is entered, printing the list string after each addition.
'''

def get_initial_input():
    user_input = input("Enter a list of words (separated by commas, spaces, tabs, or semicolons): ")
    delimiters = [',', ';', ' ', '\t']
    current_word = ""
    words = []
    for char in user_input:
        if char in delimiters:
            if current_word:
                words.append(current_word) # Append the word if it is not an empty string.
                current_word = ""
        else:
            current_word += char
    if current_word:  # Append the word if it is not an empty string.
        words.append(current_word)
    return words

def add_word_to_list(words_list, new_word):
    if new_word != "":
        words_list.append(new_word)

def list_to_comma_string(words_list):
    return ",".join(words_list)

def list_string_manager():
    words = get_initial_input()
    while True:
        new_word = input("Enter a new word to add (or 'stop' to finish): ").strip()
        if new_word == "stop":
            break
        add_word_to_list(words, new_word)
        current_string = list_to_comma_string(words)
        print(f"Current list string: {current_string}")
    final_string = list_to_comma_string(words)
    print(f"Final list string: {final_string}")
    return final_string