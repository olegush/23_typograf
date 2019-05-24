import re
from collections import OrderedDict

def typograph(source):

    result = source.strip()

    # dict of tuples with patterns and strings to replace
    rules = OrderedDict({
        'whitespaces': (r' {2,}', r' ', 0),
        'newlines': (r'\s{3,}', r'\n\n', 0),
        'mdash': (r' - ', r'&nbsp;&mdash; ', 0),
        'short_words': (r'( [\D{1,2}])( )([\w+])', r'\1&nbsp;\3', 0),
        'digits': (r'(\d+)( )(\w+)', r'\1&nbsp;\3', 0),
        'phones': (r'(\d)(-)(\d)', r'\1&ndash;\3', 0),
        'quotes': (r"""
                    (?<!<)
                    ["\'] # left quotes
                    (.+?) # quoted text
                    ["\'] # right quotes
                    (?!>)
                    """, r'&laquo;\1&raquo;', re.VERBOSE),
        })

    for pattern, string, flags in rules.values():
        prog = re.compile(pattern, flags)
        result = prog.sub(string, result)

    return result
