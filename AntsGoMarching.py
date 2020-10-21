
forth_lines = ["The little one stops to suck his thumb",
               "The little one stops to tie his shoe",
               "The little one stops to climb a tree",
               "The little one stops to shut the door",
               "The little one stops to take a dive",
               "The little one stops to pick up sticks",
               "The little one stops to pray to heaven",
               "And they all go marching down into the ground",
               "The little one stops to suck his thumb",
               'The little one stops to "THE END"']


def sing_verse(verse_number):
    print(f"The ants go marching {verse_number} by {verse_number}, hurrah, hurrah")
    print(f"The ants go marching {verse_number} by {verse_number}, hurrah, hurrah")
    print(f"The ants go marching {verse_number} by {verse_number},")
    print(forth_lines[verse_number - 1])
    print("And they all go marching down to the ground")
    print("To get out of the rain, BOOM! BOOM! BOOM!")

def main():
    for verse_number in range(1,11,1):
        sing_verse(verse_number)

main()

