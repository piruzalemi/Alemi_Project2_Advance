import os, csv, pymongo, json

#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
client.drop_database('presidents_poll')
db = client["presidents_poll"]
#collection = db["presidents"]

# read data from language text file and split the word and count values
#def read_word_count(filename):
#    word_list = []
#    with open("../2018/2018/" + filename, errors='ignore') as lang_txt:
#        content = csv.reader(lang_txt, delimiter=' ')
#        for row in content:
#            word_list.append({"word" : row[0], "count" : row[1]})
#
#    return word_list

# main function read each file from folder and insert into mongo db.
def main():
    for filename in os.listdir("data"):
        if filename.endswith(".json"):
            # call read_word_count function to get word_list values
            word_list = filename
            print(word_list)
           # language = filename.strip('.txt')
            db["presidents"].insert_many(word_list)

if __name__ == "__main__":
    main()