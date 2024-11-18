import sys
from os.path import splitext
from PIL import Image,ImageOps

def main():
    
    chek_command_line_arg()
    try:
        image_file = Image.open(sys.argv[1])
    except:
        sys.exit('Input does not exist')
    
    shirt_file = Image.open('shirt.png')
    
    size = shirt_file.size
    
    support = ImageOps.fit(image_file,size)
    support.paste(shirt_file,shirt_file)
    support.save(sys.argv[2])
    
def chek_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit('Invalid input')
    if check_extension(file2[1]) == False:
        sys.exit('Invalid output')
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')
    
def check_extension(file):
    if file in ['.jpg','.jepg','.png']:
        return True
    return False
    
if __name__ == '__main__':
    main()