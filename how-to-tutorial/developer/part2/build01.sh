#!/bin/bash

# blank the reader.tmp file
> reader.tmp

# process all the .md files in a loop
# use >> to append each output to reader.md
for i in `ls *.md`
do
pandoc "$i" \
    --to markdown \
    --template essay-template.md \
    --no-wrap \
    --base-header-level 2 \
    --id-prefix="${i}-" \
    >> reader.tmp

# ensure a blank line at the end of each essay
echo >> reader.tmp

done

# Make the EPUB from reader.tmp
pandoc \
    --epub-chapter-level=2 \
    --toc-depth=2 \
    -o reader.epub \
    --from markdown \
    reader.tmp
