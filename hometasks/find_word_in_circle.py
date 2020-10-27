def find_word_in_circle(circle, word):
    if len(word) == 0 or len(circle) == 0:
        return -1
    if len(circle) < len(word):
        full_circle = circle * int((len(word) / len(circle)))
    else:
        full_circle = circle + circle[:len(word) - 1]
    index = full_circle.find(word)
    if index != -1:
        return index, 1
    else:
        reverse_circle = circle[::-1] + circle[:len(word) - 1:-1]
        index = reverse_circle.find(word)
        if index != -1:
            return len(circle) - index - 1, -1
    return -1
