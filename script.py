destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for location in destinations]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = destinations.index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
        return
    except ValueError:
        return
        
def find_attraction(destination, interests):
    attractions_with_interest = []
    #Grabbing the index of the destination in the destination list
    destination_index = get_destination_index(destination)
    #Grabbing the destination's attractions
    attractions_in_city = attractions[destination_index]
    
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
        
    return attractions_with_interest
  
def get_attractions_for_traveler(traveler):
    #location as a string
    traveler_destination = traveler[1]
    #Travelers interests in a list
    traveler_interests = traveler[2]
    #Travelers recommended attractions in a list
    traveler_attractions = find_attraction(traveler_destination, traveler_interests)
    interest_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interest_string += "the " + traveler_attractions[i] + "."
        else:
            interest_string += "the " + traveler_attractions[i] + ", "
    
    return interest_string
      
 
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))