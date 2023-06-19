import os
import csv


daily_temperatures = [
    [68, 65, 71, 57, 62, 58],
    [57, 60, 66, 73, 59, 60],
    [61, 60, 66, 73, 59, 65],
]

dir_path = '/media/giocatory/hard_out_disk/python_projects/remembering_python/work_with_modules/documents'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

file_path = "/media/giocatory/hard_out_disk/python_projects/remembering_python/work_with_modules/documents/doc.csv"
if not os.access(file_path, mode=os.F_OK):
    os.system(f"touch {file_path}")


with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    writer.writerows(daily_temperatures)

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# ['68', '65', '71', '57', '62', '58']
# ['57', '60', '66', '73', '59', '60']
# ['61', '60', '66', '73', '59', '65']

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# {'Monday': '68', 'Tuesday': '65', 'Wednesday': '71', 'Thursday': '57', 'Friday': '62', 'Saturday': '58'}
# {'Monday': '57', 'Tuesday': '60', 'Wednesday': '66', 'Thursday': '73', 'Friday': '59', 'Saturday': '60'}
# {'Monday': '61', 'Tuesday': '60', 'Wednesday': '66', 'Thursday': '73', 'Friday': '59', 'Saturday': '65'}
