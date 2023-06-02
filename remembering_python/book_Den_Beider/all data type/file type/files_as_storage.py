path = "files_to_testing/list_of_file_formats.txt"

with open(path, mode="r", encoding="utf-8") as file:
    formats = file.readlines()
    print(f"All file formats: {len(formats)}")

# All file formats: 1813
