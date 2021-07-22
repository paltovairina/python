with open("test_file.txt") as f:
    num_line = len(f.readlines())
    print(f"Количество строк в файле равно {num_line}")
with open("test_file.txt") as f:
    content_of_file = f.readlines()
    for ind, el in enumerate(content_of_file):
        print(f"Количество слов в строке №{ind + 1} равно {len(el.split())}")
