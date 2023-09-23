favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.lower())
    if name in friends:
        language = favorite_languages[name].upper()
        print(f"\t{name.title()}, I see you love {language}!")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    print(favorite_languages[name].upper())