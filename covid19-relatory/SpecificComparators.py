def FloatComparator(older_array, new_array):
    special_indexes = [2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 16, 17]
    diferences = []
    for index in range(len(older_array)):
        if index in special_indexes:
            older_value = float(older_array[index])
            new_value = float(new_array[index])
            if new_value > older_value:
                diference = "+"
            elif new_value < older_value:
                diference = "-"
            else:
                diference = "="

        else:
            diference = ""

        diferences.append(diference)

    return diferences
