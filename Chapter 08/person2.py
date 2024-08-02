def build_person(first_name, last_name, age=''):
    person = {'frist': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=54)
print(musician)

musician = build_person('tommy', 'kravljanac')
print(musician)

musician = build_person('julian', 'hedstig', age=10)
print(musician)