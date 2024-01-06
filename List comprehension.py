###Fourth project from FreeCodeCamp
###Learning List Comprension
#####List comprension lets you work with lists without needing to use loops or methods for lists.
###Brush up on __main__
###Double check to see if strip() only handles before and after the item being stripped
###This looks like it only adds characters between words in the spaces.


###Takes a string passed in, and once everything is lowercase it gets added to a list this will also add an underscore
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = "_" + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = "".join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip("_")

    return clean_snake_cased_string


def main():
    print(convert_to_snake_case("aLongAndComplexString"))


if __name__ == "__main__":
    main()


###This is the same of the lines above


def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        "_" + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    return "".join(snake_cased_char_list).strip("_")


def main():
    print(convert_to_snake_case("aLongAndComplexString"))
