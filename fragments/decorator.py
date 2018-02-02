#
# Create on 1/24/2018
#
# Author: Sylvia
#

"""
Decorator
Given a string, format it as required, and wrap it with html tags.
"""


class Decorator:
    @staticmethod
    def add_tag(name):
        def decorator(func):
            def wrapper(text):
                value = func(text)
                return "<{name}>{value}<{name}>".format(name=name, value=value)

            return wrapper

        return decorator


class Formatter:
    @staticmethod
    def stripper(text):
        value = text.strip()
        return value

    @staticmethod
    def uppper(text):
        value = text.upper()
        return value


class Realizer:
    # get stripped text with 'div' and 'p' tags
    @staticmethod
    @Decorator.add_tag('div')
    @Decorator.add_tag('p')
    def my_stripper(text):
        return Formatter.stripper(text)

    # get upper text with 'h5' tag
    @staticmethod
    @Decorator.add_tag('h5')
    def my_upper(text):
        return Formatter.uppper(text)


if __name__ == '__main__':
    print Realizer.my_stripper('  cool  ')
    print Realizer.my_upper('cool')
