#!/usr/bin/python3
"""returns a set of common element in two sets"""
def common_elements(set_1, set_2):
	my_new_set = set_1.intersection(set_2)
	return my_new_set
