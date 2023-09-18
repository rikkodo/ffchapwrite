# ffchapwrite

ffmpegでm4aにチャプタを追加する。同時に、チャプタに設定したテキストを歌詞に加える。

## 使い方

```sh
work.sh file.m4a chapter.txt
```

## フォーマット

chapter.txtは以下形式とする。

```txt
HH:mm:ss title
...
HH:mm:ss end
```

## 注意点

chapter.txtの最終行に、ファイルの再生時間に合わせたend行がないと最終行が正しく動作しない。

## やりたいこと

歌詞の改行を有効にする。

## 参考

[How to Add Chapters to MP4s with FFmpeg - Kyle Howells](https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg)
