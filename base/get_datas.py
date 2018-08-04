import os
import yaml
def get_datas(file_name):
    file_path="./datas"+os.sep+file_name
    with open(file_path,"r",encoding="utf-8") as f :
        return yaml.load(f)


