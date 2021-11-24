INPUT_FILE = "input.txt"

filename = "input.txt"
def task() -> None:
    with open(filename) as file:  # открыть указатель на файл
        for line in file:   # файл является итератором, который работает с циклом for в построчном режиме
            print(line, end="")


if __name__ == "__main__":
    task()

#filename = "input.txt"
#    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
#        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
#            line = line.strip()
#            print(line)
#f.write(word + "\n")