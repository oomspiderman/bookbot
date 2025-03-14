def get_num_words(book_contents : str):
    book_as_words = book_contents.split()
    return len(book_as_words)

def get_char_count_dictionary(book_contents : str):
    char_dic = {}
    for char in book_contents.lower(): 
        if char in char_dic:
            char_dic[char] = char_dic[char] + 1
        else: 
            char_dic[char] = 1
    return char_dic

def get_sorted_dictionary(char_dic):
    sorted_dict_desc = dict(sorted(char_dic.items(), key=lambda item: item[1], reverse=True))
    filtered_and_sorted_dic = {}
    for char in sorted_dict_desc: 
        if char.isalpha():
          filtered_and_sorted_dic[char] = sorted_dict_desc[char]
    return filtered_and_sorted_dic