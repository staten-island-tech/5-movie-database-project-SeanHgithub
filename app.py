import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in data:
    print(i["title"]) """
user_input = int(input("What is the oldest year that you would watch a movie from?"))
user_input2 = int(input("What is the most recent year that you would watch a movie from?"))
for movie in data:
    if movie["year"] >= user_input and movie["year"] <= user_input2: 
        print(movie["title"])