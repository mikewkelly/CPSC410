'''
Created on 21.10.2013

@author: Chris
'''

import xml.etree.cElementTree as Tree
import xml.dom.minidom as minidom
import os
from ModuleParser import ModuleParser

root = Tree.Element("CodeBase")


''' write moduleName  to xml file, open filePath and parse module '''
def crawlModule(filePath, moduleName, xmlParent):
    module = Tree.SubElement(xmlParent, "Module", {'name' : moduleName})
    parser = ModuleParser(module, filePath)
    parser.parseCode()
    


''' write packageName to xml file, crawl dirPath, for every file call crawlModule() '''    
def crawlPackage(dirPath, packageName):
    package = Tree.SubElement(root, "Package", {'name' : packageName})
    for path, _, files in os.walk(dirPath):
        for f in files:
            if path == dirPath:
                crawlModule(os.path.join(dirPath, f), f, package)
        


''' open xml file, open code directory, for every package call crawlPackage() '''             
def directoryCrawl(argv):
    
    for path, dirs, _ in os.walk(argv):
        for d in dirs:
            crawlPackage(os.path.join(path, d), d)
            
    xmlName = argv + ".xml"
    xmlstring = minidom.parseString(Tree.tostring(root)).toprettyxml();
    f = open(xmlName, 'w')
    f.write(xmlstring)
    f.close()
    return xmlstring
    
''' if __name__ == '__main__':
    directoryCrawl(sys.argv[1])'''
    
#directoryCrawl('pyntaCode')