from string import Template
ListOfMovies = []
Movies = Template('Title: $title, Genre: $genre, Year: $year')

while True:
    Choice = input("Do you want to store a movie?(Y/N)")
    if Choice == "Y":
        title = input("Movie's Title:")
        genre = input("Movie's Genre:")
        year = input("Movie's Year:")
        Movie = Movies.substitute(title=title,genre=genre, year=year)
        ListOfMovies.append(Movie)
        print(ListOfMovies)
    elif Choice == "N":
        Choice = input("Do You Want to seeing a list of movies?(Y/N)")
        if Choice == "Y":
            print(ListOfMovies)
        elif Choice == "N":
            FavoriteGenre = input("What is your favorite genre?(Drama/Action/Comic/Horror)")
            Choice = input("Do you Wants to get our recommendation?(Y/N)")
            if Choice == "N":
                exit()
            elif Choice == "Y":
                pass



