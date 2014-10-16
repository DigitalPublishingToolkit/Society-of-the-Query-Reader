#!/bin/bash

scripts/expand_toc.py toc.md --filter ./essay.sh --section-pages > reader.md
pandoc --self-contained --epub-chapter-level=2 --toc-depth=2 -o reader.epub reader.md
