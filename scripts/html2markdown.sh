#!/bin/bash -x

for i
do
base=${i%%.*}
pandoc -f html -t markdown $i > $base.calibre.markdown
python scripts/patchfootnotes.py < $base.calibre.markdown > $base.markdown
rm $base.calibre.markdown
mv $i $i.old
pandoc -f markdown -t html $base.markdown --self-contained > $base.html
done
