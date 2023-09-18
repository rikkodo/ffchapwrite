#!python3

import re
import sys


def readChaps(chapsPath: str) -> str:
    """
    チャプタファイルの読み込み

    00:00:00 xxxx
    00:01:23 yyyy
    形式をチャプタ形式に変換して返す

    """
    chapters = list()

    text = "lyrics="

    with open(chapsPath, 'r') as f:
        for line in f:
            text += line.rstrip() + " "
            x = re.match(r"(\d{1,2}):(\d{2}):(\d{2})\s+(.*)", line)
            hrs = int(x.group(1))
            mins = int(x.group(2))
            secs = int(x.group(3))
            title = x.group(4)

            minutes = (hrs * 60) + mins
            seconds = secs + (minutes * 60)
            timestamp = (seconds * 1000)
            chap = {
                "title": title,
                "startTime": timestamp
            }
            chapters.append(chap)

    text += "\n"

    for i in range(len(chapters)-1):
        chap = chapters[i]
        title = chap['title']
        start = chap['startTime']
        end = chapters[i+1]['startTime']-1
        text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""

    return text


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Usage {sys.argv[0]} chapter_file", file=sys.stderr)
        exit(1)

    chaptxt = readChaps(sys.argv[1])
    print(chaptxt, end=None)
