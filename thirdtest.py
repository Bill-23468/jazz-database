import sqlite3

DATABASE = "jazz.db"

#functions
#print all the songs
def print_all_songs():
    '''Prints all jazz songs nicely.'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM song"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Song Name':<40}{'Album ID':<10}{'Duration':<10}{'Composer':<20}{'Artist ID':<10}")
    for jazz in results:
        print(f"{jazz[1]:<40}{jazz[2]:<10}{jazz[3]:<10}{jazz[4]:<20}{jazz[5]:<10}")
    db.close()

#print all the albums
def print_all_albums():
    '''Prints all jazz albums nicely.'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM album"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Title':<40}{'Year Released':<15}{'Sub-Genre':<20}")
    for album in results:
        print(f"{album[1]:<40}{album[2]:<15}{album[3]:<20}")
    db.close()

#print all the artist
def print_all_artists():
    '''Prints all jazz artists nicely.'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM artist"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Name':<40}{'Birth Year':<15}{'Death Year':<15}{'Primary Instrument':<20}")
    for artist in results:
        print(f"{artist[1]:<40}{artist[2]:<15}{artist[3]:<15}{artist[4]:<20}")
    db.close()

#print songs by requested artist
def print_songs_by_artist():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Ask the user for the artist's name
    artist_name = input('Enter the artist\'s name (or type "Exit" to quit):\n').strip().upper()
    if artist_name == "EXIT":
        return
    sql = "SELECT song.title, artist.name FROM song INNER JOIN artist ON song.artist_id = artist.artist_id WHERE UPPER(artist.name) = ?"
    cursor.execute(sql, (artist_name,))  
    results = cursor.fetchall() 
    if results:
        print(f"\nSongs by {artist_name}:")
        print(f"{'Song Name':<40}{'Artist':<30}")
        print("-" * 70)
        for song, artist in results:
            print(f"{song:<40}{artist:<30}")
    else:
        print(f"No songs found for the artist '{artist_name}'")
    
# Main menu loop
while True:
    user_input = input("What would you like to browse \n1. Browse through songs \n2. Browse through albums \n3. Browse through artists \n4. Exit\n")
    if user_input == "1":
        #sub menu
        output = input('Do you want to: \n1. See all songs \n2. Search song by artist\n')
        if output == '1':
            print_all_songs()
        elif output == '2':
            print_songs_by_artist()
        break
    elif user_input == "2":
        print_all_albums()
        break
    elif user_input == "3":
        print_all_artists()
        break
    elif user_input == "4":
        print("Goodbye!")
        break
    else:
        print('That was not an option. BITCH ASS NIGGAAAAAAAA')