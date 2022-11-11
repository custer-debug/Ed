import pandas as pd
import matplotlib.pyplot as plt

src = r'C:\Users\romak\Desktop\Diplom\Students.xlsx'
df = pd.read_excel(src,sheet_name='data_set')
years = [f'{s}_year' for s in range(2015,2020)]



def get_data(education:str)->list:
    data = []
    for year in years:
        data.append(int(df.loc[df.Name == education,year].values))
    return data


def main():
    area_education_name = 'Юриспруденция'
    data = get_data(area_education_name)
    print(data)
    # plt.bar(years,data)
    # plt.title(area_education_name)
    # plt.set_title(education)
    # plt.show()



if __name__ == '__main__':
    main()
