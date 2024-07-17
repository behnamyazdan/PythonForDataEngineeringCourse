def string_split_strip(string_inp):
    ''' split string to list by comma '''
    splited_list = string_inp.split(',')
    #remove extra spaces
    for index in range(len(splited_list)):
        splited_list[index] = splited_list[index].strip()
    return splited_list

print('Hello and welcome to fill in the blank game! ')
print('Here is how it works.\nprovide the information needed to fill the blanks of a random text')
while True:
    option = input('press 1 to play the game or 0 to exit: ')
    if option == '1':
        adjectives = input('please enter 2 adjectives sepreted by comma (","): ')
        nouns = input('pls enter 3 nouns sepreted by comma (","): ')
        places = input('pls enter a place: ')
        body_part = input('pls enter a body part: ')

        adjectives_list = string_split_strip(adjectives)
        #print(adjectives_list)
        nouns_list = string_split_strip(nouns)
        #print(nouns_list)
        places_list = string_split_strip(places)
        #print(places_list)
        body_part_list = string_split_strip(body_part)
        #print(body_part_list)
        print(f""" Yesterday, I woke up feeling very {adjectives_list[0]}.  
        I decided to make myself a delicious breakfast of {nouns_list[0]} and {nouns_list[1]}.  
        While I was eating, a {nouns_list[2]} flew right by my window!  
        I chased it outside as fast as my {body_part_list[0]} could go,  
        but it disappeared into the {places_list[0]}.  
        The rest of the day was pretty uneventful, but it was definitely an {adjectives_list[1]} morning!
        """)
    elif option == '0':
        print('good bye!')
        break
    else:
        print('invalid option')



