import re
import sys
from datetime import datetime

'''
The purpose of this program is to read two books into strings and compare their contents. It is done by hashing all their
substrings of certain length and forming an interception so that the program knows which substrings are common and
what are the start indices in both long strings. The longest one is easy to find when the books are real-world 
examples, not like a million characters 'a' repeated. 
'''

def read_book(filename: str):

    '''
    Reads a book and filters the white space
    '''

    book = ""

    whitespace = r'[\n\t]' 

    with open(f"{filename}", mode='r', encoding = 'utf-8') as data:

        book = data.read()

        book = re.sub(whitespace, " ", book)

    return book

def prefix(string, guess):

    '''
    params guess: the length of all the substrings in the result dictionary
    This procedure gives all the guess-length slices of the string. The start index of every instance
    is recorded.
    '''

    prefix_table = {}

    for iii in range(0, len(string)-guess):

        candidate = string[iii:iii+guess]

        if candidate not in prefix_table:

            prefix_table[candidate] = [iii]

        else:

            prefix_table[candidate].append(iii)

    return prefix_table

def common_words(first, second, guess):

    '''
    Uses the prefix function and finds the common slices and records their start indices
    '''

    first_table = prefix(first, guess)
    second_table = prefix(second, guess)

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

    '''
    Once the common words are found, all the start indices in both books are checked for matches. This doesn't
    actually take too much time, because if the guess is made properly, there are not too many matches and so
    the check is faster than it seems.
    '''

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

    first_filename, second_filename, guess = sys.argv[1], sys.argv[2], sys.argv[3]
    guess = int(guess)
    reading_start = datetime.now()
    first_book = read_book(f"../data_storage/{first_filename}")
    second_book = read_book(f"../data_storage/{second_filename}")
    reading_stop = datetime.now()
    print(len(first_book), len(second_book))
    print(f"Reading took {(reading_stop-reading_start).microseconds} microseconds")
    start = datetime.now()
    longest = analysis(first_book, second_book, guess)
    print(f"\"{longest}\"")
    end=datetime.now()
    print(f"Analysis took {(end-start).seconds} seconds and {(end-start).microseconds} microseconds")

if __name__ == "__main__":
 
    main()