# Movie and book database based on mood
recommendations = {
    "happy": {
        "movies": {
            "The Intouchables": 8.5,
            "Forrest Gump": 8.8,
            "Paddington 2": 7.8,
            "The Grand Budapest Hotel": 8.1,
            "Up": 8.3,
            "Singin' in the Rain": 8.3,
            "Little Miss Sunshine": 7.8,
            "Zootopia": 8.0,
            "The Lego Movie": 7.7,
            "Coco": 8.4
        },
        "books": {
            "The Alchemist - Paulo Coelho": 4.1,
            "Eleanor Oliphant is Completely Fine - Gail Honeyman": 4.3,
            "Wonder - R.J. Palacio": 4.4,
            "A Man Called Ove - Fredrik Backman": 4.5,
            "The Rosie Project - Graeme Simsion": 4.0,
            "The Hundred-Year-Old Man... - Jonas Jonasson": 4.1,
            "The House in the Cerulean Sea - TJ Klune": 4.5,
            "Matilda - Roald Dahl": 4.3,
            "Good Omens - Gaiman & Pratchett": 4.2,
            "Anne of Green Gables - L.M. Montgomery": 4.3
        }
    },
    "sad": {
        "movies": {
            "The Pursuit of Happyness": 8.0,
            "Inside Out": 8.1,
            "Marley & Me": 7.1,
            "Manchester by the Sea": 7.8,
            "Her": 8.0,
            "Bridge to Terabithia": 7.2,
            "My Girl": 7.0,
            "The Fault in Our Stars": 7.7,
            "A Beautiful Mind": 8.2,
            "Life of Pi": 7.9
        },
        "books": {
            "The Book Thief - Markus Zusak": 4.4,
            "A Little Life - Hanya Yanagihara": 4.3,
            "The Kite Runner - Khaled Hosseini": 4.6,
            "Me Before You - Jojo Moyes": 4.3,
            "Of Mice and Men - John Steinbeck": 4.2,
            "All the Bright Places - Jennifer Niven": 4.1,
            "Before I Die - Jenny Downham": 4.0,
            "Thirteen Reasons Why - Jay Asher": 3.9,
            "The Lovely Bones - Alice Sebold": 4.0,
            "Extremely Loud & Incredibly Close - Jonathan Safran Foer": 4.0
        }
    },
    "motivated": {
        "movies": {
            "Rocky": 8.1,
            "The Social Network": 7.7,
            "The Shawshank Redemption": 9.3,
            "Whiplash": 8.5,
            "Rudy": 7.5,
            "Hidden Figures": 7.8,
            "October Sky": 7.8,
            "The Blind Side": 7.6,
            "Coach Carter": 7.3,
            "Moneyball": 7.6
        },
        "books": {
            "Can’t Hurt Me - David Goggins": 4.7,
            "Atomic Habits - James Clear": 4.8,
            "Grit - Angela Duckworth": 4.4,
            "Deep Work - Cal Newport": 4.3,
            "Start With Why - Simon Sinek": 4.2,
            "Drive - Daniel H. Pink": 4.0,
            "The Power of Now - Eckhart Tolle": 4.2,
            "You Are a Badass - Jen Sincero": 4.2,
            "Mindset - Carol Dweck": 4.5,
            "The 7 Habits of Highly Effective People - Stephen Covey": 4.6
        }
    },
    "romantic": {
        "movies": {
            "Pride & Prejudice": 7.8,
            "La La Land": 8.0,
            "The Notebook": 7.8,
            "Titanic": 7.9,
            "Before Sunrise": 8.1,
            "A Walk to Remember": 7.3,
            "About Time": 7.8,
            "Crazy Rich Asians": 7.0,
            "500 Days of Summer": 7.7,
            "Notting Hill": 7.2
        },
        "books": {
            "Pride and Prejudice - Jane Austen": 4.6,
            "The Notebook - Nicholas Sparks": 4.3,
            "Outlander - Diana Gabaldon": 4.2,
            "Me Before You - Jojo Moyes": 4.3,
            "The Time Traveler’s Wife - Audrey Niffenegger": 4.0,
            "Red, White & Royal Blue - Casey McQuiston": 4.2,
            "The Hating Game - Sally Thorne": 4.1,
            "Love & Other Words - Christina Lauren": 4.3,
            "Twilight - Stephenie Meyer": 3.8,
            "To All the Boys I’ve Loved Before - Jenny Han": 4.1
        }
    },
    "adventurous": {
        "movies": {
            "Indiana Jones: Raiders of the Lost Ark": 8.4,
            "The Revenant": 8.0,
            "Pirates of the Caribbean": 8.0,
            "Jurassic Park": 8.1,
            "Mad Max: Fury Road": 8.1,
            "The Lord of the Rings: The Fellowship of the Ring": 8.8,
            "Inception": 8.8,
            "The Secret Life of Walter Mitty": 7.3,
            "Interstellar": 8.6,
            "The Martian": 8.0
        },
        "books": {
            "The Hobbit - J.R.R. Tolkien": 4.7,
            "Treasure Island - R.L. Stevenson": 4.2,
            "The Martian - Andy Weir": 4.4,
            "Into the Wild - Jon Krakauer": 4.1,
            "Life of Pi - Yann Martel": 4.2,
            "Around the World in 80 Days - Jules Verne": 4.1,
            "Hatchet - Gary Paulsen": 4.0,
            "The Call of the Wild - Jack London": 4.0,
            "The 39 Clues - Rick Riordan": 4.1,
            "Eragon - Christopher Paolini": 4.3
        }
    }
}

# Ask user for mood
print("🎭 Moods Available: " + ", ".join(recommendations.keys()))
mood = input("How are you feeling today? ")

# Fetch and display recommendations
if mood in recommendations:
    print(f"\n🎬 Top 10 Movies for your mood ({mood.title()}):")
    for title, rating in recommendations[mood]["movies"].items():
        print(f"- {title} (IMDb: {rating})")

    print(f"\n📚 Top 10 Books for your mood ({mood.title()}):")
    for title, rating in recommendations[mood]["books"].items():
        print(f"- {title} (Rating: {rating})")
else:
    print("Sorry, mood not recognized. Please try one from the list.")# mood-movies
