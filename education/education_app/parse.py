from pandas import read_excel
from collections import Counter


def parse_excel_std_fb(education:str)->list:
    src = r'C:\Users\romak\Desktop\Diplom\Ed\education\Others\Feedback.xlsx'
    df = read_excel(src,sheet_name='test')
    result = {}
    for item in df.columns[2:]:
        l = df.loc[(df.Name == education),item].values
        c = Counter(l)
        result[item] = {i: round(c[i] / len(l) * 100.0,2) for i in c}
    result['Count'] = df.loc[(df.Name == education),'Name'].count()
    return result



from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from re import findall
from collections import Counter


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}


# Поиск чисел в строке
def find_integers(string:str) -> list:
    return [int(s) for s in findall(r'-?\d+\.?\d*', string)]

# Конкатенация чисел в одно
def concatenation_int(digits:list) -> int:
    return int(''.join(map(str, digits)))


# Сохранение разряда  l=[132,0] -> l[132,0,0,0] для конкатенации
def save_discharge(l:list) -> list:
    try:
        if l[1] == 0:
            l.append(0)
            l.append(0)
        if len(str(l[0])) == 2 and len(str(l[1])) == 2:
            l.insert(1,0)
    except Exception as ex:
        print(ex)
    return l


# Получение страницы
def execute(url) :
    return BeautifulSoup(
        requests.get(
            url=url,
            headers=headers).content,
        'html.parser')


def delete_two_last_elements(tmp:list)->list:
    if len(tmp) == 4:
        tmp.pop(-1)
        tmp.pop(-1)
    return tmp


class WebSite:
    def __init__(self,education:str) -> None:
        self.params_vacancy = {
            'text':education,
            'area':'113',
            'experience':'noExperience',
            'only_with_salary':'true',
            'items_on_page':'20',
            'page':'0'
        }

        self.params_resume = {
            'area':'113',
            'experience':'noExperience',
            'age_from':'18',
            'age_to':'24',
            'job_search_status':'active_search',
            'text':education,
            'exp_period':'all_time',
            'logic':'normal',
            'pos':'full_text',
            'page':'1'
        }

    def generate_url_vacancy(self):
        return f"{'https://hh.ru/search/vacancy?'}{urlencode(self.params_vacancy)}"

    def generate_url_resume(self):
        return f"{'https://hh.ru/search/resume?'}{urlencode(self.params_resume)}"



class CrawlerHH:
    def __init__(self,site:WebSite) -> None:
        self.site = site
        self.count_resume = 0       # количество резюме
        self.pages = 1              # количество страниц
        self.count_vacancy = 0      # количество вакансий
        self.salary = []            # заработная плата
        self.cities = []
        self.resumes = []
        # self.get_resume_info()
        self.get_vacancy_info()

    def get_count_resume(self):
        self.count_resume = concatenation_int(
            delete_two_last_elements(save_discharge(
                find_integers(
                    self.soup.find('div',{'class':'bloko-header-section-3'}).text)
        )))

    def get_resume_title(self):
        for i in self.soup.find_all('a',{'class':'serp-item__title'}):
            self.resumes.append(i.text)

    def get_resume_info(self):
        for i in range(2):
            self.site.params_resume['page'] = str(i)
            self.soup = execute(self.site.generate_url_resume())
            self.get_count_resume()
            self.get_resume_title()


    def run_functions_vacancy(self):
        self.soup = execute(self.site.generate_url_vacancy())  # Получение страницы
        self.get_count_vacancy()
        self.get_pages()
        self.get_salary()
        # self.get_cities()


    def get_vacancy_info(self):
        print(f'Считывание страницы: {1}')
        self.run_functions_vacancy()

        if self.pages == 1:
            return

        for i in range(self.pages-1):
            self.site.params_vacancy['page'] = str(i+1)
            self.run_functions_vacancy()
            print(f'Считывание страницы: {i+2}')


    # Получение названия городов
    def get_cities(self):
        for i in (self.soup.find_all('div',{'data-qa':'vacancy-serp__vacancy-address'})):
            tmp = i.text.split(sep=',')
            if len(tmp) == 2:
                tmp.pop(-1)
            self.cities.append(tmp[0])


    # Получение количество вакансий
    def get_count_vacancy(self) -> None:
        try:
            string_vacancy = self.soup.find('h1').text
        except AttributeError:
            self.count_vacancy = 0
        self.count_vacancy = concatenation_int(find_integers(string_vacancy))


    # Получение количества страниц
    def get_pages(self) -> int:
        self.pages = int(self.count_vacancy / 20)
        if self.count_vacancy % 20 > 0:
            self.pages += 1


    # Получение данных о заработной плате
    def get_salary(self) -> None:
        for item in self.soup.find_all(name='span',attrs={'class':'bloko-header-section-3'}):
            tmp = delete_two_last_elements(find_integers(item.text))
            self.salary.append(concatenation_int(save_discharge(tmp)))




    def print_info(self):
        print(f'Количество вакансий: {self.count_vacancy}')
        # print(f'Количество резюме: {self.count_resume}')
        print(f'Минимальная зарплата: {min(self.salary)}  рублей')
        print(f'Максимальная зарплата: {max(self.salary)} рублей')
        # print(f'Города в которых требуются люди с таким направлением: {Counter(self.cities).most_common(5)}')
        # print(f'Распространённые резюме людей окончивших это направление: {Counter(self.resumes).most_common(3)}')




def parse_headhunter(ed:str):
    c = CrawlerHH(
        WebSite(ed)
    )
    c.print_info()
    return {
        'count_vacancy':c.count_vacancy,
        'min_salary':min(c.salary),
        'max_salary':max(c.salary),
        # 'max_salary':max(c.salary),
    }


# print(parse_headhunter('Архитектура'))
