import os
import re


def processFile(text):
    elementList = re.findall("\<[\w\s\d:=\"\/\.]*\>",text)
    for element in elementList:
        fixedElement = element.replace("\n","")
        fixedElement = re.sub("( |$)+"," ",fixedElement)
        text = text.replace(element,fixedElement)
        pass 
    pass
    return text

rootpath = "formatting_errors"

destination = f"{rootpath}/processed"


folder_tree = os.walk(f"{rootpath}/unprocessed");
print(folder_tree)
for root, dirs, files in folder_tree: 
    print(root)
    print(dirs)
    print(files)
    for file in files:
        text = ""
        with open(f"{root}/{file}","r") as xsd_file:
            text = processFile(xsd_file.read())
            print(text)
            pass
        pass

    pass



