# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country,
# population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'Paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Paris is known as the "City of Light" and is famous for the Eiffel Tower.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous city in the world.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'New York is known for the Statue of Liberty and Central Park.'
    }
}
# print(cities['city'][info][value])
# print(cities['Paris']['country'])

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\n {country}")
    print(f"It has a population of about {population}")
    print(fact)
