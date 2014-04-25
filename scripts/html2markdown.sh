#!/bin/bash -x

for i in `ls essays/`
do
docbase=essays/$i/index
mv $docbase.html $docbase.calibre.html
echo $docbase.html
pandoc -f html -t markdown $docbase.calibre.html > $docbase.calibre.markdown
python scripts/patchfootnotes.py < $docbase.calibre.markdown > $docbase.markdown
rm $docbase.calibre.markdown
# mv $docbase.markdown.tmp $docbase.markdown
pandoc -f markdown -t html $docbase.markdown --self-contained > $docbase.html
done
