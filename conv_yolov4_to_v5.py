import os 
import yaml
from yaml.loader import SafeLoader

yamlfile = open('mydataset.yaml')
data = yaml.load(yamlfile ,Loader = SafeLoader)

os.chdir(os.path.join("test"))

for filename in os.listdir(os.getcwd()):
	if filename.endswith(".txt"):
		myfile = open(filename,"r")
		lines = myfile.readlines()
		newlines = []
		for l in lines:
			splitline = l.split()
			labelname = ' '.join(map(str,splitline[:-4]))
			print(labelname)
			print(data['names'])
			rep = l.replace(labelname,str(data['names'].index(labelname)))
			newlines.append(rep)
		with open(filename,"w") as outfile:
			for l in newlines:
				outfile.write(l)
				outfile.write("\n")
			outfile.close()






	



