from typing import List
from pathlib import Path
import shutil

class Parser:
    
    extensions = [str]
    

    def valid_extensions(extension):
        return extension in self.extensions

    def parse(path:Path,source:Path,dest:Path) -> Path:
        raise NotImplementedError

    def read(path):
        with open(path) as file:
            return read(file)

    def write(path,dest,content,ext =".html"):
        full_path = dest / with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(path,source,dest):
        shutil.copy2(path,dest / source)


    class ResourceParser:

        extensions = [".jpeg",".png",".gif",".css",".html"]

        def parse(path:Path,source:Path,dest:Path) -> Path:
            raise NotImplementedError

        def copy(path,source,dest):
            super.copy()
            

    

    
        
