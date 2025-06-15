def get_word_count(file_contents):
    return len(file_contents.split())

def get_num_of_characters(file_contents):
    lowercase_text = file_contents.lower()
    characters_stats = {}
    
    for character in lowercase_text:
        if character not in characters_stats:
            characters_stats[character] = 1
        else:
            characters_stats[character] += 1

    return characters_stats

def format_dict(unformatted_dict):
    list_of_dicts = []
    for key in unformatted_dict:
        formatted_dict = {}
        formatted_dict["char"] = key
        formatted_dict["num"] = unformatted_dict[key]
        list_of_dicts.append(formatted_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(dict):
    return dict["num"]