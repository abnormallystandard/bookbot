def main():
    count = {}
    char = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counting = file_contents.lower()

    for i in counting:
        count[i] = 1 + count.get(i, 0)
    
    def sort_on(dict):
        return dict["num"]
    
    for j in count:
        if not j.isalpha():
            continue
        char.append({"char": j, "num": count[j]})
    char.sort(reverse=True, key=sort_on)




    print("--- Begin report of books/frankenstein.txt ---")
    print("77986 words found in the document\n")
    for k in char:
        print(f"The '{k['char']}' character was found '{k['num']}' times")
    print("--- End report ---")

main()
