# movies = {'Shawshang redemption':{'genre': 'drama', 'year': 1994} ,
#         'Harry Potter':{'genre': 'fantasy', 'year': 2001},
#         'Lord of the rings':{'genre': 'fantasy', 'year': 2001},
#         'God father':{'genre': 'drama', 'year': 1972}
#         }

movies = {}


def add_movies():
    add_movie = 1
    while add_movie:
        print("let's add a movie to our database!")
        movie_name = input('please enter your movie name: ').lower()
        movie_genre = input('what genre is it? ').lower()
        movie_year = int(input('what year was it produced? '))
        movies[movie_name] = {'genre': movie_genre, 'year': movie_year}
        print('movie added succesfully!')
        another_movie = input('Do you want to add another movie [yes/no] ?').lower()
        if another_movie == 'yes':
            add_movie = 1
        elif another_movie == 'no':
            add_movie = 0
            print('returning to main menue')
            break
        else:
            print('invalid option')
            print('returning to main menue')
            break


def display_all_movies():
    print('\nall movies:')
    if not movies:
        print('no movies are available in our archive')
    else:
        for key, value in movies.items():
            print(f'movie name: {key} , genre: {value['genre']} , year: {value['year']}')


def display_genre_movies():
    while True:
        print('here are genres to look for:')
        genres_set = set()
        if not movies:
            print('no movies/genre are available in our archive')
            break
        else:
            for values in movies.values():
                genres_set.add(values['genre'])
            for i in genres_set:
                print(i, end=' * ')
        inp_genre = input("\nplease enter a genre you're interested in: ").lower()
        if inp_genre in genres_set:
            for key, value in movies.items():
                if value['genre'] == inp_genre:
                    print(f'movie name: {key} , genre: {value['genre']} , year: {value['year']}')
            break
        else:
            print('not a valid genre. please select a genre from provided genres')


def menue_options():
    print('\n-----------------Menue-----------------')
    print('1 - View all movies')
    print('2 - View movies based on their genres')
    print('3 - Add new movie')
    print('4 - Exit')


print('\nHello and welcome to movie recomendation app:')
while True:
    menue_options()
    menue_input = input('\nPlease select a number: ')
    if menue_input == '1':
        display_all_movies()
    elif menue_input == '2':
        display_genre_movies()
    elif menue_input == '3':
        add_movies()
    elif menue_input == '4':
        print('good bye!')
        break
    else:
        print('Not a valid option!')
