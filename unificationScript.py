import os
import re


def stripSubFile(sub_file_text):
    #(\<xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) only opening tag
    #(\<)(\/)*(xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) opening and closing tag
    sub_file_text = re.sub("(\<)(\/)*(xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>)", "", sub_file_text)
    sub_file_text = re.sub("(\<\?xml){1}[\s\d\w\=\"\:\\/\.\-]*(\?\>){1}", "", sub_file_text)
    sub_file_text = sub_file_text.replace("")
    return sub_file_text
    pass

def unifyFiles(root_file_text, sub_file_text):

    pass


root_path = ""
destination_path = ""

config_structure = {
    "folder":"",
    "root_file":"",
    "destination_file":""
}


config_list = [
    {
        "folder_name":"filter",
        "root_file_name":"filter.xsd",
        "destination_file_name":"ogc.xsd"
    }
]


for config in config_list:
    folder_path = f"{root_path}/{config.folder_name}"
    root_file_text = ""
    with open(f"{folder_path}/{config.root_file_name}","r") as root_file:
        root_file_text = root_file.read()
        pass



    pass