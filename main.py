
if __name__ == '__main__':
    from application import salary, codingshow
    from application.db import people

    salary.calculate_salary()
    people.get_employees()

    print('')
    print('Кодировка сайта https://dzen.ru')
    print(codingshow.get_coding_url('https://dzen.ru'))

    print('')
    print('Кодировка файла requirements.txt')
    print(codingshow.get_coding_file('requirements.txt'))
