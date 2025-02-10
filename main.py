LETTERS = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_length = len(file_contents.split())
        print(f"{total_length} words found in the document")
        total_counts = appears(file_contents)
        for key in total_counts:
            if key in LETTERS:
                count = total_counts[key]
                print(f"The \'{key}\' was found {count} times")

def appears(book_text):
    totals = {}
    for char in book_text.lower():
        if char in totals:
            totals[char] += 1
        else:
            totals[char] = 1
    return totals












main()