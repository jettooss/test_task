import json
import sys
import os

def process_data(data_file, replacement_file, output_file):
    with open(replacement_file) as f:
        replacements = json.load(f)

    with open(data_file) as f:
        data = json.load(f)

    for replacement in reversed(replacements):
        source = replacement["source"]

        if source is not None:
            for i, message in enumerate(data):
                if source in message:
                    data[i] = message.replace(source, replacement["replacement"])
        else:
            data = [message for message in data if replacement["replacement"] not in message]

    with open(output_file, "w") as f:
        json.dump(data, f, ensure_ascii=False)

def get_file_path(prompt):
    while True:
        try:
            file_path = input(prompt)

            if os.path.exists(file_path):
                return file_path
            else:
                print(f"Файл не найден: {file_path}")
                continue
        except KeyboardInterrupt:
            print("\nВыход из программы")
            sys.exit()

def main():
    data_file = get_file_path("Пожалуйста, введите путь к файлу data.json: ")
    replacement_file = get_file_path("Пожалуйста, введите путь к файлу replacement.json: ")
    output_file = input("Пожалуйста, введите имя и/или путь для файла вывода (result.json): ")

    process_data(data_file, replacement_file, output_file)
    print("Обработка данных завершена. Результат сохранен в файле:", output_file)

if __name__ == "__main__":
    main()