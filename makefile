# Makefile for the Society of Query Reader, Institute of Network Cultures
#
# Developed as part of the Digital Publishing Toolkit
# (C) 2014 Contributors to the Digital Publishing Toolkit
#
# License: GPL3
#
# This code has been developed as part of the [Digital Publishing Toolkit](http://digitalpublishingtoolkit.org).
# with the support of Institute for [Network Cultures](http://networkcultures.org)
# and [Creating 010](http://creating010.com).

# Get the list of sources from the table of contents file using expand_toc's list option
# This variable allows make to be smart and rerun rules below when source files change
#
sources=$(shell scripts/expand_toc.py --list SotQreader.toc.md)

# Default target (cause it's first): Make epub + trailer
all: SotQreader.epub SotQreader-trailer.gif

# Rule to extract authors names from the different sources
SotQreader-auto-authors.xml: $(sources)
	python scripts/dump_authors.py $(sources) > SotQreader-auto-authors.xml

# Add the manual metadata to the extracted author names
SotQreader-auto-metadata.xml: SotQreader-auto-authors.xml SotQreader-metadata.xml
	cat SotQreader-metadata.xml SotQreader-auto-authors.xml > SotQreader-auto-metadata.xml

# Rule to build the entire book as a single markdown file from the table of contents file using expand_toc.py
SotQreader.md: SotQreader.toc.md $(sources)
	scripts/expand_toc.py SotQreader.toc.md --filter scripts/chapter.sh > $@

# Main Epub builder, use the files generated from above to create the final epub
SotQreader.epub: SotQreader.md SotQreader-auto-metadata.xml SotQreader.css SotQreader-cover.png
	pandoc \
		--from markdown \
		--self-contained \
		--epub-chapter-level=2 \
		--epub-stylesheet=SotQreader.css \
		--epub-cover-image=SotQreader-cover.png \
		--epub-metadata=SotQreader-auto-metadata.xml \
		--epub-embed-font=fonts/FreeUniversal-Regular.ttf \
		--epub-embed-font=fonts/FreeUniversal-Bold.ttf \
		--toc-depth=2 \
		-o SotQreader.epub \
		SotQreader.md

# Implicit rule to convert any epub into a trailer gif with epubtrailer.py
%-trailer.gif: %.epub
	python scripts/epubtrailer.py $< --width 320 --height 240 --duration=0.5 -o $@

# special rule for debugging variable names in this makefile
print-%:
	@echo '$*=$($*)'
