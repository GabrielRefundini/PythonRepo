# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
mountains = []
rivers = []
languages = []
#add
languages.append('Portuguese')
languages.append('Mandarin')
languages.insert(0, 'Italian')
languages_updated = [
    "Spanish",
    "Hindi",
    "Arabic",
    "French",
    "Bengali",
    "Russian",
    "Japanese"
]
languages.extend(languages_updated)

print(languages)

#remove

del languages[0]
removed = languages.pop(1)
print(f'The language removed was: {removed} and now removing Hindi:')
languages.remove('Hindi')
print(languages)

#sort alphabetically

languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

#sorted alphabetically

print(sorted(languages))

#length + reverse 

languages.reverse()
print (f'{len (languages)} {languages}')
