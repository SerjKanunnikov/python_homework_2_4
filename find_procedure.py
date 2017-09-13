import os.path
import os


def filter_list(files_list):
    sql_list = []
    search_line = input("Введите слово для поиска:\n")
    for file in files_list:
        check_file = open(os.path.join(migrations, file), encoding="utf-8")
        if search_line in check_file.read():
            sql_list.append(file)
            print(os.path.abspath(file))
    files_list = sql_list
    print("Всего:", len(sql_list))
    return files_list


if __name__ == '__main__':
    migrations = "Migrations"
    files_list = [file for file in os.listdir(migrations) if file.endswith(".sql")]
    while True:
        files_list = filter_list(files_list)