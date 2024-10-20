import re
my_p = "Arent#123"


def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"[a-z]+")
    uppercase_pattern = re.compile(r"[A-Z]+")
    number_pattern = re.compile(r'[0-9]+')
    special_pattern = re.compile(r"[@#§*!\.°%&$€]+")

    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have  at least 8 symbols ")

    if not re.search(lowercase_pattern, password):
        return (False, "password must have one ore more lower letters")

    if not re.search(uppercase_pattern, password):
        return (False, " password must have one ore more upper letters")

    if not re.search(number_pattern, password):
        return (False, "password must have one ore more number")

    if not re.search(special_pattern, password):
        return (False, "password must have ono ore more special symbols")


print(check_password(my_p))
