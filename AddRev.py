# add revision on reports 

import os,sys,subprocess,argparse,string,glob,datetime,time
#import bs4

def GetDate():
   date=os.system("date")
   return date

def ListHTMLfiles():
   files=[]
   for r, d, f in os.walk(sys.argv[1]):  # r=root, d=dirs, f=files
       for file in f:
	  if '.html' in file:
	     files.append(os.path.join(r, file)) 
	     files.sort(reverse=False)
   return files

def ListHtmlFiles():
   files = [ f for f in glob.glob(sys.argv[1] + "**/*.html") ]
   for f in files:
	print f

def AddRevision():
    now = datetime.datetime.today().strftime("%c") #timestamp with date() format
    wrapper = """\t\t\t\t\t\t\t<tr>
\t\t\t\t\t\t\t    <td>2.0</td>
\t\t\t\t\t\t\t    <td>%s</td>
\t\t\t\t\t\t\t    <td>Kenny Chang</td>
\t\t\t\t\t\t\t    <td>Final</td>
\t\t\t\t\t\t\t</tr>
"""
    whole =wrapper % (now)
    for i in ListHTMLfiles()[0:]:  #sorted file 1 
	print "current processing file %s" %i
	with open(i,'r') as html:
	   contents = html.readlines() # read file contents
	   html.close()
	   contents.insert(91,whole) #insert whole at line 91
	with open(i,'w') as html:
	   contents = "".join(contents) #update contents
	   html.write(contents) # write to html
	   html.close()

	with open(i,'r') as html:
	   for line in html.readlines(0)[91:97]: # print line 91-97
	   	sys.stdout.write(line.strip('\t'))
		#sys.stdout.flush
	   html.close()
        time.sleep(1)  #pause 1s for next file
    print "Total processed %s files" %len(ListHTMLfiles()[0:])
GetDate()
#ListHTMLfiles()
#ListHtmlFiles()
AddRevision()
