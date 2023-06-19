import os
import csv


daily_temperatures = [
    [68, 65, 71, 57, 62, 58],
    [57, 60, 66, 73, 59, 60],
    [61, 60, 66, 73, 59, 60],
]

if not os.path.exists('/media/giocatory/hard_out_disk/python_projects/remembering_python/book_Den_Beider/work_with_modules'):
    os.mkdir('/media/giocatory/hard_out_disk/python_projects/remembering_python/book_Den_Beider/work_with_modules')

if not os.access("/media/giocatory/hard_out_disk/python_projects/remembering_python/book_Den_Beider/work_with_modules/documents/doc.csv", mode=os.F_OK):
    os.system("touch /media/giocatory/hard_out_disk/python_projects/remembering_python/book_Den_Beider/work_with_modules/documents/doc.csv")
