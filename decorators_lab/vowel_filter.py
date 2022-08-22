from functools import wraps


def vowel_filter(function):
    vowels = "aeyuoi"

    @wraps(function)
    def wrapper():
        res = function()
        return [x for x in res if x.lower() in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
