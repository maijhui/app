import yaml

class YamlReader():
    def __init__(self,element="URL",
                 yaml_path="C:\\Users\\Administrator\\Desktop\\test.yml",
                 index=0):
        self.element=element
        self.yaml_path = yaml_path
        self.index=index


    def yaml_reader(self):
        with open(self.yaml_path,"rb") as yaml_file:
            datas=list(yaml.safe_load_all(yaml_file))
        return datas[self.index].get(self.element)

if __name__ =="__main__":
    URL=YamlReader().yaml_reader()
    print(URL)

