import sys
from stats import get_book_length, num_of_characters, sorted_char_count


if (len(sys.argv) < 2):
 print("Usage: python3 main.py <path_to_book>")
 sys.exit(1)


def get_book_text(file_path):
 with open(file_path) as f:
  book_text = f.read()
 return book_text


def main():
 book_path = sys.argv[1]
 book_text = get_book_text(book_path)
 book_length = get_book_length(book_text)


 char_count = num_of_characters(book_text)
 sorted_char = sorted_char_count(char_count)
 print("============ BOOKBOT ============")
 print(f"Analyzing book found at {book_path}...")
 print("----------- Word Count ----------")
 print (f"Found {book_length} total words")
 print("--------- Character Count -------")
 for item in sorted_char:
  if item["char"].isalpha():
   print(f"{item['char']}: {item['count']}")

main()