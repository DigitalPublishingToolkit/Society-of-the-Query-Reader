sources=$(shell scripts/expand_toc.py --list toc.md)

all: reader.epub

reader.md: toc.md $(sources)
	scripts/expand_toc.py toc.md --filter ./essay.sh --section-pages > reader.md

reader.epub: reader.md styles.css metadata.xml
	pandoc \
		--self-contained \
		--epub-chapter-level=2 \
		--epub-stylesheet styles.css \
		--epub-metadata metadata.xml \
		--toc-depth=2 \
		-o reader.epub \
		reader.md
