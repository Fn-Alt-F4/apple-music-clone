

#login

accounts = {}

login_question = input("Login or Create?")
while True:
    if login_question == "Login":
        login_username = input("Whats your username?")
        login_password = input("Whats your password?")
        if login_username in accounts and accounts[login_username] == login_password:
            print("Correct login, you may precde.")
        elif login_question == "Create":
            create_username = input("What is the username you would like to create?")
            create_password = input("Whats the password for the account your creating?")
            accounts[create_username] = create_password
        elif login_question == "Quit":
            break

###

###

###

#Now create your interface for apple music clone

interface = ["songs" , "search" , "settings" , "playlists"]

print(interface)

search = [
    "Bohemian Rhapsody", "Stairway to Heaven", "Master of Puppets", "Ace of Spades",
    "Sweet Child O' Mine", "Back in Black", "Smells Like Teen Spirit", "Paint It Black",
    "Hotel California", "Comfortably Numb", "Enter Sandman", "Paranoid",
    "Lose Yourself", "Sicko Mode", "HUMBLE.", "Juicy", "N.Y. State of Mind", "Alright",
    "Billie Jean", "Rolling in the Deep", "Uptown Funk", "Bad Guy", "Blinding Lights", "Levitating",
    "Johnny B. Goode", "Purple Haze", "Born to Run", "Free Bird", "Highway to Hell",
    "Wonderwall", "Creep", "Mr. Brightside", "Seven Nation Army", "Take Me Out",
    "One Dance", "God's Plan", "SICKO", "Money Trees", "Nuthin' but a G Thang",
    "Thriller", "Like a Prayer", "Toxic", "Since U Been Gone", "Shake It Off",
    "Ring of Fire", "Jolene", "Take Me Home Country Roads", "Chicken Fried",
    "Superstition", "September", "Respect", "What's Going On",
    "No Diggity", "Hey Ya!", "Crazy in Love", "Umbrella"
]

settings = ["audio" "quit" "apple car play"]

#Now for play lists they are gonna be seperated by genre
#rap
#pop
#Metal
#rock

playlists = ("rap" , "metal" , "rock" , "pop")

rap_playlist = [
    "Sicko Mode", "HUMBLE.", "God's Plan", "Money Trees", "Alright", "DNA.",
    "Nuthin' but a G Thang", "Juicy", "N.Y. State of Mind", "Lose Yourself",
    "Stan", "The Real Slim Shady", "In Da Club", "Hate It or Love It",
    "Gold Digger", "Stronger", "Jesus Walks", "POWER", "Runaway",
    "One Dance", "Started From the Bottom", "Nonstop", "Hotline Bling",
    "Panda", "Bad and Boujee", "Mask Off", "XO Tour Llif3", "Congratulations",
    "SICKO", "Goosebumps", "Antidote", "The Box", "Rockstar", "Sad!",
    "Old Town Road", "Bodak Yellow", "Truth Hurts", "Nice for What",
    "m.A.A.d city", "Swimming Pools", "King's Dead", "Family Ties",
    "C.R.E.A.M.", "Shook Ones Pt. II", "Dear Mama", "California Love",
    "It Was a Good Day", "Nuthin", "Still D.R.E.", "Forgot About Dre",
    "Empire State of Mind", "99 Problems", "Hard Knock Life", "Big Poppa"
]

pop_playlist = [
    "Billie Jean", "Thriller", "Beat It", "Like a Prayer", "Vogue",
    "...Baby One More Time", "Toxic", "Since U Been Gone", "Since U Been Gone",
    "Rolling in the Deep", "Someone Like You", "Hello", "Bad Romance",
    "Poker Face", "Just Dance", "Shake It Off", "Blank Space", "Anti-Hero",
    "Uptown Funk", "Blinding Lights", "Can't Feel My Face", "Starboy",
    "Bad Guy", "Happier Than Ever", "Levitating", "Don't Start Now",
    "Shape of You", "Perfect", "Watermelon Sugar", "As It Was",
    "Call Me Maybe", "Party in the U.S.A.", "Firework", "Roar",
    "Umbrella", "Crazy in Love", "Single Ladies", "Halo",
    "Royals", "Green Light", "drivers license", "good 4 u",
    "Sugar", "Girls Like You", "Moves Like Jagger", "Dynamite",
    "Teenage Dream", "We Found Love", "Rehab", "Valerie", "Cruel Summer"
]

metal_playlist = [
    "Master of Puppets", "Enter Sandman", "One", "Fade to Black", "Battery",
    "Paranoid", "Iron Man", "War Pigs", "Children of the Grave",
    "Ace of Spades", "Painkiller", "Breaking the Law", "Electric Eye",
    "Run to the Hills", "The Trooper", "Fear of the Dark", "Hallowed Be Thy Name",
    "Raining Blood", "Angel of Death", "South of Heaven",
    "Holy Wars", "Symphony of Destruction", "Peace Sells",
    "Chop Suey!", "Toxicity", "B.Y.O.B.", "Aerials",
    "Freak on a Leash", "Blind", "Falling Away from Me",
    "Bodies", "Duality", "Before I Forget", "Psychosocial",
    "Walk", "Cowboys from Hell", "Cemetery Gates",
    "Ace of Spades", "The Number of the Beast", "2 Minutes to Midnight",
    "Sad but True", "For Whom the Bell Tolls", "Seek & Destroy",
    "Crawling", "One Step Closer", "Numb", "In the End",
    "Hail to the King", "Bat Country", "Nightmare",
    "Ticks & Leeches", "Sober", "Schism", "Vicarious"
]

rock_playlist = [
    "Stairway to Heaven", "Kashmir", "Whole Lotta Love", "Black Dog",
    "Back in Black", "Highway to Hell", "Thunderstruck", "You Shook Me All Night Long",
    "Sweet Child O' Mine", "Welcome to the Jungle", "November Rain", "Paradise City",
    "Hotel California", "Life in the Fast Lane", "Take It Easy",
    "Comfortably Numb", "Wish You Were Here", "Another Brick in the Wall", "Money",
    "Born to Run", "Thunder Road", "Dancing in the Dark",
    "Free Bird", "Sweet Home Alabama", "Simple Man",
    "Bohemian Rhapsody", "Don't Stop Me Now", "We Will Rock You", "Under Pressure",
    "Purple Haze", "All Along the Watchtower", "Voodoo Child",
    "Johnny B. Goode", "Satisfaction", "Paint It Black", "Gimme Shelter",
    "Born to Be Wild", "Fortunate Son", "Bad Moon Rising",
    "Smells Like Teen Spirit", "Come As You Are", "Heart-Shaped Box",
    "Wonderwall", "Don't Look Back in Anger", "Champagne Supernova",
    "Mr. Brightside", "Seven Nation Army", "Creep", "Karma Police",
    "Livin' on a Prayer", "Dream On", "Walk This Way", "More Than a Feeling"
]

if interface == "playlist":
    playlist_question = input("What playlist?")
    if playlist_question == "metal":
        print(metal_playlist)
    elif playlist_question == "rock":
        print(rock_playlist)
    elif playlist_question == "pop":
        print(pop_playlist)
    elif playlist_question == "rap":
        print(rap_playlist)
    else:
        print("not a avaliable playlist.")
elif interface == "settings":
    print(settings)
elif interface == "search":
    print(search)

#now my next goal is to have the user have the ability to add songs to their own playlist. they can add the songs in the search setting.

user_created_playlist = []

print(search)

user_selected_songs = input("What song would you like to add to your playlist from the search?")
if user_selected_songs in search:
    user_created_playlist.append(user_selected_songs)
    print(user_created_playlist)
else:
    print("Song is not in the search.")

    