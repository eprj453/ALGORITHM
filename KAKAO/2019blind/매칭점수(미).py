import re

def get_url(html):
    start, end = html.index('<head>')+6, html.index('</head>')
    head = html[start:end]

    url = ''
    for metadata in head.splitlines():
        if 'content' in metadata:
            is_url = False
            for ch in metadata[metadata.index('content'):]:
                if is_url and ch == '"':
                    break
                if is_url:
                    url += ch
                if ch == '"':
                    is_url = True

    return url

def analyze_body(html):
    start, end = html.index('<body>') + 6, html.index('</body>')
    body = html[start:end]
    # for c

def solution(word, pages):
    answer = 0
    for p in pages:
        basic, link, match, url = 0, 0, 0, 0
        analyze_body(p)
        # print(p.index('<head>'))
    return answer

html = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

# print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
# ))


m = re.findall('.aba.', ' aba@aba aba ')
print(m)