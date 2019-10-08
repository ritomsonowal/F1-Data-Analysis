import wget
import os, shutil
import zipfile

print('===================================')
print('Updating CSV files')
print('===================================')

# Remove outdated files
folder = 'csv_files/'
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

# Download csv zip
url = 'http://ergast.com/downloads/f1db_csv.zip'

wget.download(url, 'csv_files/')

# Unzip csv files
zip_path = 'csv_files/f1db_csv.zip'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(folder)

# Delete zip file
os.remove('csv_files/f1db_csv.zip')

