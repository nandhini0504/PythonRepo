def mutate_string(string, position, character):
    char_array = list(string)
    char_array.insert(position, character)
    mutated_string = ''.join(char_array)
    return mutated_string
