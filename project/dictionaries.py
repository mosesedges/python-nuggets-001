

# *********** CREATING DICTIONARIES **************

my_dict = {'England': 'London', 'Italy': 'Rome', 'India': 'Mumbai'}
our_dict = dict([('friend', 'Aiden'), ('car', 'BMW'), ('colour', 'blue')])

# print('{1}, {0}'.format(my_dict, our_dict))
# Output // {'friend': 'Aiden', 'car': 'BMW', 'colour': 'blue'}, {'England': 'London', 'Italy': 'Rome', 'India': 'Mumbai'}


# *********** LOOKING INTO DICTIONARIES **************

country = my_dict['Italy']
fav_colour = our_dict.get('friend')

print('%s is the country of  %s' % (country, fav_colour))
# Output // Rome is the country of Aiden

keys = my_dict.keys()
values = my_dict.values()
items = our_dict.items()

print(keys)
# Output // dict_keys(['England', 'Italy', 'India'])

print(values)
# Output // dict_values(['London', 'Rome', 'Mumbai'])

print(items)
# Output // dict_items([('friend', 'Aiden'), ('car', 'BMW'), ('colour', 'blue')])


# *********** ADDING TO THE DICTIONARIES **************

my_dict['Portugal'] = 'Lisbon'
my_dict['USA'] = 'Washington DC'
my_dict['Denmark'] = 'Copenhagen'

# print(my_dict)
# Output // {'England': 'London', 'Italy': 'Rome', 'India': 'Mumbai', 'Portugal': 'Lisbon', 'USA': 'Washington DC', 'Denmark': 'Copenhagen'}


# *********** REPLACING PART OF A DICTIONARIES **************

my_dict['England'] = 'New castle'
my_dict['Portugal'] = 'Fatima'
print(my_dict)

# Output // {'England': 'New castle', 'Italy': 'Rome', 'India': 'Mumbai', 'Portugal': 'Fatima', 'USA': 'Washington DC', 'Denmark': 'Copenhagen'}

# *********** DELETE PART OF A DICTIONARIES **************
del my_dict['Portugal']
print(my_dict)

# *********** LOOK IF A DATA EXIST IN A DICTIONARIES *************
if'England' in my_dict:
    print('true')
