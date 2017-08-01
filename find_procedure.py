import os.path
import os

migrations = os.path.join(os.getcwd(), "Migrations")


def find_files():
    files_list = (file for file in os.listdir(migrations) if file.endswith(".sql"))
    return files_list


def filter_list(files_list):
    sql_list = []
    search_line = input("Вводи\n")
    for file in files_list:
        check_file = open(os.path.join(migrations, file), encoding="utf-8")
        if search_line in check_file.read():
            sql_list.append(os.path.join(migrations, file))
    # new_list = sql_list
    # for file in new_list:
    #     check_file = open(os.path.join(migrations, file), encoding="utf-8")
    #     if search_line in check_file.read():
    #         sql_list.append(os.path.join(migrations, file))
    print(sql_list)


if __name__ == '__main__':
    while True:
        filter_list(find_files())
pass
