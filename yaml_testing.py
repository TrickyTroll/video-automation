import yaml
from pathlib import Path

possible = [
        {'Shell': {'command': 'command', 'file_format': 'format', 'file_name': 'name', 'to_read':'to_read'}}
        ]


# Creating a class for each elements in possible.
for classes in possible:
    class classes(yaml.YAMLObject):
        yaml_loader = yaml.SafeLoader
        yaml_tag = u'!%s'%(str((list(classes.keys())[0])))
        def __init__(self, dictionnary):
            for k, v in dictionary.items():
                setattr(self, k, v)
        # Should be setting getters at some point.    

def yaml_getter(filename):
    '''
    This function splits the a YAML file around the lines 
    that contain '---' AND one of the possible classes.
    filename: The name of the YAML file to parse.
    returns: The parsed YAML file.
    '''
    with open(filename, 'r') as stream:
        yaml_file = stream.read()

    parsed = []
    splitted = filter(None, yaml_file.split('--- !'))
    for element in splitted:
        if element.strip != '' or element.strip != ' ':
            parsed.append('--- !' + element)
    return parsed
todo = yaml_getter('yaml_testing.yaml')
print(todo)

def object_creator(parsed_yaml):
    '''
    This function creates objects following instructions in the 
    YAML file. These objects can later be used to create a video.
    parsed_yaml: A list of strings that allow the creation of 
    classes.
    returns: List of objects. Objects possibilities are described 
    in the 'possible' list.
    '''  
    objects = {}
    for i in range(len(parsed_yaml)):
        key_name = 'scene%s'%(i)
        objects[key_name] = yaml.safe_load(parsed_yaml[i])

    return objects

x=object_creator(todo)
print(x)
print(x['scene0'])


        
