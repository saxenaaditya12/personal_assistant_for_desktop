import os
import pickle
import the_voice


class SearchEngine:
    def __init__(self):
        self.file_index = []
        self.results = []
        self.matches = 0
        self.records = 0

    def create_new_index(self):
        # create a new index and save to file
        root_paths = get_drives()
        for root_path in root_paths:
            root_path = root_path + "\\"
            for root, dirs, files in os.walk(root_path):
                if files:
                    self.file_index.append((root, dirs, files))
        # 'if files' filters out empty file lists

        # save to file
        with open("data_files/file_index.pkl", "wb") as f:
            pickle.dump(self.file_index, f)

    def load_existing_index(self):
        # load existing index
        try:
            with open("data_files/file_index.pkl", "rb") as f:
                self.file_index = pickle.load(f)
        except:
            self.create_new_index()

    def search(self, term, search_type="contains"):
        # search for terms based on search type

        # reset variables
        self.results.clear()
        self.matches = 0
        self.records = 0
        # perform search

        self.load_existing_index()

        for path, dirs, files in self.file_index:
            for file in files:
                self.records += 1
                if (search_type == 'contains' and term.lower() in file.lower() or
                        search_type == 'startswith' and file.lower().startswith(term.lower()) or
                        search_type == 'endswith' and file.lower().endswith(term.lower())):
                    result = path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
            for dir in dirs:
                self.records += 1
                if (search_type == 'contains' and term.lower() in dir.lower() or
                        search_type == 'startswith' and dir.lower().startswith(term.lower()) or
                        search_type == 'endswith' and dir.lower().endswith(term.lower())):
                    result = path.replace('\\', '/') + '/' + dir
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
        # save search results
        with open('data_files/search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')


s = SearchEngine()


def get_drives():
    response = os.popen("wmic logicaldisk get caption")
    drives = []
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if line == "Caption" or line == "":
            continue
        drives.append(line)
    return drives


def pre_process():
    global s
    s.create_new_index()


def search(term, search_type="contains"):
    the_voice.say_and_print("Searching...")
    s.search(term, search_type)
    for i in s.results:
        print(i)
    the_voice.say_and_print("Searched {:,d} records and found {:,d} matches".format(s.records, s.matches))
    print("Results saved in working directory as search_results.txt.")
    return s.results

# def main():
#     print("Starting...")
#     pre_process()
#     while True:
#         x = input(">>>")
#         if x.lower() == "exit":
#             break
#         search(x)
