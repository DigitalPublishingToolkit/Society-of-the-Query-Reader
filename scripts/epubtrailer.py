#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, zipfile, os, shutil, glob, textwrap
from os.path import join
from xml.etree import ElementTree as ET
from PIL import Image, ImageFont, ImageDraw
from images2gif import writeGif

# parameters
speed = 0.2
W = 720
H = 576
titleDuration = 6
epubFont = 1
fontratio = 6
bgColor = (255,255,255)
fontColor = (0,0,0)

# copy file
filename = str(sys.argv[1])
try:
	outfilename = sys.argv[2]
except IndexError:
	outfilename = None

copy = 'new-' + filename 
shutil.copy2(filename, 'new-' + filename)

# rename file with zip extension

if filename.endswith('.epub'):
	os.rename(copy, copy[:-4] + 'zip')
	zipname = copy[:-4] + 'zip'
	print "converted extension for " + str(zipname)
else:
	print "File is not an Epub"
	zipname = filename

# unzip ePub
fh = open(str(zipname), 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "temp"
    z.extract(name, outpath)
fh.close()

# remove copy
os.remove(zipname)

# find content.opf
lookfor = "content.opf"
for root, dirs, files in os.walk('temp'):
    print "searching", root
    if lookfor in files:
    	opfpath = join(root, lookfor)
        print "found: %s" % join(root, lookfor)
        break
        
def innerhtml (tag):
    return (tag.text or '') + ''.join(ET.tostring(e) for e in tag)

t = ET.parse(opfpath)

#Get Title
titletag = t.findall('.//{http://purl.org/dc/elements/1.1/}title')
title = titletag[0].text

# Get Authors
cap = t.findall('.//{http://purl.org/dc/elements/1.1/}creator')
authors = []
for tag in cap:
	inner = innerhtml(tag)
	authors.append(inner)
	
# Get Publisher
pubtag = t.findall('.//{http://purl.org/dc/elements/1.1/}publisher')
publisher = None
if pubtag: 
	publisher = pubtag[0].text

# Get Date
datetag = t.findall('.//{http://purl.org/dc/elements/1.1/}date')
date = None
if datetag: 
	date = datetag[0].text

# Show Metadata
if title:
	print "Title:", title
if authors:
	print "Authors:"
	for n in authors:
		print "  ",n
if publisher:
	print "Publisher:", publisher
if date:
	print "Date:", date


# create new directory
if not os.path.exists('new-pictures'):
    os.makedirs('new-pictures')

# Search for fonts
fonts = []
for root, subdirs, files in os.walk('temp'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.otf', '.ttf'):
             fonts.append(os.path.join(root, file))
if len(fonts) == 0:
	for root, subdirs, files in os.walk('.'):
	    for file in files:
	        if os.path.splitext(file)[1].lower() in ('.otf', '.ttf'):
	             fonts.append(os.path.join(root, file))
	             break
	    if len(fonts) > 0:
	    	break

def _bytes(x, encoding="latin-1"):
	if type(x) == unicode:
		return x.encode(encoding, errors='ignore')
	return x

def screen(text, seq, fontsize, frames):
	for x in range(0, frames):
		seqall = seq + '-' + str(x)
		image = Image.new("RGBA", (W,H), bgColor)
		if fonts:
			if epubFont:
				usr_font = ImageFont.truetype(fonts[0], fontsize)
		else:		
			usr_font = ImageFont.load_default() # ImageFont.truetype("resources/NotCourierSans.otf", fontsize)
		d_usr = ImageDraw.Draw(image)
		# align center
		lines = textwrap.wrap(text, width = 20)
		y_text = (H/2)-100
		for line in lines:
			w, h = d_usr.textsize(_bytes(text), usr_font)
			linebytes = line
			width, height = usr_font.getsize(_bytes(line))
			# d_usr = d_usr.text(((W-w)/2,(H-h)/2), line, fontColor, font=usr_font)
			d_usr.text((100, y_text), _bytes(line), fontColor, font=usr_font)
			y_text += height
		filename = 'new-pictures/' + seqall + '.jpeg'
		image.save(filename, 'jpeg')

# Create Screen for Title
screen(title, '00', int(fontratio * 6), titleDuration)	
# Create Screen for 'by'
screen('A book by', '01', int(fontratio * 2.8), titleDuration)
# Create Screens for Authors
i = 0
for name in authors:
	screen(name, '02-' + str(i), int(fontratio * 4), titleDuration)
	i = i + 1
if pubtag: 
	# Create Screens for "published by"
	screen('Published by', '03', int(fontratio * 2.8), titleDuration)
	# Create Screen for Publisher
	screen(publisher, '04', int(fontratio * 4), titleDuration)	

# Search for pictures
epubImages = []
for root, subdirs, files in os.walk('temp'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
             epubImages.append(os.path.join(root, file))
             
# Convert and resize all Picz to Jpeg
i = 0
for picture in epubImages:
	background = Image.new("RGBA", (W,H), bgColor)
	image = Image.open(picture)
	image.thumbnail((720, 576), Image.NEAREST)
	(w, h) = image.size
	background.paste(image, ((W-w)/2,(H-h)/2))
	pictitle = 'new-pictures/05-respic' + str(i) + '.jpeg'
	background.save(pictitle)
	i = i + 1

# add some black frames
for x in range(0, titleDuration):
	seq = '06-' + str(x)
	image = Image.new("RGBA", (W,H), bgColor)
	filename = 'new-pictures/' + seq + '-black.jpeg'
	image.save(filename, 'jpeg')
	
# create screen for date
if date: 
	screen('In your Public Library since ' + date, '07', int(fontratio * 3), titleDuration)	
	
# add some black frames
for x in range(0, titleDuration):
	seq = '08-' + str(x)
	image = Image.new("RGBA", (W,H), bgColor)
	filename = 'new-pictures/' + seq + '-black.jpeg'
	image.save(filename, 'jpeg')
	
# Make gif!!
images = [Image.open(image) for image in sorted(glob.glob("new-pictures/*.jpeg"))]

if outfilename == None:
	outfilename = 'trailer-' + title + '.gif'

writeGif(outfilename, images, duration=speed)

# Remove folders
shutil.rmtree('temp')
shutil.rmtree('new-pictures')  
 
