import pandas as  pd
# 시각화하려면 아래의 저거 불러와야됨
import matplotlib.pyplot as plt

col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names = col_names)

print(data.describe().to_csv('./results/describe.csv'))


# # 시각화 데이터
# plt.clf()
# plt.hist(data['age'])
# plt.show()
# plt.savefig("./age.png")

# print(data['preg'])
# # 상의 5명만 뽑아와
# print(data['preg'].head(5))
# print(data.head(5))
#
# # 요약을 해보는 거
# print(data.describe())