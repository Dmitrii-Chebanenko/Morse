def find_key_by_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None