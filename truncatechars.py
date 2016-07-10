def truncatechars(a_string, num_of_chars):
    if len(a_string) > num_of_chars:
        return a_string[:num_of_chars] + "..."
    else:
        return a_string


s = "This is a beautiful world"

print (truncatechars(s, 4))
print (truncatechars(s, 0))
print (truncatechars(s, 100))

