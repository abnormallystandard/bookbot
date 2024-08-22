def main():
    char_count(word_count(text()) ,count(text()))


def text(file_contents):
    print(file_contents)

def count(file_contents):
    count = {}
    counting = file_contents.lower()
    for i in counting:
        count[i] = 1 + count.get(i, 0)
    return count
    
def sort_on(dict):
    return dict["num"]

def word_count(text):
    words = text.split()
    return len(words)
    
def char_count(words, count):
    char = []
    
    for j in count:
        if not j.isalpha():
            continue
        char.append({"char": j, "num": count[j]})
    char.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for k in char:
        print(f"The '{k['char']}' character was found '{k['num']}' times")
    print("--- End report ---")

def text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

main()
