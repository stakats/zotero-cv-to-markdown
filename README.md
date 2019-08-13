# zotero-cv-to-markdown
Panflute (Pandoc python) filter that converts a zotero.org CV to markdown, e.g. for a Jekyll blog page

Usage:
```shell
pandoc -f html -t markdown-raw_html-native_divs-fenced_divs-header_attributes https://zotero.org/{username}/cv/ --filter zotero-cv-to-markdown.py -s -o cv.md
```

