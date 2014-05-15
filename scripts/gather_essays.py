import os, re, shutil

for (base, _, files) in os.walk("essays",):
    for f in files:
        if f.endswith(".markdown"):
            fp = os.path.join(base, f)
            _, np = os.path.split(base)
            np = re.sub(r"_def$", "", np)
            np = os.path.join("essays", np+".markdown")
            # print fp, "=>", np
            # shutil.copy(fp, np)
            cmd = 'git mv "{0}" "{1}"'.format(fp, np)
            print cmd
            os.system(cmd)
