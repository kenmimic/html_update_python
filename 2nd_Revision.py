import re,os,sys,datetime,time

if sys.argv[1:]: 
  folder = sys.argv[1] # recursive
else:
  folder = "./" # if Not specify folder,set current

def ListHTMLfiles():
   files = []
   for r, d, f in os.walk(sys.argv[1]):  # r=root, d=dirs, f=files
       for file in f:
          if '.html' in file:
             files.append(os.path.join(r, file))
             files.sort(reverse=False)
#   print files
   return files

def UpdateHTML(LN, old, new):
  for f in ListHTMLfiles()[0:]:
    with open(f,'r') as html:
      contents = html.readlines()
      contents[LN] = re.sub(old, new, contents[LN])
    with open(f,'wt') as html:
      for line in contents:
        html.write(line)
    html.close()


if __name__=="__main__":

  LN=87 # Line Number 
  old="><"
  new=">1.1<"
  UpdateHTML(int(LN-1),old, new)
  print("sed '%ss/%s/%s/'") %(LN,old,new)

  LN=88 # Line Number 
  old="><"
  new=">%s<" %(datetime.datetime.today().strftime("%c"))
  UpdateHTML(int(LN-1),old, new)
  print("sed '%ss/%s/%s/'") %(LN,old,new)

  LN=89 # Line Number 
  old="><"
  new=">Kenny Chang<"
  UpdateHTML(int(LN-1),old, new)
  print("sed '%ss/%s/%s/'") %(LN,old,new)

  LN=90 # Line Number 
  old="><"
  new=">2nd Draft<"
  UpdateHTML(int(LN-1),old, new)
  print("sed '%ss/%s/%s/'") %(LN,old,new)
  time.sleep(1)

print "Total processed %s files" %len(ListHTMLfiles()[0:])

