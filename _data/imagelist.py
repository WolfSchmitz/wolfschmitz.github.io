import os
import glob
import sys
from pathlib import Path

def main(argv):

    if len(argv) < 1 or not Path(argv[0]).is_dir():
        sys.exit(1)
        
    types = ('*.jpg', '*.png')
    
    imagesPath = Path(argv[0])
    
    category = imagesPath.parts[-1]
    
    imageFiles = []
    
    for fileType in types:
        imageFiles.extend(imagesPath.glob(fileType))
    
    imageFiles.sort()
    
    print('images:')
    
    for imageFile in imageFiles:
        print('    -')
        print(f'        url: /{ imageFile.absolute().relative_to(Path.cwd().parent).as_posix() }')
        print(f'        tags: [{category}]')
    
    sys.exit(0)
        

if __name__ == "__main__":
    main(sys.argv[1:])