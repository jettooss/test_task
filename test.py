
import os
import unittest
import json

from main import program_start


class TestProcessDataNew(unittest.TestCase):

    # Первый тестовый случай: проверка поведения функции program_start с определёнными аргументами
    def test_process_data_thewhite(self):
        # Вызываем функцию program_start с определёнными аргументами и сохраняем результат
        actual_output=program_start('data.json', 'replacement.json', 'output1.json')
        # Загружаем ожидаемые данные из файла
        expected_output = self.load_data_from_file('initial-data.json')
        # Используем assertEqual для проверки равенства ожидаемого и полученного результатов
        self.assertEqual(actual_output, expected_output)

    # Второй тестовый случай: проверка поведения функции program_start с другими аргументами
    def test_process_data_new(self):
        # Вызываем функцию program_start с определёнными аргументами и сохраняем результат
        actual_output=program_start('my_data.json', 'replace.json', 'output2.json')
        # Загружаем ожидаемые данные из другого файла
        expected_output = self.load_data_from_file('expected_output_data.json')
        # Еще раз сравниваем ожидаемый и полученный результаты
        self.assertEqual(actual_output, expected_output)

    # Функция для загрузки данных из файла: она будет использоваться, чтобы загрузить ожидаемые результаты
    def load_data_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

# Если этот скрипт запущен как основной файл, запускаем все тесты
if __name__ == "__main__":
    unittest.main()