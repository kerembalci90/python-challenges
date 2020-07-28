import sys
import re


def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = "This is a si siht"
    
    print(is_palindrome(word))


def is_palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    if not word.isalpha():
        return False

    start = 0
    end = len(word) - 1
    while start < len(word):
        if start == end:
            return True
        
        if word[start] is not word[end]:
            return False
        
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    main()
