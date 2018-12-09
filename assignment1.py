"""
Name : Syed Mukhtar Patan
Student ID : 13571891
Brief program details : Reading and listing a list of songs in a file to keep track whether they have been learned or
haven't been learned.
Github :https://github.com/syed123456789/Assignment1/blob/master/assignment1.py
"""

'This program can display a list of songs that are either learned or unlearned, '
'and allow user to add new songs to the list'

'Pseudocode for algorithms'
# This program will load songs from a csv file
# A menu is displayed so that user can make choices: all song being listed, downloading a song or learning a song

song_names = []
song_artists = []
song_years = []
song_learneds = []




'Sub main()'

def main():
    # print welcome message
    print("Songs To Learn 1.0 - by <Syed Mukhtar Patan>")
    # call loading_songs()
    loading_songs()
    main_menu()



'Function: main_menu()'

def main_menu():
    # Loop while the conditions given below are true
    while True:
        print("main_menu:")
        print("L - List songs")
        print("A - Add new song")
        print("C - Complete a song")
        print("Q - Quit")
        # Input users's choice
        choice = input(">>> ").upper()
        # after choice song listed = L
        if choice == "L":
            song_list()
        # User can input a song by their choice
        elif choice == "A":
            download_new_songs()
        elif choice == "C":
            complete_songs()
        # User can save all of their changes and quit the program
        elif choice == "Q":
            save_songs()
            print("Have a nice day :)")
        else:
            print("Invalid input; enter a valid number")


'Function: loading_songs()'

def loading_songs():
    # Open the csv file and attach it to a variable (in_file)
    in_file = open("songs.csv", 'r')
    # Loop from beginning to end of file
    for line in in_file:
        # Split up read line by ','
        song_item = line.split(',')
        # song name save to a list (song_names)
        song_names.append(song_item[0])
        # song artists save  to a list (song_artists)
        song_artists.append(song_item[1])
        # song years save to a list (song_years)
        song_years.append(int(song_item[2]))
        # Take away "\n" from the 4th item in the list
        song_item[3] = song_item[3].strip('\n')

        # Convert songs learned from "y" to " ", "n" to "*"
        if song_item[3] == "y":
            song_item[3] = " "
        if song_item[3] == "n":
            song_item[3] = "*"

        song_learneds.append(song_item[3])

    in_file.close()

    # Print the number of songs that is loaded.
    print("{} song is loaded".format(len(song_names)))





'Function: download_new_song()'

def download_new_songs():
    # Loop while the conditions given below are true
    while True:
        new_song = input("Title: ")
        if new_song == "":
            print("Input cannot be blank")
        else:
            break
    while True:
        new_artist = input("Artist: ")
        if new_artist == "":
            print("Input cannot be blank")
        else:
            break
    while True:
        try:
            new_year = int(input("Year: "))
            if new_year < 0:
                print("Number must be >= 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {} ({}) added to song list".format(new_song, new_artist, new_year))


'Function: song_list()'

def songs_list():
    # Print all downloaded songs
    for i in range(0, len(song_names)):
        print(" {0}. {1} {2:30} - {3:30} ({4})".format(i, song_learneds[i], song_names[i], song_artists[i],
                                                       song_years[i]))
    # Print the number of songs learned, and to learn.
    print("{} songs learned, {} songs still to learn".format(song_learneds.count(" "), song_learneds.count("*")))



'Function: save_songs()'


def save_songs(songs_list):
    # open the csv file songs.csv and edit the contents inside
    out_file = open("songs.csv", 'w')
    # Loop till the end of list
    for i in range(0, len(song_names)):
        save_song_learneds = song_learneds[i]
        if save_song_learneds == " ":
            save_song_learneds = "y"
        if save_song_learneds == "*":
            save_song_learneds = "n"
        print(",", end=" ", file= out_file)

    out_file.close()



'Function: complete_songs()'

def complete_songs():
    # input the song the user want to learn
    any_song = int(input("Enter the number of song marked as learned "))
    try:
        # Loop as long as the song number is in the range of song numbers in the csv file
        if 0 <= any_song < len(song_names):
            if song_learneds[any_song] != " ":
                song_learneds[any_song] = " "
                print("{} by {} learned".format(song_names[any_song], song_artists[any_song]))
            else:
                print("You have already learned {} ".format(song_names[any_song], song_artists[any_song]))
        else:
            print("Invalid input; enter a valid number")
    except ValueError:
        # Caution when there are systematic errors
        print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
