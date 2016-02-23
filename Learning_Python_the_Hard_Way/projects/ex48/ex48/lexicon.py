directions_list = ['north', 'south', 'east', 'west', 'up', 'down',
                   'left', 'right', 'back']

verbs_list = ['go', 'stop', 'kill', 'eat']

stop_list = ['the', 'in', 'of', 'from', 'at', 'it']

nouns_list = ['door', 'bear', 'princess', 'cabinet']

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    # break sentence up into list of lowercase words
    words = sentence.lower().split()

    # initialize result
    scan_result = []

    for word in words:
        # check if word matches any of the tuples
        if word in directions_list:
            scan_result.append(('direction', word))
        elif word in verbs_list:
            scan_result.append(('verb', word))
        elif word in stop_list:
            scan_result.append(('stop', word))
        elif word in nouns_list:
            scan_result.append(('noun', word))
        elif (convert_numbers(word) != None):
            scan_result.append(('number', convert_numbers(word)))
        else:
            scan_result.append(('error', word))

    # return the result
    return scan_result