import os
from xmlrpc.client import DateTime
import sys
import csv
import shutil


class Wit:

    def __init__(self):
        self.__path = os.getcwd()
        self.__wit_path = os.path.join(self.__path, ".wit")
        self.__user_name = ''
        self.__user_email = ''

    # region init
    def init(self):
        try:
            path = self.__path
            wit = os.path.join(path, ".wit")

            if os.path.exists(wit):
                print(".wit folder already exists.")
            else:
                self.init_wit_folder(wit)
                print(".wit folder initialized.")
        except Exception as e:
            print(e)


    def init_wit_folder(self, path):
        try:
            path += "\\" + "repository"
            os.makedirs(path)
            path = os.path.dirname(path)
            with open(self.__wit_path + "\\details.csv", 'w', newline='') as csvfile:
                fieldnames = ['hash', 'date', 'message']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            csvfile.close()
            path += "\\" + "staging_copy"
            os.makedirs(path)
        except Exception as e:
            print(e)

    # endregion

    # region add
    def add(self, name):
        try:
            path = self.__path
            path += "\\" + name
            new_path = self.__path + "\\" + ".wit\\staging_copy\\" + name
            shutil.copyfile(path, new_path)
        except Exception as e:
            print(e)

    # endregion

    # region log
    def log(self):
        try:
            if len(open(self.__wit_path + "\\details.csv").readlines()) == 1:
                print("fatal: your current branch 'master' does not have any repository yet")
            else:
                with open(self.__wit_path + "\\details.csv", 'r') as csvfile:
                    a = csv.DictReader(csvfile)
                    for row in a:
                        print("commit " + row["hash"] + "(HEAD -> master)")
                        print(f"Author: {self.__user_name} <{self.__user_email}>")
                        print("Date: " + row["date"])
                        print("\n       " + row["message"] + "\n")
        except Exception as e:
            print(e)

    # endregion

    # region status
    def status(self):
        try:
            print("On branch master\n")
            if len(open(self.__wit_path + "\\details.csv").readlines()) == 1:
                print("No repository yet")
            res = os.listdir(self.__path + "\\.wit\\staging_copy")
            if len(res) == 0:
                print("nothing to commit, working tree clean")
            else:
                print('Changes to be committed:')
                print('  (use "git commit -m <message>..." to commit)')
                for f in res:
                    print("      modified:   " + f)  # if I want to it like git: I have to check if its new file or not...
        except Exception as e:
            print(e)

    # endregion

    # region checkout
    def checkout(self, commit_id):
        try:
            with open(self.__wit_path + "\\details.csv", 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                with open(self.__path + "\\.wit\\new_details.csv", "a") as new_details:
                    writer = csv.DictWriter(new_details)
                    for row in reader:
                        if not row["hash"] == commit_id:
                            writer.writerow(row)
                        else:
                            temp_row = row
                    writer.writerow(temp_row)
            os.remove(self.__wit_path + "\\details.csv")
            os.rename(self.__wit_path + "\\new_details.csv", self.__wit_path + "\\details.csv")

            for r in os.listdir(self.__path):
                if r != '.wit':
                    if os.path.isfile(self.__path+"\\"+r):
                        os.remove(self.__path+"\\"+r)
                    else:
                        shutil.rmtree(self.__path + "\\r")
            shutil.copytree(self.__path + "\\.wit\\repository\\" + commit_id, self.__path)
        except Exception as e:
            print(e)

    # endregion

    # region commit
    def commit(self, message):
        try:
            path = self.__path + "\\.wit\\repository\\"
            current_hash = str(hash(message))
            dic = {"hash": current_hash, "date": DateTime(), "message": message}
            last_version_hash = ''
            with open(self.__wit_path + "\\details.csv", 'a', newline='') as csvfile:
                index = len(open(self.__wit_path + "\\details.csv").readlines()) - 1
                if index > 0:
                    try:
                        last_version_hash = list(csvfile)[index].split(',')[0]
                    except ValueError:
                        print("ERROR...")
                writer = csv.DictWriter(csvfile, dic.keys())
                writer.writerow(dic)
            csvfile.close()
            if last_version_hash == '':
                try:
                    dest = path + current_hash
                    print(dest)
                    shutil.copytree(self.__path, dest)
                except Exception as e:
                    print(f"Error copying directory: {e}")
                shutil.rmtree(path + current_hash + "\\.wit")
            else:
                shutil.copytree(path + last_version_hash, path + current_hash)
            for r in os.listdir(f"{self.__path}\\.wit\\staging_copy"):
                try:
                    shutil.move(f"{self.__path}\\.wit\\staging_copy\\{r}", path + current_hash)
                except Exception as e:
                    pass
        except Exception as e:
            print(e)
    # endregion
