OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE) as file:  # записать лесенку в файл
        f = open("text2.txt",'w')
        for line in file:
            f.write(line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
