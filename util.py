def split_arr_zeros(arr, split_zeros=0):
    zeros_counter = 0
    counter = 0
    ans = []
    while arr and arr[-1] == 0:
        arr.pop()
    start = 0
    for num in arr:
        if num == 0:
            zeros_counter += 1
        else:
            zeros_counter = 0
        counter += 1
        if zeros_counter == split_zeros:
            ans.append(arr[start:start + counter - split_zeros])
            start += counter
            counter = 0
            zeros_counter = 0
    ans.append(arr[start:])
    return ans

def find_key_by_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None