   
def count_book_words(book):
    book_list = book.split()
    return len(book_list)

def count_book_characters(book):
    character_dict = {}
    for char in book:
        char = char.lower()
        if(char in character_dict):
            character_dict[char] += 1
        else: 
            character_dict[char] = 1
    
    return character_dict


def sort_char_dict(dict_of_chars):
    list_of_char_dicts = []
    for char in dict_of_chars:
        list_of_char_dicts.append({"character": char, "count": dict_of_chars[char]})

    def sort_on(dict):
        return dict["count"]
    
    list_of_char_dicts.sort(key=sort_on, reverse=True)
    
    return list_of_char_dicts