import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(file_path):
	with open(file_path) as file:
		return file.read()
	
def print_report(text, path):
	print("============ BOOKBOT ============")
	print(f" Analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(text)} total words")
	print("--------- Character Count -------")
	char_dict = get_num_characters(text)
	char_list = sort_num_characters(char_dict)
	for char in char_list:
		if char["char"].isalpha():
			print(f"{char['char']}: {char['num']}")
	print("============= END ===============")


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	book_text = get_book_text(path)
	print_report(book_text, path)


if __name__ == "__main__":
	main()