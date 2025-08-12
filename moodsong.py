import random
import time

# Mood to songs mapping
mood_songs = {
    "happy": [
        "Happy - Pharrell Williams",
        "Best Day of My Life - American Authors",
        "Uptown Funk - Mark Ronson ft. Bruno Mars"
    ],
    "sad": [
        "Someone Like You - Adele",
        "Let Her Go - Passenger",
        "Fix You - Coldplay"
    ],
    "energetic": [
        "Eye of the Tiger - Survivor",
        "Stronger - Kanye West",
        "Can't Stop the Feeling - Justin Timberlake"
    ],
    "relaxed": [
        "Weightless - Marconi Union",
        "River Flows in You - Yiruma",
        "Thinking Out Loud - Ed Sheeran"
    ]
}

print("🎵 Welcome to Mood-Based Music Recommender 🎵")
print("Available moods: Happy, Sad, Energetic, Relaxed")

# Get user mood
mood = input("Enter your mood: ").strip().lower()

# Recommend song
if mood in mood_songs:
    print("\nFinding the perfect song for your mood...")
    time.sleep(1.5)  # just for effect
    song = random.choice(mood_songs[mood])
    print(f"🎧 Recommended Song: {song}")
else:
    print("❌ Sorry, I don't recognize that mood.")
