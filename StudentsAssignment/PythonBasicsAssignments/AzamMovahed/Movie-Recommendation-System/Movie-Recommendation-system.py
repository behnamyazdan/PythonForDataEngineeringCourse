
print('welcome to sahar-mvd movies recommended.')
print('we have alot of movies which categorised in these genra: \n1-animation \n2-comedy \n3-drama \n4-thriller ')

movies = {
"movie1":{"title": "Leviathan", "year": 2014, "genra": "drama"},
"movie2":{"title": "Animated Soviet Propaganda-Fascist Barbarians", "year": 2006, "genra": "animation"},
"movie3":{"title": "Miracle", "year": 2004, "genra": "drama"},
"movie4":{"title": "The Final Weekend", "year": 2005, "genra": "thriller"},
"movie5":{"title": "Attention Turtle!", "year": 1970, "genra": "comedy"},
"movie6":{"title": "Balkan Express", "year": 1983, "genra": "comedy"}
}

user_genra_selection = str(input('enter your favorite genra : ')).lower()

filtered_dict = {k: v for k, v in movies.items() if v.get('genra') == user_genra_selection}

for k, v in filtered_dict.items():
    print(v.get('title'), v.get('year'))



