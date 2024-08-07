import pandas as  pd
import numpy as  np

my_index = ['A','B', 'C']
my_columns = ['이름', '나이', '성별']
my_data = np.array([['Alice','Bob','홍길동'],
                       [25,30,26],
                       ['남', '여', '남']]).transpose()

df = pd.DataFrame(my_data, index = my_index, columns = my_columns)
# print(df[['나이', '이름']])

print(df, "\n", df.loc["A"])
# print(df, df.shape)