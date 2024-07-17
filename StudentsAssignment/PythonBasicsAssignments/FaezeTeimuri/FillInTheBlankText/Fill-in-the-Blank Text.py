import random
import csv
csv_file_path = 'Noun.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    noun = []
    for row in csv_reader:
        noun.append(row)
csv_file_path = 'Adverb.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    adverb = []
    for row in csv_reader:
        adverb.append(row)
csv_file_path = 'Verb.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    verb = []
    for row in csv_reader:
        verb.append(row)
csv_file_path = 'Adjective.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    adjective = []
    for row in csv_reader:
        adjective.append(row)

noun.append(input("Enter a noun:"))
adverb.append(input("Enter an adverb:"))
verb.append(input("Enter a verb:"))
adjective.append(input("Enter an adjective:"))

n = random.choice(noun)
a = random.choice(adverb)
v = random.choice(verb)
ad = random.choice(adjective)

print(n)
print(a)
print(v)
print(ad)

#sentence = str(n) + str(a)
#' '.join([map(str,n), map(str,a), map(str,v), map(str,ad)])
#print(sentence)
