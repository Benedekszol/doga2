def get_letter_stat(text: str) -> dict[str, int]:
    stat = dict({"vowel": 0, "consonant": 0})
    for l in text:
        if l in ["a", "e", "i", "o", "u"]:
            stat["vowel"] += 1
        else:
            stat["consonant"] +=1
    return stat

print(get_letter_stat("almafa")) 

