import re


def match_path(path, patterns):
    if path == "/":
        path = "<front>"

    path = path.lstrip("/")

    replace_regex = {
        '(\r\n?|\n)': '|',   # newlines
        '\*': '.*',   # asterisks
        #'<front>': '\b' + re.escape('/') + '\b', 
        '<front>': '<front>',
    }
    
    for k, v in replace_regex.items():
        patterns = re.sub(k, v, patterns)
    
    patterns = '^' + patterns + '/?$'

    return bool(re.findall(patterns, path))

