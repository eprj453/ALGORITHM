import re
from html.parser import HTMLParser


class Graph:
    def __init__(self):
        self.pages = []
        self.max_matching_score = 0

    def getPageByIndex(self, idx):
        if idx >= len(self.pages):
            return None
        return self.pages[idx]

    def getPageByUrl(self, url):
        for page in self.pages:
            if page.url == url:
                return page
        return None

    def connectLinkedPage(self):
        for page in self.pages:
            url = page.url
            for linked_page in self.pages:
                if url in linked_page.linked_page and linked_page.url != url:
                    page.be_linked_page.add(linked_page.url)


class WebPage:
    def __init__(self, idx):
        self.idx = idx if idx else None
        self.url = ''
        self.basic_score = 0
        self.linked_page = set()
        self.be_linked_page = set()
        self.link_score = 0
        self.matching_score = 0

    def __str__(self):
        return 'url : {}, basic_score : {}, be_linked_page : {}, matching_score : {}'.format(self.url, self.basic_score,
                                                                                             self.be_linked_page,
                                                                                             self.matching_score)


def getTagInHTMLString(string, tag):
    tag_start, tag_end = '<' + tag + '>', '</' + tag + '>'
    if tag_start in string and tag_end in string:
        start, end = string.index(tag_start), string.index(tag_end)
        return string[start:end]
    return ''


def getUrlInHead(string):
    if 'content="' in string and '"/>' in string:
        start, end = string.index('content="') + len('content="'), string.index('"/>')
        return string[start:end]
    return ''


def getLinkInBody(string):
    links = set()
    i = 0
    while i < len(string):
        s = string[i]
        if s == '<' and string[i + 1] == 'a':
            url = ''
            start = i + 9
            while string[start] != '"' and start < len(string):
                url += string[start]
                start += 1
            links.add(url)
            i = start
        else:
            i += 1
    return links


def getLinkScore(p, graph):
    score = 0
    for url in list(p.be_linked_page):
        external_page = graph.getPageByUrl(url)
        if external_page:
            score += (external_page.basic_score / len(external_page.linked_page))
    return score


def getAllCountByString(string, word):
    cnt = 0
    for s in re.split(r' |[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?1234567890]', string):
        if s == word:
            cnt += 1
    return cnt

def deleteEscapeSeq(string):
    i = 0
    result = ''
    while i < len(string):
        if string[i] == '"\"':
            i += 2
        else:
            result += string[i]
            i += 1
    return result


def solution(word, pages):
    answer = 0
    graph = Graph()
    for idx, p in enumerate(pages):
        web_page = WebPage(idx)
        head, body = getTagInHTMLString(p, 'head'), getTagInHTMLString(p, 'body')
        body = deleteEscapeSeq(body)
        web_page.url = getUrlInHead(head)
        web_page.basic_score = getAllCountByString(body.lower(), word.lower())
        web_page.linked_page = getLinkInBody(body)
        graph.pages.append(web_page)

    graph.connectLinkedPage()

    for idx, p in enumerate(graph.pages):
        p.matching_score = p.basic_score + getLinkScore(p, graph)
        if p.matching_score > graph.max_matching_score:
            answer = idx
            graph.max_matching_score = p.matching_score
    return answer

html = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

for h in html:
    print(h)
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
))