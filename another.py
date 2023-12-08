def calculate_beer_volume(total_volume, num_people):
    try:
        total_volume = float(total_volume)
        num_people = int(num_people)

        if total_volume <= 0 or num_people <= 0:
            return "Total volume and number of people must be positive numbers."

        beer_per_person = total_volume / num_people
        return beer_per_person
    except ValueError:
        return "Please enter valid numeric values for total volume and number of people."

def main():
    total_volume = input("Enter the total volume of beer (in liters): ")
    num_people = input("Enter the number of people: ")

    beer_per_person = calculate_beer_volume(total_volume, num_people)

    if isinstance(beer_per_person, float):
        print(f"Each person will be served {beer_per_person:.2f} liters of beer.")
    else:
        print(beer_per_person)

if __name__ == "__main__":
    main()
