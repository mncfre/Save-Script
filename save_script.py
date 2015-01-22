#this script is intented to be use with worlflow for iOS, the workflow is executed from the Open In... option
#and save .py scripts to Pythonista.
#the workflow link is: https://workflow.is/workflows/8cdee57f79664205a6a565c9cbdb3d48
import sys
import clipboard
import os
import console

def save(name,text):
	filename=name
	extension='py'
	finalname=filename+'.'+extension
	filenum=1
	while os.path.isfile(finalname) is True:
		finalname = filename + ' ({})'.format(str(filenum)) + '.' + extension
		filenum += 1
	
	#print finalname
	f = open(finalname,'wb')
	f.write(text)
	f.close()
	#clipboard.set(finalname)
	return finalname
	
def main():
	console.clear()
	print 'Wait a Moment Please!'
	text=clipboard.get()
	name=sys.argv[1]
	finalname=''
	finalname=save(name,text)
	alert='Done!\nFile Saved as:\n'+finalname
	console.set_font('Futura', 16)
	print alert
	
if __name__ == '__main__':
	main()
