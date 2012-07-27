import markdown
import re

class PlotPreprocessor(markdown.preprocessors.Preprocessor):

    pattern = re.compile(
        r'>>> (.+)')
    pt1 = re.compile(
        r"savefig\(['\"](.+?)['\"]\)")
    
    def run(self, lines):
        new_lines=[]
        file_name = 'test1.png'
        for line in lines:
            m = self.pattern.match(line)
            if m:
                exec(m.group(1))
                if re.search(self.pt1, line):
                    file_name = re.search(self.pt1, line)
                    new_line = "![alt img]" + '(' + file_name.group(1) + ')'
                    new_lines.append(new_line)
            else:
                new_lines.append(line)
        return new_lines

class Plot(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.add('PlotPreprocessor', PlotPreprocessor(md), '>reference')

def makeExtension(configs=None):
    return Plot(configs=configs)
