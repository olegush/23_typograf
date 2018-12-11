import re


def typograph(source_text):
    # whitespaces
    result_text = source_text.strip()
    result_text = re.sub(' {2,}', ' ', result_text)
    result_text = re.sub('\s{3,}', '\n\n',  result_text)
    # &mdash;
    result_text = re.sub(' - ', '&nbsp;&mdash; ', result_text)
    # &nbsp; after short words
    result_text = re.sub('( [\D{1,2}])( )([\w+])', r'\1&nbsp;\3', result_text)
    # &nbsp; after digits
    result_text = re.sub('(\d+)( )(\w+)', r'\1&nbsp;\3', result_text)
    # phone numbers
    result_text = re.sub('(\d)(-)(\d)', r'\1&ndash;\3', result_text)
    # quotes
    result_text = re.sub(
        r'(?<!<)["\'](.+?)["\'](?!>)',
        r'&laquo;\1&raquo;',
        result_text
    )
    return result_text
