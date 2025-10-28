import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in data:
    print(i["title"]) """
""" user_input = int(input("What is the oldest year that you would watch a movie from?"))
user_input2 = int(input("What is the most recent year that you would watch a movie from?"))
for movie in data:
    if movie["year"] >= user_input and movie["year"] <= user_input2: 
        print(movie["title"]) """
""" user_input = int(input("What year do you want to watch a move from?"))
for movie in data:
    if movie["year"] == user_input:
        print(movie["title"])   """
#exact search
""" user_input = input("What movie do you want to watch?")
for movie in data:
   if user_input == movie["title"]:
      print(movie["title"]) """
#results with search
""" x = input("What movie?")
y = x.lower()
for i in data: 
    if y in i["title"].lower():
        print (i["title"]) """
x = input("what genre?")
for movie in data:
    if x in movie["genres"]:
        print(movie["title"])





""" user_input = input("What genre would you like to watch?")
for movie in data:
    if user_input == movie["genres"]:
        print(movie["title"]) """