---
title: "Hybrid workflow how-to: Making automated workflows, part 2"
---

As part of the [INC subgroup][INC], we have been developing a workflow that allows a flexible production of different kinds of electronic outputs like EPUB, PDF, and [book trailers](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/) from a sample collection of essays from the recently published [Society of the Query](http://networkcultures.org/query/) Reader.

In part two of this tutorial, we create a shell script to compile multiple [markdown][markdown] sources into a EPUB-format Reader using [pandoc][pandoc]. We then use a helper script, expand-toc.py, to use a markdown-formatted table of contents to order the contents of the EPUB. Finally, we create a [makefile](http://digitalpublishingtoolkit.org/2014/10/make-book/) to fully automate the build process, and add an [EPUB trailer](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/) as an output.

This tutorial is targeted for developers or people interested in creating automated workflows for producing EPUBs. It assumes basic familiarity with a commandline interface (such as the Terminal application on GNU/Linux or Mac OS X, or the command prompt in Windows).


## Prepare your workspace & tools

Unpack, checkout or copy the sample files from the [github repository](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader). Open the Terminal and use the cd command to enter the "part2" folder in the developer section of the how-to-tutorial files.

```bash
git clone https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader.git

cd how-to-tutorial/developer/part2
```

## Use pandoc to tweak a markdown document to be combinable with others

Any filename given to pandoc on the commandline that is not preceded by an option (such as -o) is considered an input. When you give pandoc multiple input files, pandoc cuts and pastes the different texts together as if they were coming from a single file. While this will sometimes just work, it creates some specific problems for the essays from the Society of the Query:

```bash
pandoc -o reader.epub *.md
```

Produces a lot of warnings:

```bash
pandoc: Duplicate note reference `3' "source" (line 1582, column 1)
pandoc: Duplicate note reference `2' "source" (line 1580, column 1)
pandoc: Duplicate note reference `1' "source" (line 1578, column 1)
```

This is because when treated as a single document, all the footnotes (which use numeric indexes) from the different essays can no longer be differentiated (reference 3 from which essay?).

Besides overlapping footnotes, there may be problems with the hierarchy of the overall document. The individudal essays have been written with their title as level 1, and sections within the essay as level 2. This is fine, but for the final reader we may want to introduce higher level sections (at level one) to for instance group the essays thematically. In that case the essay levels should shift so that their title is level 2, and essay sections level 3. Luckily pandoc has an option to do just that called --base-header-level that (re)sets the "topmost" level of a document when outputting it.

In general, a useful technique is to use pandoc in two passes, first individually on each essay to adjust it for compilation in the larger document. Each altered essay is then pasted in a new master markdown file containing the entire reader document and it is this file that is converted (again by pandoc) to EPUB.

Try the following command:

```bash
pandoc David_Crusoe.md --to markdown --id-prefix=David_Crusoe.md- --base-header-level 2
```

In the resulting markdown output, note the final Notes section:

```markdown
### Notes {#notes .notes}

[^David_Crusoe.md-1]: The Common Core references algebraic set theory in
    its high school appendices. See
    http://www.corestandards.org/assets/CCSSI\_Mathematics\_Appendix\_A.pdf
    for more information.

[^David_Crusoe.md-2]: Way Back Machine, 21 November 1996 archive of ‘How
    to Use Excite Search’,
    http://web.archive.org/web/19961219003220/http://www.excite.com/Info/advanced.html?aqt.

[^David_Crusoe.md-3]: Anthony Stuart, ‘Re: Boolean + Operator Removed?
    Why?’ posting to Google Search Forum, 5 November 2011,
    http://productforums.google.com/forum/\#!searchin/websearch/%22implied\$20and%22/websearch/3oIWbew9xdE/xuKBfNk5wjwJ.
```

First the "Notes" header has shifted from a level 2 to level 3. The "--base-header-level 2" option basically shifts each level by one (in other words what was 1 becomes 2, was 2 becomes 3 and so on).

Additionally, the footnote references now are preceded by the name of the document (and pandoc has changed the matching references in the text as well). This markdown will now combine well with other sources.

Next, let's use a template (see essay-template01.md) to add a custom header and format the authors names:

```markdown
# $title$ {.title}

<div class="separator">&#172;</div>
$for(author)$
<div class="author">$author$</div>
$endfor$

$body$
$for(include-after)$
$include-after$
$endfor$
```

Now putting it all together:

```bash
pandoc David_Crusoe.md --to markdown --template essay-template-01.md --no-wrap --id-prefix=David_Crusoe.md- --base-header-level 2
```

*Devilish detail*: Note the use of the --no-wrap option. This disables pandoc's automatic text wrapping feature when outputting, in this case, markdown. A subtle bug we discovered was that long titles were being line wrapped which would then break the h2 header in the template (where the $title$ variable is expanded on a line starting with ## so that only the first line was considered part of the header). Thankfully this behaviour can be disabled with --no-wrap.


## Use pandoc to convert multiple markdown source files to an EPUB

Open the file build01.sh, it contains the following:

```bash
#!/bin/bash

# blank the reader.md file
> reader.md

# process all the files listed in ESSAYS in a loop
# use >> to append each output to reader.md
for i in `cat ESSAYS`
do
pandoc "$i" \
    --to markdown \
    --template essay-template-01.md \
    --no-wrap \
    --id-prefix="${i}-" \
    >> reader.md

# ensure a blank line at the end of each essay
echo >> reader.md

done

# Make the EPUB from reader.md
pandoc \
    --epub-chapter-level=1 \
    --toc-depth=1 \
    -o reader.epub \
    reader.md
```

Run the build01 script by typing:
```
bash build01.sh
```

*Devilish detail*: When combining all the markdown into a single document, all the footnotes would be merged together and displayed in one large section at the end of the EPUB. A crucial pandoc feature is the --epub-chapter-level option which in addition to splitting the source (back) into separate files (which makes the document lighter for an e-reader), it also puts footnotes back into each individual essay.


## Using a Table of Contents to order the EPUB

In the step above, the names and order of the essays added to the EPUB output is set by using a simple text file (named ESSAYS).

For the INC workflow, we created a custom script (expand-toc.py) that allows a table of contents file written in markdown format to order the contents of the EPUB. The script expects the name of a table of contents file containing (markdown formatted) links to the essays in the order they should appear.

As an additional feature, the table of contents itself is output first allowing a customized table of contents display beyond the automatic table of contents feature of pandoc. To do this, the script remaps the links to the first id found in the linked-to file; for this reason it's important that the individual files (or at least their filtered output, see below) begin with a unique heading.

To customize the output of each file to include alterations developed in the previous step (such as patching the footnotes & using a custom template), the expand_toc script has a --filter option that should point to a bash script that receives the input filename as the first parameter and which should output to *stdout*.

Finally, expand-toc.py has a --section-pages option that outputs separate pages for each section header in the table of contents.

Open the file essay.sh, it should contain the following:
```bash
#!/bin/bash

pandoc \
    --to markdown \
    --template essay-template-02.md \
    --no-wrap \
    --base-header-level 2 \
    --id-prefix=$1- \
    $1
```

Make sure to make this script is executable:
```bash
chmod +x essay.sh
```

Now you can use the expand_toc script to create the compiled reader.md document:
```bash
scripts/expand_toc.py toc.md --filter ./essay.sh --section-pages > reader.md
```

And convert this into an EPUB:
```bash
pandoc --self-contained --epub-chapter-level=2 --toc-depth=2 -o reader.epub reader.md
```

## Installing make

The GNU *make* utility is a program that can help orchestrate your build scripts. See the [related blog post on how make has been used in the INC subgroup](http://digitalpublishingtoolkit.org/2014/10/make-book/).

Mac: One way to install make is to install Apple's XCode development tools. This is either available on your Mac's original system discs, via the Apple App store, or via the Apple developers website. On recent systems, you can simply open the Terminal (in Applications/Utilities) and type:

```bash
make
```

A message should then tell you how to install the program. If make is correctly installed you will see the message:

```bash
make: *** No targets specified and no makefile found.  Stop.
```

Ubuntu:

You may need to install the "build-essentials" package:

```bash
sudo apt-get install build-essentials
```

Debian:

Make is likely already installed, try running it from the commandline.

## Create a makefile

A *Makefile* can be seen as a kind of [executable notebook](http://zgp.org/static/scale12x/) that helps organize ad hoc build scripts into a format that understands how the pieces fit together as *targets* and *dependencies*.

Open the file *makefile*, it contains the following:

```makefile
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
```

*Devlish detail*: The indented lines of a makefile *must* use the tab character (and not spaces). In SublimeText, you can select text to "show invisibles". You should see the long unbroken dash of a tab character before each command. Be careful when cutting and pasting code into a makefile that no spaces get introduced or make will starting inexplicably complaining.

Note how the two command lines from the build02.sh script have been turned into rules of the form:

```makefile
target: dependencies ...
    command(s) to build the target
```

To use the makefile, simple type:

```bash
make
```

To trigger the build process. By default the all script will build creating first the reader.md, and then reader.epub.

In the first line, the expand_toc.py script's --list option is used to produce the list of markdown sources in a format (one file per line) that is usable in the makefile. These sources are listed as a dependency to *reader.md*. If you alter one of the linked to markdown sources, *make* will know that it needs to rebuild first *reader.md* and then *reader.epub*. If you subsequently alter just the *styles.css* file, however, only the final step will be repeated to update *reader.epub*.


## Add EPUB trailers as a target to the makefile

A major benefit to using a makefile is the ability to produce a number of different outputs by creating multiple "targets" and rules based on the same sources. In this case we use the [epubtrailer script](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/) to take the epub resulting from pandoc, and create a GIF-format book trailer.

To use the epubtrailer.py script, you will need the Python Image Library, as well as the images2gif python library. If you have installed the python package manager *pip*, you can install both with the command:

    sudo pip install PIL images2gif

Now add the following lines to the end of your makefile:

```makefile
reader-trailer.gif: reader.epub
    scripts/epubtrailer.py \
        --width 320 \
        --height 240 \
        -o reader-trailer.gif \
        reader.epub
```

As mentioned above (see *devlish detail*), make sure that you put an actual single tab character before "scripts/epubtrailer.py" (cutting and pasting from the web version will be using spaces!). Now type:

```bash
make reader-trailer.gif
```


[INC]: http://networkcultures.org
[pandoc]: http://johnmacfarlane.net/pandoc/
[markdown]: http://daringfireball.net/projects/markdown/