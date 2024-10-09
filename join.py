# join is used to join the elements from the iterable

def join_list(list:list[str]) -> str:
    joined_string = " ".join(list)
    return joined_string

l1 = ["ram","shyam","kashyap"]
merge = join_list(l1)
print(merge)

# ram shyam kashyap