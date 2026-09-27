# nicFW880_950_Docs

Markdown files for the nicFW880/950 documentation wiki.

## Offline PDF edition

The complete wiki is also available as a single offline PDF:

* [RMS880_950_Documentation.pdf](RMS880_950_Documentation.pdf)

Regenerate it from the Markdown source with only Python 3:

```sh
python3 tools/build_wiki_pdf.py
```

The generator preserves the Home page's navigation order, includes every wiki
page except the GitHub sidebar, and renders headings, lists, block quotes, and
tables for readable offline reference.
