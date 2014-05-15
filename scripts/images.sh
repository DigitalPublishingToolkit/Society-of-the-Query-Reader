# images
rename "s/ /-/g" *
for i in *.tif; do base=${i%%.*}; convert -resize 640x $i $base.png; done

