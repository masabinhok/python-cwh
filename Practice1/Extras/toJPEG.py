# I do not understand the below code, this is just a practice to install external modules through pip and use it in your program.

import os, sys
from PIL import Image 

for infile in sys.argv[1:]:
  f, e = os.path.splitext(infile)
  outfile = f+".jpg"
  if infile !=outfile:
      try:
          with Image.open(infile) as im:
            im.save(outfile)
      except OSError:
          print("cannot convert", infile)