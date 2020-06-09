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
