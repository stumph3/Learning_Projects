#Need to be able to add new moview to my collection

#Would like to be able to list all the movies in the collection

#Find a movie by using the movie title

##IMPLIMENTATION

#---------------------------------------
#Decide where to store movies in code
#Use a list = movie[]
movies = []

#Decide what data we want to store for each movie 
#Create a dictionary variable for each movie, In the dictonary we are going to store a movie title, director, and release year.
#Create a variable for each of the things we will store and ask the user for the input, then movies.append({"'title:" title,}) for each thing.
#Create a function that runs when the users selects the add movie choice in the user menu, that adds what they type to the movies dictonary.
def addMovie():
        title = input("Enter the title of the movie: ")
        director = input("Who was the director of this movie?: ")
        release_year = input("what year was this movie realease?: ")

        movies.append({
        'title': title,
        'director': director,
        'release_year': release_year
    })



#create a function that lists all of the movies in the dictionary

def listMovies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['release_year']}")

def findMovie():
    movieToFind = input("What movie are you searching for?")
    for movie in movies:
        if movie["title"] == movieToFind:
            print_movie(movie)

#impliment each requirement in turn, each as a seperate function.
#stop running the program when the user inputs Q
#---------------------------------------



#Show the user a menu and let them pick and option
#Get the users input, then run a loop and get their input again at the end.
#Create a menu prompt, then store the input in selection (selection = input(prompt))
#Create a while loop with three options a, l, f, or q to quit


MENU_PROMPT = "Please enter what you would like to do: \n 'a' to add a movie to your collection: \n 'l' to list all the movies in your current collection:  \n 'f' to find \
movies by title: \n 'q' to quit:"
selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        addMovie()
    elif selection == 'l':
        listMovies()
    elif selection == 'f':
        findMovie()
    else:
        print("Unknown command. please try again.")
    selection = input(MENU_PROMPT)
        
        
print('You have chosen to quit the program, Goodbye!')

