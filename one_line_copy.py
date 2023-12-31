import os as os

class one_line_copy:
    filesToCopy = ["a"]
    
    def CopyAndEdit(self):
        content = ""
        for i in self.filesToCopy:
            fileR = open(i, "r", errors='ignore', encoding='utf-8')
            content = fileR.read()
            fileR.close()
            contentT = content.split('\n')
            content = ""
            for j in contentT:
                content+=j
            i = i.split('.')
            i=i[0]+"-copy."+i[-1]
            fileW = open(i, "w", errors='ignore', encoding='utf-8')
            fileW.write(content)
            fileW.close()