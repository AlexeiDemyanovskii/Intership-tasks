import json
import sys

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test.get('id')
        if test_id and test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'tests' in test:
            fill_values(test['tests'], values_dict)

def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py <path_to_values.json> <path_to_tests.json> <path_to_report.json>")
        return

    path_to_values = sys.argv[1]
    path_to_tests = sys.argv[2]
    path_to_report = sys.argv[3]

    # Чтение файлов values.json и tests.json
    with open(path_to_values, 'r', encoding='utf-8') as values_file:
        values_data = json.load(values_file)
    
    with open(path_to_tests, 'r', encoding='utf-8') as tests_file:
        tests_data = json.load(tests_file)

    # Преобразование списка values.json в словарь для быстрого доступа по ID
    values_dict = {value['id']: value['value'] for value in values_data}

    # Заполнение полей value в структуре тестов
    fill_values(tests_data['tests'], values_dict)

    # Запись результатов в файл report.json
    with open(path_to_report, 'w', encoding='utf-8') as report_file:
        json.dump(tests_data, report_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
