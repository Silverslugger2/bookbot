with open("books/Frankenstein.txt") as f:
    file_contents = f.read()
    file_contents_lower = file_contents.lower()
    cleaned = ''.join(c for c in file_contents_lower if c.isalpha())
    words = file_contents_lower.split()
    wordcount = len(words)
    characters = [key for key in cleaned]
    character_dictionary = {}
    for character in characters:
        count = 0
        character_dictionary[character] = count
    for character in characters:
        if character in characters:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
            
sorted_character_dictionary = sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True)

def main():
    print("--- Begin report of books/Frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    
    for character, count in sorted_character_dictionary:
        print(f"The {character} character was found {count} times")

    print("--- End report ---")

main()
