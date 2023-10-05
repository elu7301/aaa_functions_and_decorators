import csv


def file_open(path: str) -> list:
    """
    Opens a CSV file and returns its contents as a list of lists.

    :param path: A string representing the file path of the
    CSV file to be opened.
    :return: A list of lists representing the contents of the CSV file.
    """
    with open(path, 'r', encoding='utf-8') as f:
        file = csv.reader(f, delimiter=';')
        my_list = [row for row in file]
    return my_list


def get_data(path: str) -> dict:
    """
    Parses a CSV file containing information
    about employees and returns a dictionary
    containing information about departments.

    :param path: A string representing the file path of the
    CSV file to be parsed.
    :return: A dictionary containing information about departments.
    """
    data = file_open(path)[1:]
    departments = {employer[1]: [set(), float('inf'), 0, 0, 0.0]
                   for employer in data}
    for row in data:
        departments[row[1]][0].add(row[2])
        departments[row[1]][1] = min(float(row[5]), departments[row[1]][1])
        departments[row[1]][2] = max(float(row[5]), departments[row[1]][2])
        departments[row[1]][3] += 1
        departments[row[1]][4] += float(row[5])

    return departments


def find_departments(data: dict) -> None:
    """
    Prints a list of unique departments found in the given data.

    :param data: A dictionary containing information
    about departments and their employees.
    :return: None
    """
    print('Департаменты и отделы:\n')
    for key, value in data.items():
        print(key, ':', ', '.join(value[0]))


def department_report(data: dict) -> None:
    """
    Prints a summary report of departments, including the number of
    employees, minimum and maximum salaries, and average salary.

    :param data: A dictionary containing information
    about departments and their employees.
    :return: None
    """
    print('Сводный отчёт по департаментам:\n')
    for key, value in data.items():
        print(f'{key}:\n'
              f'Количество сотрудников: {value[3]}\n'
              f'Минимальная ЗП: {value[1]}\n'
              f'Максимальная ЗП: {value[2]}\n'
              f'Средняя ЗП: {value[4] / value[3]:.2f}\n')


def save_report(data: dict) -> None:
    """
    Saves a summary report of departments to a CSV file,
    including the number of employees, minimum and maximum salaries,
    and average salary.

    :param data: A dictionary containing information
    about departments and their employees.
    :return: None
    """
    with open('department_report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Department', 'Number of Employees',
                         'Minimum Salary', 'Maximum Salary', 'Average Salary'])
        for key, value in data.items():
            writer.writerow([key, value[3], value[1],
                             value[2], round(value[4] / value[3], 2)])
    print('Отчёт сохранен в файл department_report.csv')


if __name__ == '__main__':
    path = 'Corp_Summary.csv'
    choice = input('Выберите что хотите сделать:\n'
                   '1. Вывести департаменты и все команды в нем\n'
                   '2. Вывести сводный отчёт по департаментам\n'
                   '3. Сохранить отчёт из пункта выше в формате csv\n')
    data = get_data(path)
    while choice not in ['1', '2', '3']:
        choice = input('Выберите число от 1 до 3')
    if choice == '1':
        find_departments(data)
    elif choice == '2':
        department_report(data)
    else:
        save_report(data)
