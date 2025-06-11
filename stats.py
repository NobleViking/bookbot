def get_num_words(text):
	words = text.split()
	return len(words)

def get_num_characters(text):
	text = text.lower()
	char_dict = {}
	for char in text:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	return char_dict

def sort_num_characters(char_dict):
	char_list = []
	for char, count in char_dict.items():
		char_list.append({"char": char, "num": count})
	char_list.sort(key=lambda item: item["num"], reverse=True)
	return char_list