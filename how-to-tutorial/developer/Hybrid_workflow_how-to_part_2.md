---
title: "Hybrid workflow how-to: Creating an automated workflow, Part 2"
---

As part of the [INC group][INC], we have been developing a workflow that allows a flexible production of different kinds of electronic outputs like EPUB, PDF, and [book trailers](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/) from collection of essays from the [Society of the Query](http://networkcultures.org/query/).

## Use pandoc to convert multiple markdown source files to an EPUB

When you give pandoc multiple input files, pandoc simply cuts and pastes the different texts together as if they were a single file. While this will sometimes just work, it creates some specific problems for the essays from the Society of the Query:

```bash
pandoc -o reader.epub essays/*.md
```

Produces a lot of warnings:

```bash
pandoc: Duplicate note reference `38' "source" (line 6452, column 1)
pandoc: Duplicate note reference `37' "source" (line 6450, column 1)
pandoc: Duplicate note reference `36' "source" (line 6438, column 1)
```

This is because when treated as a single document, all the footnotes (which use numeric indexes) from the different essays can no longer be differentiated (reference 38 from which essay?).

Besides overlapping footnotes, there may be problems with the hierarchy of the overall document. The individudal essays have been written with their title as level 1, and sections within the essay as level 2. This is fine, but for the final reader we want to introduce higher level sections (at level one) to group the essays. Then the essay levels should shift so that their title is level 2, and essay sections level 3. Luckily pandoc has an option to do just that called --base-header-level that (re)sets the "topmost" level of a document when outputting it.

In general, a useful technique is to use pandoc in two passes, first individually on each essay to adjust it for compilation in the larger document. Each altered essay is then pasted in a new master markdown file containing the entire reader document and it is this file that is converted (again by pandoc) to EPUB.

```bash
pandoc essays/David_Crusoe.md --to markdown --id-prefix=essays/David_Crusoe.md-  --base-header-level 2
```

base header level 2 means that level 1 becomes 2, 2 -> 3 and so on. This adjusts the level to match the "global" document structure (In a sense it pushes the levels +1 deeper).

So the final command for reformatting an essay as a reader section is:

```bash
pandoc essays/David_Crusoe.md --to markdown --template essay-template.md --no-wrap --id-prefix=essays/David_Crusoe.md- --base-header-level 2
```

*Devilish detail*: Note the use of the --no-wrap option. This disables pandoc's automatic text wrapping feature when outputting, in this case, markdown. A subtle bug we discovered was that long titles were being line wrapped which would then break the h2 header in the template (where the $title$ variable is expanded on a line starting with ## so that only the first line was considered part of the header). Thankfully this behaviour can be disabled with --no-wrap.


```bash
cd sotq
> reader.md
for i in `ls *.md`
do
pandoc "$i" --to markdown --template essay-template.md --no-wrap --base-header-level 2 --id-prefix="${i}-" >> reader.md
# important: ensure a blank line at the end of each essay
echo >> reader.md
done
```
And then:

bash
```
pandoc reader.md -o reader.epub
```

Note that it's important to build the epub from the same directory as the markdown source, otherwise any relative links to images would not be found. 

In the resulting epub from above, all the footnotes are merged together in one big end notes section. A useful feature is the --epub-chapter-level option which in addition to splitting the source (back) into separate files (which makes it lighter for an e-reader to load the essays), it puts footnotes back in each individual essay.

bash
```
pandoc reader.md -o reader.epub --epub-chapter-level=1
```

## Using the expand-toc.py script

The trouble with the above is controlling the order of the sections. A simple solution is to build a long bash script that adds each chapter in the right order.

For the INC workflow, we created a custom utility (expand-toc.py) that allows a table of contents file to be used to order the contents of the sections. The script expects a table of contents as input, written in markdown, that contains (markdown formatted) links to the essays. The script then includes the linked to files, in the order they appear. As an additional feature, the table of contents itself can (optionally) be output to allow a custom formated table of contents beyond the automatic table of contents feature of pandoc. NB: The script remaps the links to the first id found in the linked to file, for this reason it's important that the included files begin with a heading.

To customize the output of each chapter to include the tweaks developed above, patching the footnotes & using the custom template, the expand_toc script has a --filter option that should point to a bash script that receives the input filename as the first parameter and should output to stdout.

Create the file essay.sh (in the sotq folder) and write the following:
```bash
#!/bin/bash

pandoc \
    --to markdown \
    --template essay-template.md \
    --no-wrap \
    --base-header-level 2 \
    --id-prefix=$1- \
    $1
```

Make sure to make this script executable:
```bash
chmod +x chapter.sh
```

Now from the sotq folder, you can use the expand_toc script to create the compiled reader.md document:
```bash
../scripts/expand_toc.py toc.md --filter ./essay.sh --section-pages > reader.md
```

And convert this into an EPUB:
```bash
pandoc --self-contained --epub-chapter-level=2 --toc-depth=2 -o reader.epub reader.md
```


## Using a makefile

## Installing make

*make*

Mac: One way to install make is to install Apple's XCode development tools. This is either available on your Mac's original system discs, via the Apple App store, or via the Apple developers website. On recent systems, you can simply open the Terminal (in Applications/Utilities) and type:

```bash
make
```

And a message should tell you how to install the program. If make is correctly installed you will see the message:

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


## Add other kinds of output, like a EPUB trailer, to your makefile

A major benefit to using a makefile is the ability to produce a number of different outputs by creating multiple "targets" and rules based on the same sources. In this case we use the [epubtrailer script](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/) to take the epub resulting from pandoc, and create a GIF-format book trailer.

Download the latest epubtrailer.py from the [code repository](https://github.com/DigitalPublishingToolkit/epubtrailer.py). In addition to the epubtrailer.py script, you will need the Python Image Library, as well as the images2gif python library. If you have installed the python package manager *pip*, you can install both with the command:

    sudo pip install PIL images2gif



[INC]: http://networkcultures.org
[pandoc]: http://johnmacfarlane.net/pandoc/
[markdown]: http://daringfireball.net/projects/markdown/