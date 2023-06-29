import chardet
import urllib.request


def get_coding_file(filename: str):
    detector = chardet.UniversalDetector()

    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done:
            break

    detector.close()
    return detector.result


def get_coding_url(url: str):
    data = urllib.request.urlopen(url).read()
    return chardet.detect(data)
