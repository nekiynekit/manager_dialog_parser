from scripts.common import preprocess, greets, good_anything, good


def detect_greeting(sentence: str) -> bool:
    words = list(map(preprocess, sentence.split()))
    for greet in greets:
        if greet in words:
            return True
    if good not in words:
        return False
    idx = words.index(good) + 1
    if idx < len(words) and words[idx] in good_anything:
        return True
    return False

def mark_greetings(monologue: list) -> list:
    verdict = [detect_greeting(sent) for sent in monologue]
    return verdict