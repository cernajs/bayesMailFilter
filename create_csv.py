import pathlib
import os
import csv

fieldnames = ['text','spam']

def open_and_read(file):
	f = open(file,"r",encoding='latin1')
	fin = f.read()
	f.close()
	return fin

rows1 = [
	{"text":open_and_read(f),"spam":0} for f in pathlib.Path("./enron2/ham").iterdir()
]

rows2 = [
	{"text":open_and_read(f),"spam":1} for f in pathlib.Path("./enron2/spam").iterdir()
]



with open('file2.csv', 'w', encoding='latin1', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows1)
    writer.writerows(rows2)
"""

def write_to_csv(file_name,*stuff):
	with open(file_name,"w",newline="") as f:
		writer = csv.writer(f)

		writer.writerow(stuff)

write_to_csv("file.csv",*HEADER)


with open("file.csv","w",newline="") as f:
	writer = csv.writer(f)

	writer.writerow(stuff)


for f in pathlib.Path("./enron1/ham").iterdir():
	if f.is_file():
		cur_f = open(f,"r") 
		write_to_csv("file.csv",cur_f,"0")
		cur_f.close()

for f in pathlib.Path("./enron1/spam").iterdir():
	if f.is_file():
		cur_f = open(f,"r") 
		write_to_csv("file.csv",cur_f,"0")
		cur_f.close()
"""