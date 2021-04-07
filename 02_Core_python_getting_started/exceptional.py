import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = (int(number))
        print(f"Conversion succeded! x = {x}")

    # except KeyError:
    #     print("Conversion failed!")
    #     x = -1

    except (TypeError, KeyError) as e:
        print(f"Conversion eror: {e!r}",
            file=sys.stderr)
        return -1
    return x