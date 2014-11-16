# Makefile for the Society of Query Reader, Institute of Network Cultures
#
# Developed as part of the Digital Publishing Toolkit
# (C) 2014 Contributors to the Digital Publishing Toolkit
#
# License: [GPL3](http://www.gnu.org/copyleft/gpl.html)
#
# This code has been developed as part of the [Digital Publishing Toolkit](http://digitalpublishingtoolkit.org).
# with the support of Institute for [Network Cultures](http://networkcultures.org)
# and [Creating 010](http://creating010.com).

# Get the list of sources from the table of contents file using expand_toc's list option
# This variable allows make to be smart and rerun rules below when source files change
#

# Default target (cause it's first): Make epub + trailer
all: epub trailer
epub: SotQreader.epub
trailer: SotQreader-trailer.gif
pdf: SotQreader.pdf

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
		--to epub3 \
		-o SotQreader.epub \
		SotQreader.md
	mv SotQreader.epub SotQreader.tmp.epub
	python scripts/epubutils.py open SotQreader.tmp.epub --output SotQreader
	python scripts/patch_toc.py SotQreader
	python scripts/epubutils.py zip SotQreader.epub --input SotQreader
	rm SotQreader.tmp.epub
	# rm -rf SotQreader
	#	--table-of-contents \


# PDF (via xelatex)
SotQreader.pdf: SotQreader.md SotQreader-auto-metadata.xml
	pandoc \
	--from markdown \
	--to latex \
	--self-contained \
	--epub-metadata=SotQreader-auto-metadata.xml \
	--default-image-extension png \
	--table-of-contents \
	-o SotQreader.pdf \
	--latex-engine=xelatex \
	SotQreader.md

# Trailer (this rule works for any epub)
%-trailer.gif: %.epub
	python scripts/epubtrailer.py $< --width 320 --height 240 --duration=0.5 -o $@

# markdown sources
sources=$(shell scripts/expand_toc.py --list SotQreader.toc.md)

# Rule to build the entire book as a single markdown file from the table of contents file using expand_toc.py
SotQreader.md: SotQreader.toc.md $(sources)
	> $@
	cat SotQreader.title.md >> $@
	scripts/expand_toc.py SotQreader.toc.md --section-pages --filter scripts/chapter.sh | \
	python scripts/enable_links_markdown.py >> $@

# Rule to extract authors names from the different sources
SotQreader-auto-authors.xml: $(sources)
	python scripts/dump_authors.py $(sources) > SotQreader-auto-authors.xml

# Add the manual metadata to the extracted author names
SotQreader-auto-metadata.xml: SotQreader-auto-authors.xml SotQreader-metadata.xml
	cat SotQreader-metadata.xml SotQreader-auto-authors.xml > SotQreader-auto-metadata.xml

HTML = $(sources:source/%.md=build/web/%.html)

web: $(HTML)

# This implicit rule tells make how to create separate web pages
# from markdown sources for web publishing (todo: use template)
#
build/web/%.html: source/%.md
	mkdir -p build/web
	pandoc \
	--css SotQreader.web.css \
	--standalone \
	-o $@ \
	$< \


clean:
	rm build/web/*.html

# special rule for debugging variable names in this makefile
print-%:
	@echo '$*=$($*)'


upload:
	scp SotQreader.epub kafka@pandoc.networkcultures.org:/var/www
