import re
import sys
from datetime import datetime

def read_book(filename: str):

    book = ""

    whitespace = r'[\t\n]'

    with open(f"{filename}", mode='r', encoding = 'utf-8') as data:

        book = data.read()

        book = re.sub(whitespace, " ", book)

    return book

def suffix(string, guess):

    suffix_table = {}

    for iii in range(0, len(string)-guess):

        candidate = string[iii:iii+guess]

        if candidate not in suffix_table:

            suffix_table[candidate] = [iii]

        else:

            suffix_table[candidate].append(iii)

    return suffix_table

def common_words(first, second, guess):

    first_table = suffix(first, guess)
    second_table = suffix(second, guess)

    common = {}

    for word in first_table:

        if word in second_table:

            common[word] = [first_table[word], second_table[word]]

    return common


def analysis(first, second, guess):

    first_book = first
    second_book = second

    common = common_words(first_book, second_book, guess)

    longest_suffix = 0
    longest = ""

    for index_list_pair in common.values():

        first_indices, second_indices = index_list_pair

        for first in first_indices:

            for second in second_indices:

                iii = longest_suffix

                while first_book[first:first+guess+iii] == second_book[second:second+guess+iii]:

                    longest = first_book[first:first+guess+iii]
                    iii += 1
                    longest_suffix += 1

    return longest

def main():

    first_filename, second_filename = sys.argv[1], sys.argv[2]

    reading_start = datetime.now()
    first_book = read_book(f"../data_storage/{first_filename}")
    second_book = read_book(f"../data_storage/{second_filename}")
    reading_stop = datetime.now()
    print(len(first_book), len(second_book))
    print(f"Reading took {(reading_stop-reading_start).microseconds} microseconds")
    guess = 16
    start = datetime.now()
    longest = analysis(first_book, second_book, guess)
    print(f"\"{longest}\"")
    end=datetime.now()
    print(f"Analysis took {(end-start).seconds} seconds and {(end-start).microseconds} microseconds")

if __name__ == "__main__":
 
    main()