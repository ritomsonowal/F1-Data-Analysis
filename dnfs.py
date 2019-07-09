import matplotlib.pyplot as plt
import numpy as np
import pandas
import matplotlib
matplotlib.use('tkagg')
plt.rcdefaults()


# clean status csv
df_status = pandas.read_csv('csv_files/status.csv',
                            names=['S-ID', 'Status'])

df_status = df_status.set_index("S-ID", drop=False)

# clean race results csv
df_results = pandas.read_csv('csv_files/results.csv',

                             names=['Res-ID', 'R-ID', 'D-ID', 'C-ID', 'Number', 'Grid', 'Position', 'PositionText', 'PositionOrder',
                                    'Points', 'Laps', 'Time', 'Milliseconds', 'FastestLap', 'Rank', 'FastestLapTime', 'FastestLapSpeed', 'S-ID'],
                             )

df_races = pandas.read_csv('csv_files/races.csv',
                           names=['R-ID', 'Year', 'Round', 'Cir-ID',
                                  'Name', 'Date', 'Time', 'URL'])

# INNER JOIN RESULTS AND RACES
df_inner = pandas.merge(left=df_results, right=df_races,
                        on="R-ID", how="inner")

# 1950-1980 vs 1980-2010 vs 2010-2019
section1 = {}
section2 = {}
section3 = {}

for index, row in df_inner.iterrows():
    status_id = row['S-ID']
    year = row['Year']
    if status_id in [11,12,13,14,15,16,17,18]:
        continue
    if year >= 1950 and year < 1980:
        if status_id not in section1.keys():
            section1[status_id] = 1
        else:
            section1[status_id] += 1
    elif year >= 1980 and year < 2010:
        if status_id not in section2.keys():
            section2[status_id] = 1
        else:
            section2[status_id] += 1
    else:
        if status_id not in section3.keys():
            section3[status_id] = 1
        else:
            section3[status_id] += 1

# clean the data
x = []
y = [[] for _ in range(3)]

for i in range(1,137):
    if i in df_status['S-ID'] and i in section1.keys() and i in section2.keys() and i in section3.keys() and (section1[i]+section2[i]+section3[i] > 150):
        x.append(df_status.at[i, 'Status'])
        if i in section1.keys():
            y[0].append(section1[i])
        else:
            y[0].append(0)
        if i in section2.keys():
            y[1].append(section2[i])
        else:
            y[1].append(0)
        if i in section3.keys():
            y[2].append(section3[i])
        else:
            y[2].append(0)

# print(section1)
# print(section2)

# create plot
fig, ax = plt.subplots()
index = np.arange(len(y[0]))
bar_width = 0.15
opacity = 0.8

rects1 = plt.bar(index, y[0], bar_width,
                 alpha=opacity,
                 color='#00CED1',
                 label='1950-1980')

rects2 = plt.bar(index + bar_width, y[1], bar_width,
                 alpha=opacity,
                 color='#DC143C',
                 label='1980-2010')

rects3 = plt.bar(index + bar_width + bar_width, y[2], bar_width,
                 alpha=opacity,
                 color='#FF8C00',
                 label='2010-present')

plt.xlabel('Status')
plt.ylabel('Instances')
plt.title('DNF Trend Over 69 Years')
plt.xticks(index + bar_width, tuple(x))
plt.legend()

plt.tight_layout()
plt.show()
#
# plt.show()
