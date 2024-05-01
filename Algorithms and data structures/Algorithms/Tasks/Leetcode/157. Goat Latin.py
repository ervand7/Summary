# my solution
def to_goat_latin(sentence: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    sentence = sentence.split()
    result = []
    counter = 1
    for word in sentence:
        if word[0].lower() in vowels:
            result.append(word + "ma" + ("a" * counter))
        else:
            result.append(word[1:] + word[0] + "ma" + ("a" * counter))

        counter += 1

    return " ".join(result)
