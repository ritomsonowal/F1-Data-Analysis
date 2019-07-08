import pandas

df = pandas.read_csv('csv_files/constructors.csv',
                     names=['C-ID', 'Alias', 'Name', 'Nationality', 'URL'])

df = df.set_index("C-ID", drop=False)

print(df)
