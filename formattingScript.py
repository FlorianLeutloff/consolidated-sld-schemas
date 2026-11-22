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

beginning = f"{rootpath}/unprocessed"
destination = f"{rootpath}/processed"


folder_tree = os.walk(beginning);
print(folder_tree)



for root, dirs, files in folder_tree: 
    print(root)
    print(dirs)
    print(files)
    target_stem = root.replace(beginning,destination)
    os.makedirs(target_stem,exist_ok=True)
    for file in files:
        text = ""
        with open(f"{root}/{file}","r") as xsd_file:
            text = processFile(xsd_file.read())
            print(text)
            pass
        target_file_path = f"{target_stem}/{file}"
        print(target_file_path)
        with open(target_file_path,"w") as xsd_file:
            xsd_file.write(text)
            pass
        pass
    pass



