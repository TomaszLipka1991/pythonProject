import numpy as np
import pandas as pd
# klasa series - tablica danych

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(data.index)
#print(data.values)
# roznica miedzy array a eries - mozna samemu ustawic indeksy
# data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                  index = ['a', 'b', 'c', 'd'])
# print(data)
# print(type(data.index))
# print(data['b'])
# data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                  index=[2, 5, 3, 7])  # indeksy są liczbami, ale nie muszą mieć konkretnej kolejności
# print(data)

# licba ludnosci-  tworzymy slownik stan: ilosc mieszkancow i slownik wrzucamy do Series
# population_dict = {'California': 38332521,
#                    'Texas'     : 26448193,
#                    'New York'  : 19651127,
#                    'Florida'   : 19552860,
#                    'Illinois'  : 12882135}
# population = pd.Series(population_dict)
# print(population)
# print(population['California'])
# # mozemy dalej korzystac z operacji dla tablic np. slice
# print(population['California':'Illinois'])

# tworzenie obiektow series

# print(pd.Series([2, 4, 6]))  # z listy))
# b = pd.Series(5, index=[1, 2, 3])  # jako jedna wartość, która jest powtarzana dla indeksów
# print(b)
# c = pd.Series({2: 'a', 1: 'b', 3: 'c'})  # ze słownika
# print(c)
# object taka super klasa malo wydajna
# d = pd.Series(np.arange(10))  # z tablicy numpy
# print(d)
#DataFrame
# area_dict = {'California': 423967,
#              'Texas'     : 695662,
#              'New York'  : 141297,
#              'Florida'   : 170312,
#              'Illinois'  : 149995}
# area = pd.Series(area_dict)
#
# population_dict = {'California': 38332521,
#                    'Texas'     : 26448193,
#                    'New York'  : 19651127,
#                    'Florida'   : 19552860,
#                    'Illinois'  : 12882135}
# population = pd.Series(population_dict)
#
# states = pd.DataFrame({
#     'population': population,
#     'area'      : area
# })
# # print(states)
# print(states.index)
# print(states.columns)
# data = [{'a': i, 'b': 2 * i} for i in range(3)]
# # data
# f = pd.DataFrame(data)  # z listy słowników
# print(f)
# g = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])  # pandas sam wypełni brakujące indeksy
# print(g)

# h = pd.DataFrame(
#     np.random.rand(3, 2),
#     columns=['foo', 'bar'],
#     index=['a', 'b', 'c']
# )  # z dwuwymiarowej tablicy numpy
# print(h)

# Index
# ind = pd.Index([2,3,5,7,11])
# print(ind)
# ind[1] = 0

# # indeksowanie i wybieranie danych
# data = pd.Series(['a','b','c'], index = [1,3,5])
# print(data)
# print(data[1]) #indeks series
# print(data[1:3]) #indeks z numpy
# lepiej jawnie powiedziec który chcemy indeks za pomoca atrybutow loc i iloc
# loc uzywa indeksu z Series
# print(data.loc[1])
# print(data.loc[1:3])
# # iloc z numpy
# print(data.iloc[1])
# print(data.iloc[1:3])

# wybieranie danych z DataFrame
area = pd.Series({
    'California': 423967,   'Texas'  : 695662,
    'New York'  : 141297,   'Florida': 170312,
    'Illinois'  : 149995
})
pop = pd.Series({
    'California': 38332521, 'Texas'  : 26448193,
    'New York'  : 19651127, 'Florida': 19552860,
    'Illinois'  : 12882135
})
data = pd.DataFrame({'area':area, 'pop':pop})
# print(data)
# print(data['area'])
data['density'] = data['pop']/data['area']
# print(data) #i to jest plus bo mamy to od razu  nie jakimis petlami!
# print(data.iloc[:3, :2])
# print(data.loc[:'Texas', :'pop'])
# print(data.loc[data.density >100, ['pop', 'density']])
# data.iloc[0,2] = 90 #zmieniamy wartosc pod wskazanym indeksem
# print(data)

# # operowanie na brakujacych danyc NaN
# vals1 = np.array([1, None, 3,4])
# # print(vals1)
# # print(vals1.dtype)
# vals2 = np.array([1, np.nan,3,4])
# print(vals2)
# print(vals2.dtype)
# print(vals2.sum())
# # 'omijanie nan-ow
# print(np.nansum(vals2)) #podobnie nunmin, nunmax

# nan i none w panda
# p = pd.Series([1, np.nan, 2, None])
# print(p)
# 0    1.0
# 1    NaN
# 2    2.0
# 3    NaN
# dtype: float64


data =  pd.Series([1, np.nan, 'hello', None])
# print(data)
#
# 0        1
# 1      NaN
# 2    hello
# 3     None
# dtype: object


# print(data.isnull())  # znajdowanie pustych wartości
#
# 0    False
# 1     True
# 2    False
# 3     True
# dtype: bool

# print(data[data.notnull()])
# 0        1
# 2    hello
# dtype: object
#
# print(data.dropna())  # usuwanie pustych wartości
# print(data.fillna(0) ) # wypełnianie pustych wartości
# 0        1
# 1        0
# 2    hello
# 3        0
# dtype: object
# ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
# ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
# cc = pd.concat([ser1, ser2])
# print(cc)
#
# 1    A
# 2    B
# 3    C
# 4    D
# 5    E
# 6    F
# dtype: object

def make_df(cols, ind):
    """Stwórz DataFrame z kombinacji cols i ind"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)
# a = make_df('ABC', range(2))
# print(a)

df1 = make_df('AB', [1,2])
# print(df1)
#     A   B
# 1  A1  B1
# 2  A2  B2
df2 = make_df('AB', [3,4])
cc2 = pd.concat([df1, df2]) #łaczenie po wierszach
# print(cc2)
#     A   B
# 1  A1  B1
# 2  A2  B2
# 3  A3  B3
# 4  A4  B4
cc3 = pd.concat([df1, df2], axis=1)
# print(cc3)
#      A    B    A    B
# 1   A1   B1  NaN  NaN
# 2   A2   B2  NaN  NaN
# 3  NaN  NaN   A3   B3
# 4  NaN  NaN   A4   B4

# aap1= df1.append(df2)
# print(aap1) #warning bo append niedługo zostanie usuniety

#joiny :) tytlo tutaj pd.merge

df1 = pd.DataFrame({'employee': ['Bob',        'Jake',        'Lisa',        'Sue'],
                    'group'   : ['Accounting', 'Engineering', 'Engineering', 'HR' ]})
# print(df1)

df2 = pd.DataFrame({'employee' : ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [ 2004,   2008,  2012,   2014]})

df3 = pd.merge(df1,df2) #stara sie po pirwszej kolumnie ale mozna wymusic ktora kolumna bedzie łączyc
# print(df3)

#   employee        group  hire_date
# 0      Bob   Accounting       2008
# 1     Jake  Engineering       2012
# 2     Lisa  Engineering       2004
# 3      Sue           HR       2014
#
df4 = pd.DataFrame({'group'     : ['Accounting', 'Engineering', 'HR'   ],
                    'supervisor': ['Carly',      'Guido',       'Steve']})
df41 = pd.merge(df3, df4)
# print(df41)
#
#   employee        group  hire_date supervisor
# 0      Bob   Accounting       2008      Carly
# 1     Jake  Engineering       2012      Guido
# 2     Lisa  Engineering       2004      Guido
# 3      Sue           HR       2014      Steve

df5 = pd.DataFrame({
    'group' : [
        'Accounting',
        'Accounting',
        'Engineering',
        'Engineering',
        'HR',
        'HR'],
    'skills': [
        'math',
        'spreadsheets',
        'coding',
        'linux',
        'spreadsheets',
        'organization']
})

df51 = pd.merge(df1, df5)
# print(df51)
# 0      Bob   Accounting          math
# 1      Bob   Accounting  spreadsheets
# 2     Jake  Engineering        coding
# 3     Jake  Engineering         linux
# 4     Lisa  Engineering        coding
# 5     Lisa  Engineering         linux
# 6      Sue           HR  spreadsheets
# 7      Sue           HR  organization

# jezeli chcemy miec pewnosc poprawnego łączenie to parametr on:
# print(pd.merge(df1, df2, on='employee'))
# 0      Bob   Accounting       2008
# 1     Jake  Engineering       2012
# 2     Lisa  Engineering       2004
# 3      Sue           HR       2014

df31 = pd.DataFrame({
    'name': [
        'Bob',
        'Jake',
        'Lisa',
        'Sue'],
    'salary': [
        70000,
        80000,
        120000,
        90000]})
# print(pd.merge(df1, df31, left_on = 'employee', right_on = 'name').drop('name', axis=1))
#   employee        group  salary
# 0      Bob   Accounting   70000
# 1     Jake  Engineering   80000
# 2     Lisa  Engineering  120000
# 3      Sue           HR   90000


df1 = make_df('AB', [1, 2, 4])
df2 = make_df('ABCD', [1, 2, 5, 6])
# print(df1)
# print(df2)
#df1 left join df2:

# print(pd.merge(df1, df2, on='A', how='left'))
#     A B_x  B_y    C    D
# 0  A1  B1   B1   C1   D1
# 1  A2  B2   B2   C2   D2
# 2  A4  B4  NaN  NaN  NaN

# right
# print(pd.merge(df1, df2, on='A', how='right'))
#     A  B_x B_y   C   D
# 0  A1   B1  B1  C1  D1
# 1  A2   B2  B2  C2  D2
# 2  A5  NaN  B5  C5  D5
# 3  A6  NaN  B6  C6  D6

# outer
# print(pd.merge(df1, df2, on='A', how='outer'))
#     A  B_x  B_y    C    D
# 0  A1   B1   B1   C1   D1
# 1  A2   B2   B2   C2   D2
# 2  A4   B4  NaN  NaN  NaN
# 3  A5  NaN   B5   C5   D5
# 4  A6  NaN   B6   C6   D6

# inner
# print(pd.merge(df1, df2, on='A', how='inner'))
#     A B_x B_y   C   D
# 0  A1  B1  B1  C1  D1
# 1  A2  B2  B2  C2  D2

# agregacja i grupowanie
#
# df = pd.DataFrame({
#     'A': np.random.rand(5),
#     'B': np.random.rand(5)
# })
# print(df)
# print(df.mean())

df = pd.DataFrame(
    {
        'key' : ['A', 'B', 'C', 'A', 'B', 'C'],
        'data': range(6)
    },
    columns=['key', 'data']
)

# print(df)
# print(df.groupby('key'))
# print(df.groupby('key').sum())
#      data
# key
# A       3
# B       5
# C       7

print(df.groupby('key')['data'].median())