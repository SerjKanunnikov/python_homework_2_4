import os.path
import os

migrations = os.path.join(os.getcwd(), "Migrations")


def find_files():
    while True:
        for file in os.listdir(migrations):
            if file.endswith(".sql"):
                check_file = open(os.path.join(migrations, file))

        files_list = []
        search_line = input("Вводи")
        for file in os.listdir(migrations):
            if file.endswith(".sql"):
                check_file = open(os.path.join(migrations, file))
                if search_line in check_file.read():
                    files_list.append(os.path.join(migrations, file))
                    print(os.path.join(migrations, file))
        print(files_list)


if __name__ == '__main__':
    find_files()
pass
