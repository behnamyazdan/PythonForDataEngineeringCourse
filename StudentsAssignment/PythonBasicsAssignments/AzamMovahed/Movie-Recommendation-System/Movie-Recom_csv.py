import csv

movie_list = open('my_movie.csv', 'w')
movie_list = csv.writer(movie_list)
movie_list.writerow(['Title', 'Genra', 'Year'])

n = int(input("enter the number of movie you want add to your list: "))
for i in range(n):
    name, genra, year = input(f'{i}. Enter name, genra and year of movies separated by dash: ').split(sep="-")
    movie_list.writerow([name, genra, year])

with open('my_movie.csv') as file:
    for k in csv.DictReader(file):
        print(dict(k))

# Mentor Comments:
'''


'''
