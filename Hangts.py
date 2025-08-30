import random
import re
import sys

# Uses only the built-in Taylor Swift list
TS_SONGS = [
    "The 1",
    "1 Step Forward, 3 Steps Back",
    "22",
    "Actually Romantic",
    "Afterglow",
    "The Albatross",
    "The Alchemy",
    "The Alcott",
    "All of the Girls You Loved Before",
    "All Too Well",
    "All Too Well (10 Minute Version)",
    "All You Had to Do Was Stay",
    "American Girl",
    "Anti-Hero",
    "The Archer",
    "August",
    "Babe",
    "Baby (live cover of \"Baby, Don't You Break My Heart Slow\")",
    "Back to December",
    "Bad Blood",
    "Bad Blood (single version)",
    "Beautiful Eyes",
    "Beautiful Ghosts",
    "Begin Again",
    "Bein' With My Baby",
    "Bejeweled",
    "The Best Day",
    "Best Days of Your Life",
    "Bette Davis Eyes",
    "Better Man",
    "Better than Revenge",
    "Betty",
    "Bigger Than the Whole Sky",
    "Big Star (Live)",
    "Birch",
    "The Black Dog",
    "Blank Space",
    "The Bolter",
    "Both of Us",
    "Breathe",
    "Breathless",
    "But Daddy I Love Him",
    "Bye Bye Baby",
    "Call It What You Want",
    "Cancelled!",
    "Cardigan",
    "Carolina",
    "Cassandra",
    "Castles Crumbling",
    "Champagne Problems",
    "Change",
    "Chloe or Sam or Sophia or Marcus",
    "Christmas Must Be Something More",
    "Christmas Tree Farm",
    "Christmases When You Were Mine",
    "Clara Bow",
    "Clean",
    "Closure",
    "Cold as You",
    "Come Back... Be Here",
    "Come in with the Rain",
    "Coney Island",
    "Cornelia Street",
    "Cowboy like Me",
    "Crazier",
    "Cruel Summer",
    "Dancing with Our Hands Tied",
    "Daylight",
    "Dear John",
    "Dear Reader",
    "Death by a Thousand Cuts",
    "Deja Vu",
    "Delicate",
    "Don't Blame Me",
    "Don't You",
    "Dorothea",
    "Down Bad",
    "Dress",
    "Drops of Jupiter (Live)",
    "Eldest Daughter",
    "Electric Touch",
    "Elizabeth Taylor",
    "Enchanted",
    "End Game",
    "Epiphany",
    "Evermore",
    "Everything Has Changed",
    "Exile",
    "Eyes Open",
    "False God",
    "The Fate of Ophelia",
    "Father Figure",
    "Fearless",
    "Fifteen",
    "Florida!!!",
    "Foolish One",
    "Forever & Always",
    "Forever Winter",
    "Fortnight",
    "Fresh Out the Slammer",
    "Gasoline",
    "Getaway Car",
    "Girl at Home",
    "Glitch",
    "Gold Rush",
    "Gorgeous",
    "The Great War",
    "Guilty as Sin?",
    "Half of My Heart",
    "Happiness",
    "Haunted",
    "Hey Stephen",
    "High Infidelity",
    "Highway Don't Care",
    "Hits Different",
    "Hoax",
    "Hold On",
    "Holy Ground",
    "Honey",
    "How Did It End?",
    "How You Get the Girl",
    "I Almost Do",
    "I Bet You Think About Me",
    "I Can Do It with a Broken Heart",
    "I Can See You",
    "I Can Fix Him (No Really I Can)",
    "I Did Something Bad",
    "I Don't Wanna Live Forever",
    "I Forgot That You Existed",
    "I Hate It Here",
    "I Heart ?",
    "I Look in People's Windows",
    "I Knew You Were Trouble",
    "I Know Places",
    "I Think He Knows",
    "I Want You Back",
    "I Wish You Would",
    "If This Was a Movie",
    "Illicit Affairs",
    "I'm Only Me When I'm with You",
    "Im gonna get you back",
    "Innocent",
    "Invisible",
    "Invisible String",
    "Is It Over Now?",
    "It's Nice to Have a Friend",
    "It's Time to Go",
    "Ivy",
    "The Joker and the Queen (single version)",
    "Jump Then Fall",
    "Karma",
    "Karma (remixed version)",
    "King of My Heart",
    "Labyrinth",
    "The Lakes",
    "Last Christmas",
    "The Last Great American Dynasty",
    "Last Kiss",
    "The Last Time",
    "Lavender Haze",
    "The Life of a Showgirl",
    "Loml",
    "London Boy",
    "Long Live",
    "Long Live (Brazilian version)",
    "Long Story Short",
    "Look What You Made Me Do",
    "Love Story",
    "Lover",
    "Lover (Remix)",
    "The Lucky One",
    "Macavity",
    "Mad Woman",
    "The Man",
    "The Manuscript",
    "Marjorie",
    "Maroon",
    "Mary's Song (Oh My My My)",
    "Mastermind",
    "Me!",
    "Mean",
    "Message in a Bottle",
    "Midnight Rain",
    "Mine",
    "Mirrorball",
    "Miss Americana & the Heartbreak Prince",
    "The Moment I Knew",
    "Mr. Perfectly Fine",
    "My Boy Only Breaks His Favorite Toys",
    "My Tears Ricochet",
    "Never Grow Up",
    "New Romantics",
    "New Year's Day",
    "No Body, No Crime",
    "Nothing New",
    "Now That We Don't Talk",
    "Only the Young",
    "Opalite",
    "The Other Side of the Door",
    "Our Song",
    "Ours",
    "Out of the Woods",
    "The Outside",
    "Paper Rings",
    "Paris",
    "Peace",
    "A Perfectly Good Heart",
    "Peter",
    "Picture to Burn",
    "A Place in This World",
    "The Prophecy",
    "Question...?",
    "...Ready for It?",
    "Red",
    "Renegade",
    "Right Where You Left Me",
    "Robin",
    "Ronan",
    "Ruin the Friendship",
    "Run",
    "Sad Beautiful Tragic",
    "Safe & Sound",
    "Santa Baby",
    "Say Don't Go",
    "September",
    "Seven",
    "Shake It Off",
    "Should've Said No",
    "Silent Night",
    "'Slut!'",
    "The Smallest Man Who Ever Lived",
    "Snow on the Beach",
    "So High School",
    "So It Goes...",
    "So Long, London",
    "Soon You'll Get Better",
    "Sparks Fly",
    "Speak Now",
    "Starlight",
    "State of Grace",
    "Stay Beautiful",
    "Stay Stay Stay",
    "The Story of Us",
    "Style",
    "Suburban Legends",
    "Superman",
    "Superstar",
    "Sweet Nothing",
    "Sweeter than Fiction",
    "Teardrops on My Guitar",
    "Tell Me Why",
    "Thank You Aimee",
    "That's When",
    "This Is Me Trying",
    "This Is What You Came For",
    "This Is Why We Can't Have Nice Things",
    "This Love",
    "Tied Together with a Smile",
    "Tim McGraw",
    "Timeless",
    "'Tis the Damn Season",
    "Today Was a Fairytale",
    "Tolerate It",
    "The Tortured Poets Department",
    "Treacherous",
    "Two Is Better Than One",
    "Umbrella",
    "Untouchable",
    "Us",
    "The Very First Night",
    "Vigilante Shit",
    "The Way I Loved You",
    "We Are Never Ever Getting Back Together",
    "Welcome to New York",
    "We Were Happy",
    "When Emma Falls in Love",
    "White Christmas",
    "White Horse",
    "Who's Afraid of Little Old Me?",
    "Wildest Dreams",
    "Willow",
    "Wish List",
    "Wonderland",
    "Wood",
    "Would've, Could've, Should've",
    "You All Over Me",
    "You Are in Love",
    "You Belong with Me",
    "You'll Always Find Your Way Back Home",
    "You Need to Calm Down",
    "You're Losing Me",
    "You're Not Sorry",
    "You're on Your Own, Kid",
    # Second block
    "A Little More like You",
    "Acting like a Boy",
    "All Night Diner",
    "Am I Ready for Love",
    "American Boy",
    "Angelina",
    "Baby Blue",
    "Beautiful Days",
    "Better Off",
    "Bother Me",
    "Brand New World",
    "Brought Up That Way",
    "By the Way",
    "Can I Go with You",
    "Check Out This View",
    "Closest to a Cowboy",
    "Cross My Heart",
    "Dark Blue Tennessee",
    "Diary of Me",
    "Don't Hate Me for Loving You",
    "Drama Queen",
    "Fall Back on You",
    "Family",
    "Fire",
    "For You",
    "Gail's Song",
    "Go Slow",
    "Gracie",
    "Half-Way to Texas",
    "Heaven",
    "Her",
    "His Lies",
    "Honey Baby",
    "Houston Rodeo",
    "I Don't Want to Lose Your Face",
    "I Used to Fly",
    "I'd Lie",
    "In the Pouring Rain",
    "Just South of Knowing Why",
    "Kid in the Crowd",
    "Let's Go",
    "Live for the Little Things",
    "Long Time Going",
    "Look at You like That",
    "Love They Haven't Thought of Yet",
    "Love to Lose",
    "Lucky You",
    "Made Up You",
    "Mandolin",
    "Mary Jo",
    "Matches",
    "Me & Britney",
    "Missing You",
    "My Turn to Be Me",
    "Need",
    "Need You Now",
    "Never Fade",
    "Never Mind",
    "None of the Above",
    "Not One Day",
    "One More Day",
    "One-Sided Goodbye",
    "Perfect Have I Loved",
    "Permanent Marker",
    "Point of View",
    "Pretty Words",
    "Rain Song",
    "Revenge",
    "Ride On",
    "Same Girl",
    "Scream",
    "Shaking Thrift Shop",
    "Smokey Black Nights",
    "Someone Just Told Me",
    "Someone Loves You",
    "Spinning Around",
    "Stupid Boy",
    "Sugar",
    "Sweet Tea and God's Graces",
    "Tell Me",
    "Tennessee",
    "That's Life",
    "Thinking 'Bout You",
    "Thirteen Blocks",
    "This Here Guitar",
    "This Is Really Happening",
    "This One's Different",
    "Today",
    "Too Beautiful",
    "Under My Head",
    "Wait for Me",
    "Welcome Distraction",
    "What Do You Say?",
    "What to Wear",
    "Who I've Always Been",
    "Wonderful Things",
    "You",
    "You Do",
    "You Don't Have to Call",
    "You Walk Away",
    "Your Picture"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def normalize_title(title):
    display, answer = [], []
    for ch in title:
        if ch.isalpha() or ch.isdigit():
            display.append("_")
            answer.append(ch.upper())
        else:
            display.append(ch)
            answer.append(None)
    return display, answer

def show_state(display, wrong_guesses, guessed_letters):
    print(HANGMAN_PICS[min(len(wrong_guesses), len(HANGMAN_PICS)-1)])
    print()
    print("Song:", " ".join(display))
    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    if wrong_guesses:
        print("Wrong guesses:", " ".join(wrong_guesses))
    print()

def apply_letter_guess(letter, display, answer):
    hit = False
    for i, target in enumerate(answer):
        if target == letter:
            display[i] = letter
            answer[i] = None
            hit = True
    return hit

def check_win(answer):
    return all(a is None for a in answer)

def clean_guess(s):
    t = s.strip().replace("’", "'")
    t = re.sub(r'^\s*["\']|["\']\s*$', "", t)  # strip wrapping quotes
    t = re.sub(r"\s+", " ", t)                 # collapse spaces
    return t.upper()

def main():
    print("Taylor Swift Hangman")
    print("Guess letters or try the full song title.")
    print("Spaces and punctuation are shown.")
    print()

    titles = TS_SONGS  # fixed pool only

    while True:
        secret_title = random.choice(titles)
        display, answer = normalize_title(secret_title)

        lives = len(HANGMAN_PICS) - 1
        wrong_guesses = []
        guessed_letters = set()

        while True:
            show_state(display, wrong_guesses, guessed_letters)
            guess = input("Your guess (letter or full title): ").strip()

            if not guess:
                print("Please enter something.")
                continue

            if len(guess) > 1:
                if clean_guess(guess) == clean_guess(secret_title):
                    for i in range(len(display)):
                        if answer[i] is not None:
                            display[i] = answer[i]
                    print("\nCorrect. The song is:", secret_title)
                    break
                else:
                    wrong_guesses.append(guess)
                    print("Not quite.")
            else:
                letter = guess.upper()
                if not re.fullmatch(r"[A-Z0-9]", letter):
                    print("Guess letters A-Z or digits 0-9.")
                    continue
                if letter in guessed_letters:
                    print("You already tried that letter.")
                    continue
                guessed_letters.add(letter)

                if apply_letter_guess(letter, display, answer):
                    print("Nice.")
                    if check_win(answer):
                        print("\nYou got it:", secret_title)
                        break
                else:
                    wrong_guesses.append(letter)
                    print("Nope.")

            if len(wrong_guesses) >= lives:
                print(HANGMAN_PICS[-1])
                print("\nOut of lives.")
                print("The song was:", secret_title)
                break

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing.")
            return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
