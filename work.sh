#!zsh
# https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg

if [ $# -lt 2 ]; then
    echo "Usage ${0} file.m4a chapter_file

    chapter_file:
    \"\"\"
    00:00:00 xxxx
    00:01:23 yyyy
    ...
    XX:XX:XX end <-- required.
    \"\"\"
    " >&2
    exit 1
fi

TARGET=${1}
CHAPS=${2}

TG_NOSFX=${1%%.*}

META=${TG_NOSFX}_META.txt

TARGET_CHAPS=${TG_NOSFX}_CHAP.${1##*.}

# メタファイルを作成
ffmpeg -i ${TARGET} -f ffmetadata ${META}

# チャプタファイル作成
python3 conv.py ${CHAPS} >> ${META}

# メタファイルを合成
ffmpeg -i ${TARGET} -i ${META} -map_metadata 1 -codec copy ${TARGET_CHAPS}

# 不要メタファイルを削除
rm ${META}
