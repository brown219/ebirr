dictionary = {}
def add_word(word, definition):
    dictionary[word] = definition
    print(f"Word '{word}' added successfully.")

def remove_word(word):
    if word in dictionary:
        del dictionary[word]
        print(f"Word '{word}' removed successfully.")
    else:
        print(f"Word '{word}' not found.")

def lookup_word(word):
    if word in dictionary:
        print(f"{word}: {dictionary[word]}")
    else:
        print(f"Word '{word}' not found.")

def list_words():
    if dictionary:
        for word, definition in dictionary.items():
            print(f"{word}: {definition}")
    else:
        print("Dictionary is empty.")


def display_menu():
    print("\nDictionary App")
    print("1. Add a word")
    print("2. Remove a word")
    print("3. Look up a word")
    print("4. List all words")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            word = input("Enter the word: ")
            definition = input("Enter the definition: ")
            add_word(word, definition)
        elif choice == '2':
            word = input("Enter the word to remove: ")
            remove_word(word)
        elif choice == '3':
            word = input("Enter the word to look up: ")
            lookup_word(word)
        elif choice == '4':
            list_words()
        elif choice == '5':
            print("Exiting the dictionary app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
