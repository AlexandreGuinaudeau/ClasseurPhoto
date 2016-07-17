
def pretty_print(object, attributes=None, inline=False, maxline=20, tab=0):
    attribute_dict = object.__dict__
    if attributes is None:
        attributes = sorted(attribute_dict.keys())
    if inline:
        s = "<%s: " % object.__class__.__name__
    else:
        s = "<%s>" % object.__class__.__name__
    for attr in attributes:
        if inline:
            s += ' - '
        else:
            s += '\n'
            s += '\t'*(tab+1)
        if attr in attributes:
            value = str(attribute_dict[attr])
            if len(value) > maxline:
                value = value[:17] + '...'
            s += str(attr) + ':' + value
    if inline:
        s += " >" % object.__class__.__name__
    else:
        s += '\n'
        s += "</%s>" % object.__class__.__name__
    return s
