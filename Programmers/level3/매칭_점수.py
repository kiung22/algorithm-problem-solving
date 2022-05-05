import re


def get_url(page):
    pattern = r"<meta property=\"og:url\" content=\"https://(?P<url>\S+)\""
    m = re.search(pattern, page)
    if m:
        return m.group("url")
    return None


def get_links(page):
    pattern = r"<a href=\"https://(\S+)\""
    m = re.findall(pattern, page)
    return m


def get_word_score(word, page):
    pattern = f"({word})[^a-zA-Z]"
    m = re.findall(pattern, page, re.I)
    return len(m)


def solution(word, pages):
    N = len(pages)
    url_dict = {}
    word_score = [0] * N
    links = []
    link_score = [0] * N

    for i, page in enumerate(pages):
        url = get_url(page)
        url_dict[url] = i
        links.append(get_links(page))
        word_score[i] = get_word_score(word, page)
    
    for i in range(N):
        if not links[i]:
            continue
        score = word_score[i] / len(links[i])
        for url in links[i]:
            idx = url_dict.get(url)
            if idx is None:
                continue
            link_score[idx] += score

    max_value = 0
    answer = 0
    for i in range(N):
        if word_score[i] + link_score[i] > max_value:
            max_value = word_score[i] + link_score[i]
            answer = i

    return answer
