# Makefile for Society of the Query 2 Reader
#
# allmd = $(wildcard *.md )
allmd = $(wildcard *.markdown essays/*.markdown )

derivedhtml = $(patsubst %.markdown,%.html,$(allmd))

all : sotq.epub

sotq.epub : $(derivedhtml)
	ebook-convert TOC.html sotq.epub --cover images/cover.png --title "Society of the Query Reader" --pubdate "22 May 2014" --publisher "Institute of Network Cultures"

%.html: %.markdown
	python scripts/chapter.py $< > $@

clean:
	rm -f $(derivedhtml)
