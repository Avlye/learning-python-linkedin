import os
import shutil

from os import path
from shutil import make_archive

filename = "ronaldo.txt"

if path.exists(filename):
    source = path.realpath(filename)
    destiny = source + ".bak"
    shutil.copy(source, destiny)
    shutil.copystat(source, destiny)

    # rename the original file
    # os.rename(filename, "ronaldo.txt")

    # create a zip file
    root_dir, tail = path.split(source)
    shutil.make_archive("archive", "zip")