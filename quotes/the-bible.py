import json
import os
import random

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the JSON file
json_file_path = os.path.join(script_directory, 'the-bible.json')

# Load the JSON data
with open(json_file_path, 'r') as json_file:
    bible_data = json.load(json_file)

# Select a random book
random_book = random.choice(bible_data)
book_name = random_book['name']  # Use the full name of the book

# Select a random chapter from the selected book
random_chapter = random.choice(random_book['chapters'])
chapter_number = random_book['chapters'].index(random_chapter) + 1

# Select a random verse from the selected chapter
random_verse = random.choice(random_chapter)
verse_number = random_chapter.index(random_verse) + 1

# Join the verse lines into a single string with proper spacing
verse_text = ' '.join(random_verse)
# LOL I don't even know man... I kept getting weird outputs, and while goofy, this actually fixed it
# Old output: A r t a x e r x e s ,   k i n g   o f   k i n g s ,   t o   E z r a   t h e   p r i e s t ,   s c r i b e   o f   t h e   l a w   o f   t h e   G o d   o f   h e a v e n ,   a l l   p e a c e ;
# New output: Artaxerxes, king of kings, to Ezra the priest, scribe of the law of the God of heaven, all peace;
verse_text = verse_text.replace("  ", "-") 
verse_text = verse_text.replace(" ", "") 
verse_text = verse_text.replace("-", " ") 

# Print the selected book, chapter, verse, and its content
print("")
print(verse_text)
print(f"{book_name} {chapter_number}:{verse_number}")
print("")