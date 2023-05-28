def crypt_cesar(some_text, step):
    result = ""
    alf = [
        "a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x",
        "y", "z"
    ]
    for i in some_text:
        ind = alf.index(i)
        if (ind + step) > len(alf) - 1:
            ind = (ind + step) - (len(alf) - 1)
            result += alf[ind]
        else:
            result += alf[ind + step]

    return result


def decrypt_cesar(some_text, step):
    result = ""
    alf = [
        "a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x",
        "y", "z"
    ]
    for i in some_text:
        ind = alf.index(i)
        if (ind - step) > len(alf) - 1:
            ind = (ind - step) - len(alf)
            result += alf[ind]
        else:
            result += alf[ind - step]
    return result


print(crypt_cesar("abc", 3))
print(decrypt_cesar("def", 3))
