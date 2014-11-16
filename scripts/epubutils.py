import zipfile, argparse, os


if __name__== "__main__":
    parser = argparse.ArgumentParser(description='EPUB utilites')
    parser.add_argument('command', help='command')
    parser.add_argument('epub', help='epub file')
    # parser.add_argument('-o', '--output', help='output file')
    parser.add_argument('-o', '--output', help='output file')
    # parser.add_argument('--width', type=int, default=720, help='Width (default: 720)')
    # parser.add_argument('--height', type=int, default=576, help='Width (default: 576)')
    # parser.add_argument('--duration', type=float, default=0.25, help='Base slide duration (Default: 0.25 secs)')
    parser.add_argument('-i', '--input', help='input file')
    args = parser.parse_args()

    if args.command == "open":
        with zipfile.ZipFile(args.epub, "r") as z:
            output = args.output
            if output == None:
                if "." in args.epub:
                    output = args.epub.split(".", 1)[0]
                else:
                    output = "out"
            try:
                os.mkdir(output)
            except OSError, e:
                print "warning", e
                pass
            z.extractall(output)

    elif args.command == "list":
        with zipfile.ZipFile(args.epub, "r") as z:
            for i in z.infolist():
                print i.filename, i.compress_type


    elif args.command == "zip":
        # Create a new epub (args.epub) using the contents of the args.input directory
        # args.input must contain an open epub, and args.epub must not already exist
        #
        contents = []
        for base, dirs, files in os.walk(args.input):
            for f in files:
                path = os.path.join(base, f)
                rpath = os.path.relpath(path, args.input)
                contents.append(rpath)
        contents.sort()
        contents.remove("mimetype")
        if os.path.exists(args.epub):
            raise Exception("EPUB already exists")
        with zipfile.ZipFile(args.epub, "w") as zout:
            zout.write(os.path.join(args.input, "mimetype"), "mimetype", zipfile.ZIP_STORED)
            for c in contents:
                zout.write(os.path.join(args.input, c), c, zipfile.ZIP_DEFLATED)
