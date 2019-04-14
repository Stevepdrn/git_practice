# Welcome to The Boredless Tourist, an online application giving you the power to find
# the parts of the city that fit the pace of your life.
# We at The Boredless Tourist run a recommendation engine using Python.
# We first evaluate what a person’s interests are
# and then give them recommendations in their area
# to venues, restaurants, and historical destinations that we think they’ll be engaged by

destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# Remove # print(get_destination_index("Paris, France"))


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# Remove # test_destination_index = get_traveler_location(test_traveler)
# Remove # print(test_destination_index)

attractions = [[] for dest in destinations]
# print(attractions)


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(
            attraction)  # Not sure why add this variable! CHECK!!
    except ValueError:
        print("Sorry, destination doesn't exist")
        return


add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
# print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Finding best places to go


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)  # Not Sure!
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    # CHECK THIS SYNTAX FOR THE LOOP: possible_attraction = [for attraction in attractions_in_city]
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                # The [0] returns just the name of the attraction without the tag ["art", "museum"]
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


# la_arts = find_attractions("Los Angeles, USA", ["art"])
# print(la_arts)


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interest = traveler[2]
    traveler_attractions = find_attractions(
        traveler_destination, traveler_interest)
    interests_string = "Hi " + \
        traveler[0] + ", we think you'll like these places around " + \
        traveler_destination + ": "

    """If last attraction in list add a period, else add a coma plus space"""

    for i in range(len(traveler_attractions)):
        """Extra logic check to see if attraction we are on it's the last one< if it is format the interests_string differently"""
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ", "

    return interests_string


smills_france = get_attractions_for_traveler(
    ['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
