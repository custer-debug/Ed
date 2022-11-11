# from collections import Counter
from json import load
from openpyxl import load_workbook
import pandas as pd
from random import choice
feedback_src = r'C:\Users\romak\Desktop\Diplom\Feedback.xlsx'
students_src = r'C:\Users\romak\Desktop\Diplom\Students.xlsx'
education_names = [
    'Автоматизация технологических процессов и производств',
    'Информационные системы и технологии',
    'Прикладная информатика',
    'Машиностроение',
    'Юриспруденция',
    'Информационная безопасность',
    'Архитектура',
    'Бизнес-информатика',
    'Теплоэнергетика и теплотехника',
    'Лингвистика'
]
df = pd.read_excel(students_src,sheet_name='all')
rating = [3,4,5]
yes_or_no = ['Да','Нет']
complexity = ['Легко','Тяжко идёт']
wb = load_workbook(feedback_src)

def write_to_excel(l:list):
    ws = wb['test']
    ws.append(l)


def generate_random_data():
    for i in range(1000):
        ed = choice(education_names)
        code = df.loc[df.Name == ed,'Code'].values[0]
        write_to_excel([ed,code,choice(complexity), choice(rating), choice(yes_or_no), choice(yes_or_no)])
        # print(f'{ed} ({code}) {choice(complexity)} {choice(rating)} {choice(yes_or_no)} {choice(yes_or_no)}')


def main():
    # code = df.loc[df.Name == ed,'Code'].values[0]
    generate_random_data()
    wb.save(feedback_src)



if __name__ == '__main__':
    main()
