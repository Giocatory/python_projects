path = "files_to_testing/list_of_file_formats.txt"

with open(path, mode="r", encoding="utf-8") as file:
    formats = file.readlines()
    print(f"All file formats: {len(formats)}")

# All file formats: 1813

# popular types
with open("files_to_testing/list_of_file_popular_types.txt", mode="r", encoding="utf-8") as file:
    popular_types = file.readlines()
    for line in popular_types:
        s = line.split(";")
        print(f"{s[0]}:\t{s[1]}", end="")
# Тип:	Формат
# Изображение:	jpg,png,gif,bmp,tif
# Документ:	doc,docx,odt,rtf
# Электронная таблица:	xls,xlsx,csv
# PDF:	pdf
# Текстовый фаил:	txt,json,xml,csv
# Архив:	zip,rar,gzip,apk,deb,rpm
# Аудио файл:	mp3,wav,midi,aac
# Видео фаил:	mp4,avi,mkv,wmv,flv,mpeg
# Страница интернет:	html,php,mht
# Презентация:	ppt,pptx
# Базы данных:	sql,db,mdb,dbf,mdf
# Образ диска:	iso,sdi,cif
# Векторные изображения:	svg,cdr
# Торрент файлы:	torrent
# Сканированный документ:	djvu
# Электронная книга:	fb2,epub,mobi
# Программы:	exe,msi,sh
# Объектный код:	a,a.out.elf,dll
# Биометрия:	cbf,ebf,cbfx,ebfx
# Виртуальные машины:	vdi,vsv,vmc,vhd
# Двоичные файлы:	bak,bk,bin,dsk,raw
# Временные файлы:	temp,tmp
