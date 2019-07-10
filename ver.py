import matplotlib.pyplot as plt
import numpy as np
import pandas
from math import pi
import matplotlib
matplotlib.use('tkagg')
plt.rcdefaults()

# Helper Function to create the data for Radar

def createData(d_id, df_results):
    case = 'D_ID == ' + d_id
    df_driver = df_results.query(case)

    df_wins = df_driver.query('PositionText == "1"')

    df_podiums = df_driver.query('PositionText in ["1","2","3"]')

    df_poles = df_driver.query('Grid == 1')

    df_points = df_driver.query('PositionOrder <= 10')

    df_dnfs = df_driver.query('S_ID != 1')

    wins = len(df_wins.index)
    podiums = len(df_podiums.index)
    poles = len(df_poles.index)
    points = len(df_points.index)
    dnfs = len(df_dnfs.index)

    races = len(df_driver.index)

    data = [wins, podiums, poles, points, dnfs]

    data = [x * 100 / races for x in data]

    return data

# Function to create individual Radar Plots

def createRadar(driver, data):
    Attributes = ["Wins", "Podiums", "Poles", "Points", "DNFs"]

    data += data[:1]

    angles = [n / 5 * 2 * pi for n in range(5)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1], Attributes, color='grey', size=10)
    ax.plot(angles, data)
    ax.fill(angles, data, 'blue', alpha=0.1)

    ax.set_title(driver)
    plt.show()


# Function to compare radar plots

def createRadar2(driver, data, driver2, data2):
    Attributes = ["Wins", "Podiums", "Poles", "Points", "DNFs"]

    data += data [:1]
    data2 += data2 [:1]

    angles = [n / 5 * 2 * pi for n in range(5)]
    angles += angles [:1]

    angles2 = [n / 5 * 2 * pi for n in range(5)]
    angles2 += angles2 [:1]

    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1],Attributes)

    ax.plot(angles,data)
    ax.fill(angles, data, 'teal', alpha=0.1)

    ax.plot(angles2,data2)
    ax.fill(angles2, data2, 'red', alpha=0.1)

    #Rather than use a title, individual text points are added
    plt.figtext(0.2,0.9,driver,color="teal")
    plt.figtext(0.2,0.85,"v")
    plt.figtext(0.2,0.8,driver2,color="red")
    plt.show()

# clean drivers csv
df_drivers = pandas.read_csv('csv_files/drivers.csv',
                             names=['D_ID', 'Alias', 'Number', 'Code', 'Forename', 'Surname', 'DOB', 'Nationality', 'URL'])

# df_drivers = df_drivers.set_index("D_ID", drop=False)

# clean race results csv
df_results = pandas.read_csv('csv_files/results.csv',

                             names=['Res_ID', 'R_ID', 'D_ID', 'C_ID', 'Number', 'Grid', 'Position', 'PositionText', 'PositionOrder',
                                    'Points', 'Laps', 'Time', 'Milliseconds', 'FastestLap', 'Rank', 'FastestLapTime', 'FastestLapSpeed', 'S_ID'],
                             )

df_races = pandas.read_csv('csv_files/races.csv',
                           names=['R_ID', 'Year', 'Round', 'Cir_ID',
                                  'Name', 'Date', 'Time', 'URL'])

# Schumacher ID _ 30
# Ayrton Senna ID _ 102
# Lewis Hamilton ID _ 1
# Sebastian Vettel ID _ 20
# Verstappen ID _ 830

# --------------------INDIVIDUAL STATS---------------------
# Michael Schumacher

data = createData('30',df_results)
createRadar('Michael Schumacher', data)

# Ayrton Senna

data = createData('102',df_results)
createRadar('Ayrton Senna', data)

# Lewis Hamilton

data = createData('1',df_results)
createRadar('Lewis Hamilton', data)

# Sebastian Vettel

data = createData('20',df_results)
createRadar('Sebastian Vettel', data)

# Max Verstappen

data = createData('830', df_results)
createRadar('Max Verstappen', data)

# ------------------------HEAD-TO-HEAD------------------------

# Michael Schumacher vs Max Verstappen
data = createData('30',df_results)
data2 = createData('830',df_results)

createRadar2('Schumacher', data, 'Verstappen', data2)

# Ayrton Senna vs Max Verstappen
data = createData('102',df_results)
data2 = createData('830',df_results)

createRadar2('Senna', data, 'Verstappen', data2)

# Lewis Hamilton vs Max Verstappen
data = createData('1',df_results)
data2 = createData('830',df_results)

createRadar2('Hamilton', data, 'Verstappen', data2)

# Sebastian Vettel vs Max Verstappen
data = createData('20',df_results)
data2 = createData('830',df_results)

createRadar2('Vettel', data, 'Verstappen', data2)
