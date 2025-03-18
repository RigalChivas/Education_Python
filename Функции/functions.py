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


# res_two = merge_list_to_dict([13], ['a', 'b', 'c', 'd'])

# значение функции по умолчанию
# def multi_by_factor(value, multiplier=1):
#     return value * multiplier

# print(multi_by_factor(5, 2))
# print(multi_by_factor(5))

# from datetime import date

# def get_weekday():
#     return date.today().strftime('%A')

# def create_new_post(post, weelday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weelday
#     return post_copy

# initial_post = {
#     'id':243,
#     'author': 'Jack',
#     'text': 'Hello, world!'
# }

# post_with_weekday = create_new_post(initial_post)

# print(post_with_weekday)

