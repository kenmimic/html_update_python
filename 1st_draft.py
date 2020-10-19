import os,sys,subprocess,argparse,string,glob,datetime,time,re
#import bs4

if sys.argv[1:]:
  folder = sys.argv[1] # recursive
else:
  folder = "./" # if not specify, set current 

#contain = []

def ListHTMLfiles():
   files = []
   for r, d, f in os.walk(sys.argv[1]):  # r=root, d=dirs, f=files
       for file in f:
          if '.html' in file:
             files.append(os.path.join(r, file))
             files.sort(reverse=False)
#   print files
   return files

def ReplaceString(old,new):
  for f in ListHTMLfiles()[0:]:
    with open(f,'r') as html:
       contents = html.readlines()
    with open(f,'wt') as html:
       for line in contents:
         html.write(re.sub(old, new, line))
    html.close()

def UpdateHTML(LN, old, new):
  for f in ListHTMLfiles()[0:]:
    with open(f,'r') as html:
      contents = html.readlines()
      contents[LN] = re.sub(old, new, contents[LN])
    with open(f,'wt') as html:
      for line in contents:
        html.write(line)
    html.close()

def UpdateNumbers(LNPass, LNFail, LNReFe):
  for f in ListHTMLfiles()[0:]:
    with open(f,'r') as html:
      contents = html.readlines()
      OldPass = re.findall(r'\d+',contents[LNPass]) 
      OldFail = re.findall(r'\d+',contents[LNFail]) 
      OldReFe = re.findall(r'\d+',contents[LNReFe]) 
      Adj = int(OldFail[0]) + int(OldReFe[0])
      NewPass = int(OldPass[0]) + int(Adj)
      NewFail = 0
      NewReFe = 0
      print ("%s + %s + %s = %s, %s") %(OldPass[0],OldFail[0],OldReFe[0],str(NewPass),f)
      contents[LNPass] = re.sub(OldPass[0], str(NewPass), contents[LNPass])
      contents[LNFail] = re.sub(OldFail[0], str(NewFail), contents[LNFail])
      contents[LNReFe] = re.sub(OldReFe[0], str(NewReFe), contents[LNReFe])
    with open(f,'wt') as html:
      for line in contents:
        html.write(line)
      html.close()

#GetDate()

if __name__=="__main__":

  old="status_failed"
  new="status_passed"
  ReplaceString(old, new)
  print("sed 's/%s/%s/g") %(old,new)
  time.sleep(1)

  old="feedback required"
  new="status passed"
  ReplaceString(old, new)
  print("sed 's/%s/%s/g") %(old,new)
  time.sleep(1)

  LN=30 # Line Number 
  old="Prepared by"
  new="Prepared by Kenny Chang"
  UpdateHTML(int(LN-1),old, new)
  print("sed '%ss/%s/%s/'") %(LN,old,new)
  time.sleep(1)

  for LN in (51,55,83): 
  #LN=55 # Line Number 
    old="><"
    new=">Kenny Chang<"
    UpdateHTML(int(LN-1),old, new)
    print("sed '%ss/%s/%s/'") %(LN,old,new)
    time.sleep(1)

  for LN in (59,63): 
  #LN=55 # Line Number 
    old="><"
    new=">Phong Son<"
    UpdateHTML(int(LN-1),old, new)
    print("sed '%ss/%s/%s/'") %(LN,old,new)
    time.sleep(1)

  LNPass=126
  LNFail=127
  LNReFe=129
  print("Updating Summary, Pass, Fail, Require Feedback")
  UpdateNumbers(int(LNPass-1),int(LNFail-1),int(LNReFe-1))
  time.sleep(1)

  LN=82
  old="<span class=\"date\"></span>"
  new= datetime.datetime.today().strftime("%c")
  print new
  UpdateHTML(int(LN-1), old, new)
  print("Updating Date")
  time.sleep(1)

  print "Total processed %s files" %len(ListHTMLfiles()[0:])
