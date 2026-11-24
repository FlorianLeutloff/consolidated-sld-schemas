import os
import re


def removeImportsIncludes(file_text, namespace_prefix):
    #remove include statements
    file_text = re.sub(f"(\<)({namespace_prefix}include)[\s\d\w\=\"\:\\/\.\-]*(\>)", "", file_text)
    #remove import statements
    file_text = re.sub(f"(\<)({namespace_prefix}import)[\s\d\w\=\"\:\\/\.\-]*(\>)", "", file_text)
    return file_text
    pass

def stripSubFile(sub_file_text, namespace_prefix):
    #(\<xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) only opening tag
    #(\<)(\/)*(xsd\:schema)[\s\d\w\=\"\:\\/\.]*(\>) opening and closing tag
    sub_file_text = re.sub(f"(\<)(\/)*({namespace_prefix}schema)[\s\d\w\=\"\:\\/\.\-]*(\>)", "", sub_file_text)
    sub_file_text = re.sub("(\<\?xml){1}[\s\d\w\=\"\:\\/\.\-]*(\?\>){1}", "", sub_file_text)
    sub_file_text = removeImportsIncludes(sub_file_text, namespace_prefix)
    return sub_file_text
    pass

def unifyFiles(root_file_text, sub_file_text):
    root_file_text = root_file_text + "\n" + sub_file_text
    return root_file_text
    pass

def openRootFileTextStructure(root_file_text, namespace_prefix):
    root_file_text = re.sub(f"(\<\/)({namespace_prefix}schema)(\>)","",root_file_text)
    return root_file_text
    pass

def closeRootFileTextStructure(root_file_text, namespace_prefix):
    if(namespace_prefix.count("\\") > 0):
        namespace_prefix = namespace_prefix.replace("\\","")
        pass
    root_file_text = root_file_text + f"</{namespace_prefix}schema>"
    return root_file_text
    pass


root_path = "formatting_errors/processed"
destination_path = "formatting_errors/unified"

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
        "namespace_prefix": "xsd\:"
    },
    {
        "folder_name":"gml",
        "root_file_name":"gml.xsd",
        "destination_file_name":"gml.xsd",
        "namespace_prefix": ""
    },
    {
        "folder_name":"ows",
        "root_file_name":"owsAll.xsd",
        "destination_file_name":"ows.xsd",
        "namespace_prefix": ""
    },
    {
        "folder_name":"se",
        "root_file_name":"FeatureStyle.xsd",
        "destination_file_name":"se.xsd",
        "namespace_prefix": "xsd\:"
    },
    {
        "folder_name":"sld",
        "root_file_name":"StyledLayerDescriptor.xsd",
        "destination_file_name":"sld.xsd",
        "namespace_prefix": "xsd\:"
    },
    {
        "folder_name":"smil",
        "root_file_name":"smil20.xsd",
        "destination_file_name":"smil.xsd",
        "namespace_prefix": ""
    },
    {
        "folder_name":"wfs",
        "root_file_name":"wfs.xsd",
        "destination_file_name":"wfs.xsd",
        "namespace_prefix": "xsd\:"
    },
    {
        "folder_name":"xlink",
        "root_file_name":"xlinks.xsd",
        "destination_file_name":"xlink.xsd",
        "namespace_prefix": ""
    }    
]


for config in config_list:
    print(config)
    folder_path = f"{root_path}/{config["folder_name"]}"
    root_file_text = ""
    with open(f"{folder_path}/{config["root_file_name"]}","r") as root_file:
        root_file_text = root_file.read()
        pass
    root_file_text = removeImportsIncludes(root_file_text, config["namespace_prefix"])
    root_file_text = openRootFileTextStructure(root_file_text, config["namespace_prefix"])
    folder_tree = os.walk(folder_path)
    for root, dirs, files in folder_tree:
        for file_name in files:
            if(file_name != config["root_file_name"]):
                sub_file_text = ""
                with open(f"{root}/{file_name}","r") as sub_file:
                    sub_file_text = sub_file.read()
                    pass
                sub_file_text = stripSubFile(sub_file_text, config["namespace_prefix"])
                root_file_text = unifyFiles(root_file_text, sub_file_text)
                pass
            pass
        pass 
    root_file_text = closeRootFileTextStructure(root_file_text, config["namespace_prefix"])
    root_file_text = re.sub("((\s)*(\n)){2,}","\n",root_file_text)
    os.makedirs(destination_path,exist_ok=True)
    with open(f"{destination_path}/{config["destination_file_name"]}", "w") as destination_file:
        destination_file.write(root_file_text)
        pass
    pass