# Makefile for Digital Publishing Toolkit
#

sourcemd = $(wildcard source/*.md)

buildmd = $(patsubst source/%,build/%,$(sourcemd))

all : SotQreader.epub

print-%:
	@echo '$*=$($*)'

authors.xml : $(sourcemd)
	python scripts/dump_authors.py $(sourcemd) > authors.xml

metadata.xml : authors.xml metadata.base.xml
	cat metadata.base.xml authors.xml > metadata.xml

SotQreader.epub : $(buildmd) metadata.xml
	pandoc \
	    --self-contained \
	    --table-of-contents \
	    --toc-depth=2 \
	    --epub-chapter-level=2 \
	    --epub-stylesheet=epub.css \
	    --epub-cover-image=images/cover.png \
	    --epub-metadata=metadata.xml \
	    -o SotQreader.epub \
	    sections/section01.md \
	    build/Introduction.md \
	    sections/section02.md \
	    build/Kylie-Jarrett.md \
	    build/Andrea_Miconi.md \
	    build/Vito_Campanelli.md \
	    sections/section03.md \
	    build/Dirk_Lewandowski.md \
	    build/Astrid_Mager.md \
	    build/Ippolita_Pre_Afterword.md \
	    build/Angela_Daly.md \
	    sections/section04.md \
	    build/Richard_Graham.md \
	    build/Tantner.md \
	    sections/section05.md \
	    build/Min_Jiang.md \
	    build/JobinGlassey.md \
	    build/Amanda_Scardamaglia.md \
	    build/Martin-Reiche_Ulrich-Gehmann.md \
	    sections/section06.md \
	    build/Jacob_Ormen.md \
	    build/Martin_Feuz.md \
	    build/David_Crusoe.md \
	    build/Simon_Knight.md \
	    sections/section07.md \
	    build/Hogan_Luka.md \
	    build/Mahnke_Uprichard.md \
	    build/Jones_Amir.md \
	    sections/section08.md \
	    build/SotQ_Conferences.md \
	    build/Author_Bios.md \
	    build/colophon.md

SotQreader.trailer.gif: SotQreader.epub
	python scripts/epubtrailer.py SotQreader.epub SotQreader.trailer.gif

build/%.md: source/%.md
	if [ ! -d build ]; then mkdir build; fi
	pandoc \
	    --to html  \
	    --template article.head.template.md \
	    $< > $@
	pandoc \
	    --to markdown \
	    --template article.body.template.md \
	    --id-prefix=$<- \
	    --base-header-level=2 \
	    $< >> $@

clean:
	rm -f $(buildmd)

SotQreader.testing.md: $(shell scripts/expand_toc.py --list toc.md)
	scripts/expand_toc.py toc.md --filter scripts/chapter.sh > $@

SotQreader.testing.epub: SotQreader.testing.md
	pandoc \
	    --self-contained \
	    --epub-chapter-level=2 \
	    --epub-stylesheet=epub.css \
	    --epub-cover-image=images/cover.png \
	    --epub-metadata=metadata.xml \
	    --toc-depth=2 \
	    -o $@ \
	    SotQreader.testing.md
