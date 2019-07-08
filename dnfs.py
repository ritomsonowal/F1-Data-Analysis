import pandas
import matplotlib
matplotlib.use('tkagg')
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


# clean status csv
df_status = pandas.read_csv('csv_files/status.csv',
                            names=['S-ID', 'Status'])

df_status = df_status.set_index("S-ID", drop=False)

# clean race results csv
iter_csv = pandas.read_csv('csv_files/results.csv',

                           names=['Res-ID', 'R-ID', 'D-ID', 'C-ID', 'Number', 'Grid', 'Position', 'PositionText', 'PositionOrder',
                                  'Points', 'Laps', 'Time', 'Milliseconds', 'FastestLap', 'Rank', 'FastestLapTime', 'FastestLapSpeed', 'S-ID'],
                           iterator=True,
                           chunksize=1000)
df_dnfs = pandas.concat([chunk[chunk['S-ID'] > 2] for chunk in iter_csv])

dnf_num = {}

for index, row in df_dnfs.iterrows():
    status_id = row['S-ID']
    if status_id not in dnf_num.keys():
        dnf_num[status_id] = 1
    else:
        dnf_num[status_id] += 1

# for i in range(137):
#     if i in dnf_num.keys() and dnf_num[i] >= 50:
#         print("Driver DNFed ", dnf_num[i], "times for ",
#               df_status.loc[i, 'Status':'Status'])

x = []
y = []

for i in range(137):
    if i in dnf_num.keys() and dnf_num[i] >= 100:
        x.append(df_status.at[i,'Status'])
        y.append(dnf_num[i])
        # print("Driver DNFed ", dnf_num[i], "times for ",
        # df_status.loc[i, 'Status':'Status'])
print(x)
y_pos = np.arange(len(x))
plt.barh(x, y, align='center', alpha = 0.5)
plt.yticks(y_pos, x)
plt.xlabel('Total DNFs')
plt.title('DNF Status')

plt.show()

# print(df_status)
