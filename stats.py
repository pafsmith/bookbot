def get_book_length(book_text):
 x = book_text.split()
 return len(x)


def num_of_characters(book_text):
   char_counts = {}
   for char in book_text.lower():
     char_counts[char] = char_counts.get(char, 0) + 1
   return char_counts
   
def sorted_char_count(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        sorted_chars.append({"char": char, "count": count})

    def sort_on_count(item):
        return item["count"]

    sorted_chars.sort(reverse=True, key=sort_on_count)
    return sorted_chars



def sorted_dict(char_dict):
 char_dict = "x"
 return char_dict
 