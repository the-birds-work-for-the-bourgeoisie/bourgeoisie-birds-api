from typing import List


def validate_data_keys(data, keys: List[str]) -> bool:
    return all(map(lambda k: k in data and len(data[k]) == 1, keys))

def validate_initials(initials: str) -> str or None:
    initials = initials.strip().upper()
    if len(initials) == 3 and initials.isascii() and initials.isalpha():
        return initials
    return None

def validate_score(score: str) -> int or None:
    score = score.strip()
    if score.isdigit() and len(score) < 10:
        return int(score)
    return None


if __name__ == '__main__':
    # tests
    assert(not validate_data_keys({}, ["initials"]))
    assert(not validate_data_keys({"initials": []}, ["initials"]))
    assert(not validate_data_keys({"initials": ["", ""]}, ["initials"]))
    assert(not validate_data_keys({"score": ["9"]}, ["initials"]))
    assert(not validate_data_keys({"initials": [], "score": ["9"]}, ["initials"]))
    assert(not validate_data_keys({"initials": ["", ""], "score": ["9"]}, ["initials"]))
    assert(validate_data_keys({"initials": [""]}, ["initials"]))
    assert(validate_data_keys({"initials": ["asd"]}, ["initials"]))
    assert(validate_data_keys({"initials": [""], "score": ["9"]}, ["initials", "score"]))

    assert(validate_initials("abc") == "ABC")
    assert(validate_initials("hs1") == None)
    assert(validate_initials("<br>") == None)
    assert(validate_initials("äaa") == None)
    assert(validate_initials("ABC") == "ABC")

    assert(validate_score("abc") == None)
    assert(validate_score("hs1") == None)
    assert(validate_score("<br>") == None)
    assert(validate_score("äaa") == None)
    assert(validate_score("ABC") == None)
    assert(validate_score("591837598273589723298375") == None)
    assert(validate_score("1") == 1)
    assert(validate_score("2") == 2)
    assert(validate_score("2981274") == 2981274)