import os, csv, pymongo

#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client.drop_database('presidents_poll')
db = client["presidents_poll3"]
collection = db["presidents"]

# read data from language text file and split the word and count values

def read_word_count(filename):
    word_list = []
    with open(filename, errors='ignore') as lang_txt:
        content = csv.reader(data_candidates_coordinates.csv)
        for row in content:
            word_list.append({"latitude" : row[1], "count" : row[1]})

    return word_list

# main function read each file from folder and insert into mongo db.
def main():
    for filename in os.listdir("data"):
        print(type(filename))
        if filename.endswith(".json"):
            # call read_word_count function to get word_list values
            word_list = filename
            print(word_list)
           # language = filename.strip('.txt')
           db["presidents"].insert_many(word_list)

if __name__ == "__main__":
    main()



    Dictionary ={"latitiude": Latitude,
                  "Longitude": Longitude  }


 ##  After you read csv
 ##           For