import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = ...  #записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()

#### \d\d \[(\.+){1,}] \(http[s]://\w+
#### \d\d\. \[(.+?)\]\(https://.+?\)\s+\w+\w+
#### \d\d\. \[(.+?)\]\(https://.+?\)\s+\w+ \w+ \w+ \(\d+.\d% recommended?\)\s...\(https://www.\w+.\w+/\w+/(.+?)/\d\d.\w+#\w+\)\s..(.+?)\"\s\[\w+.\w+\]\(https://\w+.\w+/\w+\)
# https://regex101.com/r/wxXm1z/1