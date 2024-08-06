from name_function import get_formatted_name

def test_city_country_name():
    """Do names like 'Stockholm Sverige' work?"""
    formatted_name = get_formatted_name('stockholm', 'sverige')
    assert formatted_name == 'Stockholm Sverige'


