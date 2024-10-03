import csv
# paperIDName = "Paper ID"
# paperTitleName = "Paper Title"
# authorNamesName = "Author Names"
# abstractName = "Abstract"
# supplementaryName = "Supplementary"
# notesName = "Notes"
paperIDName = 0# "Paper ID"
paperTitleName = 3# "Paper Title"
authorNamesName = 5# "Author Names"
abstractName = 4# "Abstract"
supplementaryName = -1# "Supplementary"
notesName = 12# "Notes"
cmtName = 2
o = open("rss2024ProgramForGenScript.csv","w")
writer = csv.writer(o)
with open("rss2024Program.csv") as csvfile:
	reader = csv.reader(csvfile)
	sessionName = ""
	header = True
	for row in reader:
		if header:
			header = False
			shortrow = [ c.replace(" ","") for c in row ]
			writer.writerow(shortrow)
			continue
		if row[paperIDName]=="":
			if row[abstractName]!="":
				sessionName = row[abstractName].split(".")[1]
			continue
		# print(row[paperIDName],sessionName,row[notesName])
		row[notesName] = sessionName+";"+row[8].title()+";"+row[9].title() 
		row[cmtName]="{0:03}".format(int(row[paperIDName]))
		print(row[paperIDName],sessionName,row[notesName])
		writer.writerow(row)

o.close()