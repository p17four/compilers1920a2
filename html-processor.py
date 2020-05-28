import re   

#Παρακάτω φτιάχνω μια συνάρτηση για μετατροπής html με τη χρήση της sub.
def func(m): 
  if (m.group(0)=='&amp;'):
      return '&'  

  elif (m.group(0)=='&gt;'):
      return '>'
  
  elif (m.group(0)=='&lt;'):
      return '<'

  else:
      return ' '	

text = open('testpage.txt','r').read() #Ανοιγμα αρχείου testpage και διαβασμα.


p1 = re.compile(r'<title>(.+?)</title>')     # Εξαγωγή και εκτύπωση του τίτλου  <title> και </title>.
m = p1.search(text)
print(m.group(1))

p2 = re.compile(r'<!--.*?-->',re.DOTALL)     # Απαλοιφή των σχολίων μεταξύ <!-- και -->.
text = p2.sub('',text)



p3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)    #Απαλοιφή των <script> και <style> tags με όλο τους το περιεχόμενο.
text = p3.sub('',text)


p4= re.compile(r'<a.*?href="(.+?)">(.*?)</a>',re.DOTALL)     # Εξαγωγή και εκτύπωση του συνδέσμου (ιδιότητα href) από <a> tags και του κειμένου τους.
for m in p4.finditer(text):
	print (m.group(1),m.group(2))


p5= re.compile(r'<[^>]+>',re.DOTALL)		# Απαλοιφή όλων των tags από το κείμενο.
text = p5.sub('',text)


p6 = re.compile(r'&(amp|gt|lt|nbsp);')		# Μετατροπή HTML entities.
text = p6.sub(func,text)


p7 = re.compile(r'\s+')		# Μετατροπή whitespace σε ένα ακριβώς κενό.
text = p7.sub(' ',text)


print(text)		# Εκτύπωση τελικού κειμένου.
