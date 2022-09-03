from scripts.common import preprocess, campaign, analyzer


def get_company(sentence: str) -> bool or None:
    words = list(map(preprocess, sentence.split()))
    if campaign not in words:
        return None
    start = words.index(campaign) + 1
    end = start + 1
    for idx in range(start, len(words)):
        item = analyzer.parse(words[idx])[0]
        if item.tag.POS == 'NOUN':
            end = idx + 1
            break
    return ' '.join(words[start:end])

def extract_companies(introduces: list) -> list:
    names = [get_company(sent) for sent in introduces]
    return names