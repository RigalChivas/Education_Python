#избегаем создания объекат внутри функции

# def increase_persin_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy
# person_one = {
#     'name': 'Jack',
#     'age': 23
# }

# new_person = increase_persin_age(person_one)
# print(new_person[ 'age'])
# print(person_one['age'])

# def merge_list_to_dict(list_one, list_two):
#     zipped_seq = zip(list_one, list_two)
#     return dict(zipped_seq)


# res_one = merge_list_to_dict([1, 2, 3], ['a', 'b', 'c'])
# print(res_one)


res_two = merge_list_to_dict([13], ['a', 'b', 'c', 'd'])
