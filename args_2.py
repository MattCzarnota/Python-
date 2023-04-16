def get_the_most_popular_word(*args, ignore_case=True):
    words ={}

    for arg in args:
        arg = arg.lower() if ignore_case else arg
        words[arg]= words.get(arg,0)+1

    for word, occurences in words.items():
        if occurences == max(words.values()):
            return word
            #return occurences

print(get_the_most_popular_word('cat','cat','dog','bird','CAT', 'DOG'))




