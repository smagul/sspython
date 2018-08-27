rock = []
country = []

def collect_songs():
    song = "Enter the music. "
    ask = "Enter the r (rock) or c (country). Enter the X for exit "

    while True:
        genre = input(ask)
        if genre == "X":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)
        elif genre == "c":
            cy = input(song)
            country.append(cy)
        else:
            print("Wrong.")

    print(rock)
    print(country)


collect_songs()
