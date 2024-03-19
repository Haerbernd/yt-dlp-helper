import re


def list_to_pretty_string(list_that_will_be_converted, keep_comma=True, replace_comma_with_newline=False,
                          add_newline_after_comma=False):
    list_that_will_be_converted = str(list_that_will_be_converted)
    list_that_will_be_converted = re.sub('\\[', '', list_that_will_be_converted)
    list_that_will_be_converted = re.sub(']', '', list_that_will_be_converted)
    list_that_will_be_converted = re.sub("'", '', list_that_will_be_converted)
    if replace_comma_with_newline:
        list_that_will_be_converted = re.sub(', ', ',\n', list_that_will_be_converted)
    if add_newline_after_comma:
        list_that_will_be_converted = re.sub(', ', ',\n', list_that_will_be_converted)
    if not keep_comma:
        list_that_will_be_converted = re.sub(',', '', list_that_will_be_converted)
    return list_that_will_be_converted
