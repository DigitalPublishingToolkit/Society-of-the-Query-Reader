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
