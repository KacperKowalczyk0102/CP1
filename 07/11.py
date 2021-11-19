file = open("film_titles","w")

file.write("Star wars","Fast and Furius","Deadpool","joker","Spider-man")
for file in films_titles:
    file.write(title + '\n')
file.close()