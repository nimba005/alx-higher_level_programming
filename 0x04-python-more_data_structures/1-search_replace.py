#!/usr/bin/python3
def search_replace(my_list, search, replace):
	"""replaces all occurences of an element by another in a new list."""
	new_list = [replace if item == search else item for item in my_list]
	return new_list
