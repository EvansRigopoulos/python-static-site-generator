from pathlib import Path

class Site:
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)
        
    def create_dir(self,path):
        directory = self.dest / relative_to(self.source)
        mkdir(directory,parents=True,exist_ok=True)
        
    def build(self):
        mkdir(self.dest,parents=True,exist_ok=True)
        
        for path in self.source.rglob("*"):
            if path :
                create_dir(path)
            elif path is file:
                run_parser(path)
                
    def load_parser(self,extension):
        for parser in self.parsers:
            if valid_extension(extensions):
                return parser

    def run_parser(self,path):
        parser = load_parser(path.suffix)

        if parser is not None:
            parser.parse(path,self.source,self.dest)
        else:
            print("Not Implemented")
            



