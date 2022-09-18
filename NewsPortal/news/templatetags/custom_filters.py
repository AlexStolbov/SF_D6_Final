from django import template

register = template.Library()

SWEAR_WORDS = [
    'ругань1',
    'ругань2',
    'ругань3',
]


@register.filter()
def censor(value):
    res = value

    print(value)
    print(type(value))

    if type(value) == str:
        for swear_word in SWEAR_WORDS:
            res = res.replace(swear_word, '****')
            res = res.replace(swear_word.capitalize(), '****')

    print(res)

    return res
