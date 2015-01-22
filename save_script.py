''' This script allows you to copy a .py script to the iOS clipboard and then use Open In...
to have that script saved in Pythonista.  This requires both the Workflow and Pythonista apps
and the workflow at https://workflow.is/workflows/8cdee57f79664205a6a565c9cbdb3d48 '''

import clipboard
import console
import os
import sys

def save(filename, text):
    root, _ = os.path.splitext(filename)
    extension = '.py'
    filename = root + extension
    filenum = 1
    while os.path.isfile(filename):
        filename = '{} {}{}'.format(root, filenum, extension)
        filenum += 1
    #print(finalname)
    with open(filename,'w') as f:
        f.write(text)
    #clipboard.set(filename)
    return filename

def main():
    text = clipboard.get()
    assert text, 'No text on the clipboard!'
    filename = sys.argv[1]
    console.clear()
    print('Wait a Moment Please!')
    filename = save(filename, text)
    console.set_font('Futura', 16)
    print('Done!\nFile Saved as:\n' + filename)

if __name__ == '__main__':
    main()
