import sqlite3

DATABASE = "jazz.db"

def print_all_song():
    '''Print all jazz songs nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM song"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Song Name':<40}{'Album ID':<10}{'Duration':<10}{'Composer':<20}{'Artist ID':<10}")
    for jazz in results:
        print(f"{jazz[1]:<40}{jazz[2]:<10}{jazz[3]:<10}{jazz[4]:<20}{jazz[5]:<10}")
    db.close()

def print_all_album():
    '''Print all jazz albums nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM album"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Title':<60}{'Year Released':<15}{'Sub-Genre':<20}")
    for album in results:
        print(f"{album[1]:<60}{album[2]:<15}{album[3]:<20}")
    db.close()

def print_all_artists():
    '''Print all jazz artists nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM artists"  
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Name':<40}{'Birth Year':<15}{'Death Year':<15}{'Primary Instrument':<20}")
    for artist in results:
        print(f"{artist[1]:<40}{artist[2]:<15}{artist[3]:<15}{artist[4]:<20}")
    db.close()

#main code
print("\n--- Jazz Database ---")
while True:
    user_input = input("What would you like. \n1. Browse through songs \n2. Browse through albums \n3. Browse through artists \n4. Exit\n")
    if user_input == "1":
        print_all_song()
        break
    elif user_input == "2":
        print_all_album()
        break
    elif user_input == "3":
        print_all_artists()
        break
    elif user_input == "4":
        break
    else:
        print('That was not an option!\n')

