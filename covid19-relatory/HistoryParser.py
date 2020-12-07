def ReadHistoryContent(history_file):
    """ Read a history file and return its contents. """
    file_object = open(history_file, 'r')
    content = file_object.readlines()
    valid_content = []
    for line in content:
        line = line.replace("\n", "")
        if line[0] != "[":
            valid_content.append(line)

    return valid_content

