def nth_letter(words):
    if not words:
        return ""
    result = ""
    for i in range(len(words)):
        result = result + words[i][i]
    return result
