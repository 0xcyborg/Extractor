# 20 November 2022

Keys = (".js", "=")
Name = input("File Name: ")

with open(Name, "r") as File:
	Data = File.readlines()

for Link in Data:
	for Ext in Keys:
		if(Ext in Link):
			with open("Output.txt", "a") as File:
				File.write(Link)