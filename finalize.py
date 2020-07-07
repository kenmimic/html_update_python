import re,os,sys,datetime,time

if sys.argv[1:]: 
  folder = sys.argv[1] # recursive
else:
  folder = "./" # if Not specify folder,set current

files=[]
Contain=[]

def ListFiles():
  for r, d, f in os.walk(folder):
    for file in f:
      if 'html' in file:
        files.append(os.path.join(r, file))
	files.sort(reverse=False)
  #print files
  return files

def FindingString():
  old = "Version 1.0"
  for f in ListFiles()[0:]:
    with open(f,'r') as html:
      for line in html.readlines():
        found = re.search(r'(.+)'+old+'(.+)',line)
        if found:
          Contain.append(found.group(0)) 
          print found.group(0)
        
  print "Total processed %s files" %len(Contain)

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
    for i in ListFiles()[0:]:  #sorted file 1 
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
    print "Total processed %s files" %len(files)


def ReplaceString():
  old = "Version 1.0"
  new = "Version 2.0"
  for f in files:
    with open(f, 'r') as html:
      contents = html.readlines()
      # Line 47, hard coded 2.0 ( not great )
      contents[46] = "\t\t\t\t\t\t\t\t<td>2.0</td>\n"
    with open(f, 'wt') as html:
      for line in contents:
         html.write(re.sub(old, new, line))
      #print contents[46]

    #Contain.append(ListFiles()[0:]) 
    html.close()     
  print "Total processed %s files" %len(files)

#ListFiles()
#FindingString()
AddRevision()
ReplaceString()
