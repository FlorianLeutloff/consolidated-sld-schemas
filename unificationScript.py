import os
import re


def stripSubFile(sub_file_text):
    #(\<xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) only opening tag
    #(\<)(\/)*(xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) opening and closing tag
    sub_file_text = re.sub("(\<)(\/)*(xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>)", "", sub_file_text)
    sub_file_text = re.sub("(\<\?xml){1}[\s\d\w\=\"\:\\/\.\-]*(\?\>){1}", "", sub_file_text)
    return sub_file_text
    pass

def unifyFiles(root_file_text, sub_file_text):
    root_file_text = root_file_text + "\n" + sub_file_text
    return root_file_text
    pass

def openRootFileTextStructure(root_file_text):
    root_file_text = re.sub("(\<\/)(xsd\:schema)(\>)","",root_file_text)
    return root_file_text
    pass

def closeRootFileTextStructure(root_file_text):
    root_file_text = root_file_text + "</xsd:schema>"
    return root_file_text
    pass


root_path = ""
destination_path = ""

config_structure = {
    "folder":"",
    "root_file_name":"",
    "destination_file_name":"",
    "namespace_prefix": ""
}


config_list = [
    {
        "folder_name":"filter",
        "root_file_name":"filter.xsd",
        "destination_file_name":"ogc.xsd",
        "namespace_prefix": ""
    }
]


for config in config_list:
    folder_path = f"{root_path}/{config.folder_name}"
    root_file_text = ""
    with open(f"{folder_path}/{config.root_file_name}","r") as root_file:
        root_file_text = root_file.read()
        pass
    root_file_text = openRootFileTextStructure(root_file_text)
    folder_tree = os.walk(folder_path)
    for root, dirs, files in folder_tree:
        for file_name in files:
            sub_file_text = ""
            with open(f"{root}/{file_name}","r") as sub_file:
                sub_file_text = sub_file.read()
                pass
            sub_file_text = stripSubFile(sub_file_text)
            root_file_text = unifyFiles(root_file_text, sub_file_text)
            pass
        pass 
    root_file_text = closeRootFileTextStructure(root_file_text)
    os.makedirs(destination_path,exist_ok=True)
    with open(f"{destination_path}/{config.destination_file_name}", "w") as destination_file:
        destination_file.write(root_file_text)
        pass
    pass