import json
import requests
import bs4
import urllib
#r = requests.get("https://ketqua.net")
#r = requests.get("https://ncov.moh.gov.vn/",verify=False)
#s = r.text
#vitri= s.find("Số ca nhiễm")
#s = r.text[vitri-100:vitri+100]
#print(s.split(">")[3].split("<")[0])
#resp = requests.get("https://ketqua.net")
#tree = bs4.BeautifulSoup(markup = resp.text)
#t=tree.find('td',attrs={'id':'rs_0_0'})
#print(t.text)
#--------------------------------------------
#resp = requests.get("https://ncov.moh.gov.vn/",verify=False)    
#tree = bs4.BeautifulSoup(markup=resp.text)
#t= tree.find('span',attrs={'class':'font24'})
#print(t.text)
array = [1, 1, 2, 6, 4, 6, 3, 4]

tatcagiai = []
vitrigiai = [
	'giai dac biet ',
	'giai nhat ',
	'giai nhi','giai nhi',
	'giai ba','giai ba','giai ba','giai ba','giai ba','giai ba',
	'giai tu','giai tu','giai tu','giai tu',
	'giai nam','giai nam','giai nam','giai nam','giai nam','giai nam',
	'giai sau','giai sau','giai sau',
	'giai bay','giai bay','giai bay','giai bay']
r = requests.get("https://ketqua.net")

tree = bs4.BeautifulSoup(markup = r.text)
for i in range(len(array)):
	for sl in range(array[i]):
		tdb    = tree.find('div',attrs={'id' : 'rs_'+str(i)+'_'+str(sl)})
		giaidacbiet = (tdb.text[0:])
		tatcagiai.append(giaidacbiet)
print("Nhap vao so ma ban muon tra ")
s = input()
if (s in tatcagiai):
	index = tatcagiai.index(s)
	
	print('Ban da trung ' + vitrigiai[index] )
else:
   print('Khong trung gi ca con ga nay')

