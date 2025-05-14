import sqlite3

DATABASE = "jazz.db"

# Function to print all songs with their artist names
def print_all_songs():
    # Connect to the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    
    # Query to get song title and artist name from the database
    sql = "SELECT song.title, artist.name FROM song INNER JOIN artist ON song.artist_id = artist.artist_id"
    cursor.execute(sql)  # Execute the query
    results = cursor.fetchall()  # Fetch all the results (songs and their artists)
    
    # Print the header for the output
    print(f"{'Song Name':<40}{'Artist':<30}")
    print("-" * 70)  # This prints a line of dashes for separation
    
    # Print the song titles and artist names
    for song in results:
        print(f"{song[0]:<40}{song[1]:<30}")
    
    # Close the database connection
    db.close()

# Function to print songs by a specific artist
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
    # If songs are found, print them
    if results:
        print(f"{'Song Name':<40}{'Artist':<30}")
        print("-" * 70)  # Line of dashes for separation
        for song in results:
            print(f"{song[0]:<40}{song[1]:<30}")
    else:
        # If no songs are found for the artist
        print(f"No songs found for artist '{artist_name}'.")
    
    # Close the database connection
    db.close()

# Main menu loop
while True:
    print("\n--- Jazz Database ---")
    
    # Ask the user what they want to do
    user_input = input(
        "What would you like to browse?\n"
        "1. Browse through songs\n"
        "2. Browse through albums\n"
        "3. Browse through artists\n"
        "4. Exit\n"
    )
    
    if user_input == "1":
        # Ask if the user wants to see all songs or search by artist
        song_choice = input("Do you want to:\n1. See all songs\n2. Search by artist\n")
        
        if song_choice == "1":
            print_all_songs()  # Call the function to print all songs
        elif song_choice == "2":
            print_songs_by_artist()  # Call the function to print songs by a specific artist
        else:
            print("Invalid option. Returning to main menu.")
    
    elif user_input == "2":
        print("Displaying all albums (this part needs more code).")
    
    elif user_input == "3":
        print("Displaying all artists (this part needs more code).")
    
    elif user_input == "4":
        print("Goodbye!")  # Exit the program
        break
    
    else:
        print("That was not an option. Please try again.")
