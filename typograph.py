import re
from collections import OrderedDict

def typograph(source):

    result = source.strip()

    # dict of tuples with compiled expressions and strings to replace
    rules = OrderedDict({
        'whitespaces': (
            re.compile(r' {2,}'), r' '),
        'newlines': (
            re.compile(r'\s{3,}'), r'\n\n'),
        'mdash': (
            re.compile(r' - '), r'&nbsp;&mdash; '),
        'short_words': (
            re.compile(r'( [\D{1,2}])( )([\w+])'), r'\1&nbsp;\3'),
        'digits': (
            re.compile(r'(\d+)( )(\w+)'), r'\1&nbsp;\3'),
        'phones': (
            re.compile(r'(\d)(-)(\d)'), r'\1&ndash;\3'),
        'quotes': (
            re.compile(r"""
                        (?<!<)
                        ["\'] # left quotes
                        (.+?) # quoted text
                        ["\'] # right quotes
                        (?!>)
                        """, re.VERBOSE), r'&laquo;\1&raquo;'),
        })

    for prog, string in rules.values():
        result = prog.sub(string, result)

    return result
