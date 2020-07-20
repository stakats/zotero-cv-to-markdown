#!/usr/bin/env python3

"""
Panflute filter that converts a zotero.org CV to markdown for a Jekyll blog page
Usage:
	pandoc -f html -t markdown-raw_html-native_divs-fenced_divs-header_attributes https://zotero.org/{username}/cv/ --filter zotero-cv-to-markdown.py -s -o cv.md
"""

import panflute
import datetime

def prepare(doc):
	doc.entries = []

def action(elem, doc):
	if isinstance(elem, panflute.Div):
		if "profile_cvEntry" in elem.classes:
			doc.entries.append(elem)

def finalize(doc):
	temp_entries = doc.entries
	doc.content = []

	now = datetime.datetime.now(datetime.timezone.utc)
	datestamp = now.astimezone().isoformat('T', 'seconds')

	# customize the YAML below as desired for the generated CV
	doc.metadata = {'title':'CV', 'date':datestamp, 
	'layout':'page', 'custom_css': 'cv', 'permalink':'/cv/'
		}

	for entry in temp_entries:
		doc.content.append(entry)

def main(doc=None):
    return panflute.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
