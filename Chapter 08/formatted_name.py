#Get defenition name and parameters first name and last name
def get_formatted_name(first_name, last_name):

    """Return a full name, neatly formatted."""
    # Full name is created as a new variable with first name and last name and also neatly formatted with space etc
    full_name = first_name + ' ' + last_name

    # Return the full name variable and alos with title for both first and lastname that is in full name
    return full_name.title()

# New variable named musician that take in the defenition and wiht a first name as jimi and lastname as hendrix
musician = get_formatted_name('tommy', 'kravljanac')

# Print out new variable musician
print(musician)