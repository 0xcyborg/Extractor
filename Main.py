# 20 November 2022

Keys = (".js", "=")
Name = input("File Name: ")

with open(Name, "r") as File:
	Data = File.readlines()

for Link in Data:
	for Key in Keys:
		if(Key in Link):
			with open("Output.txt", "a") as File:
				File.write(Link)
