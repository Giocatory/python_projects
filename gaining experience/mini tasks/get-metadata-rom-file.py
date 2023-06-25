import time
import os


path = "gaining experience/mini tasks/simple-text.txt"

# file size
file_size = os.path.getsize(path)
print(file_size)  # 18285 (в байтах)

# file modification time
file_modification_time = time.ctime(os.path.getmtime(path))
print(file_modification_time)  # Sun Jun 25 16:42:29 2023
file_mta = file_modification_time.split(" ")
print(f"{file_mta[2]} {file_mta[1]} ({file_mta[0]}): {file_mta[3]} ({file_mta[4]} year)")  # 25 Jun (Sun): 16:42:29 (2023 year)

# file name
file_name = os.path.basename(path)
print(file_name)  # simple-text.txt

# file real path
file_real_path = os.path.realpath(path)
print(file_real_path)  # /media/giocatory/hard_out_disk/python_projects/gaining experience/mini tasks/simple-text.txt
