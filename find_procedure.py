import os.path
import os


def filter_list(files_list):
    search_line = input("Вводи\n")
    for file in files_list:
        check_file = open(os.path.join(migrations, file), encoding="utf-8")
        if search_line in check_file.read():
            sql_list.append(file)
    print(sql_list)
    files_list = sql_list
    print(files_list)
    return files_list

if __name__ == '__main__':
    migrations = os.path.join(os.getcwd(), "Migrations")
    files_list = [file for file in os.listdir(migrations) if file.endswith(".sql")]
    # print(files_list)
    while True:
        sql_list = []
        files_list = filter_list(files_list)

