import yaml
possible = [
        {'Monster': {'name': 'name', 'hp': 'hp', 'ac': 'ac', 'attacks':'attacks'}}
        ]

for classes in possible:
    class classes(yaml.YAMLObject):
        yaml_loader = yaml.SafeLoader
        yaml_tag = u'!%s'%(str((list(classes.keys())[0])))
        def __init__(self, dictionnary):
            for k, v in dictionary.items():
                setattr(self, k, v)
        
        for attributes in classes[(str((list(classes.keys())[0])))]:
            @property
            def get_attributes(self):
                return self._attributes

#class Monster(yaml.YAMLObject):
#    yaml_loader = yaml.SafeLoader
#    yaml_tag = u'!Monster'
#    def __init__(self, name, hp, ac, attacks):
#         self.name = name
#         self.hp = hp
#         self.ac = ac
#         self.attacks = attacks
#    def __repr__(self):
#        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
#            self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)


x=yaml.safe_load("""
--- !Monster
name: Cave spider
hp: [2, 6]
ac: 16
attacks: [BITE, HURT]
""")

print(x.hp())
