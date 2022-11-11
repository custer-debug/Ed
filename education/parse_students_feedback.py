import pandas as pd
from collections import Counter

src = r'Others\Feedback.xlsx'
df = pd.read_excel(src,sheet_name='test')

def parse_excel(education:str)->list:
    result = {}
    for item in df.columns[2:]:
        l = df.loc[(df.Name == education),item].values
        c = Counter(l)
        result[item] = {i: round(c[i] / len(l) * 100.0,2) for i in c}

    result['Count'] = df.loc[(df.Name == education),'Name'].count()
    return result



def main():
    r = parse_excel('Машиностроение')
    print(r)



if __name__ == '__main__':
    main()
