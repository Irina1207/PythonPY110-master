import json


def task() -> str:
    dict_numbers = {i: i ** 2 for i in range(1, 11)}
    #dict_numbers = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    #dict1_squared = {key: pow(value, 2.) for key, value in dict_numbers.items()}
    #print(dict1_squared)
    #d = int(dict1_squared)
    json_string = json.dumps(dict_numbers, indent=4)  # метод dumps сериализует объект в JSON строку
    return json_string


if __name__ == "__main__":
    print(task())
