'''
Created on Nov 20, 2013

@author: ericchu
'''
from CodeNeighbourhood.Visualizer.Renderer import Renderer
from CodeNeighbourhood.Visualizer.Renderer import House
from CodeNeighbourhood.Visualizer.Renderer import Window
from CodeNeighbourhood.Visualizer.Renderer import Tent
from CodeNeighbourhood.Visualizer.Renderer import Block
from CodeNeighbourhood.Analyzer.XMLParser import XMLParser
import unittest

''' Unit test class for the package Visualizer ''' 

class TestVisualizer(unittest.TestCase):
    
    ''' constructs necessary objects in preparation for testing Visualizer::Renderer::Renderer;
        takes TestXMLSample.xml as input xml for testing purposes '''
    def setUp(self):
        afile = open("TestXMLSample.xml", "r")
        self.xmlString = "".join(afile.readlines())
        afile.close()
        self.xmlparser = XMLParser(self.xmlString)
        self.xmlPackages = self.xmlparser.getPackages()
        self.renderer = Renderer(self.xmlPackages)
           
    ''' calls Renderer::House constructor and its various getter methods to ensure the house can be properly constructed ''' 
    def testHouseConstructor(self):
        house = House("TheHouseName", 4, 5, (5,3), 7)
        self.failUnless(house.getName() == "TheHouseName")
        self.failUnless(house.getLength() == 4)
        self.failUnless(house.getWidth() == 5)
        self.failUnless(house.getTopLeft() == (5,3))
        self.failUnless(house.getCondition() == 7)
    
    ''' calls Renderer::Window constructor and its various getter methods to ensure windows can be properly constructed ''' 
    def testWindowConstructor(self): 
        window = Window((6,8), 4, 65, (54,84,95))
        self.failUnless(window.getTopLeft() == (6,8))
        self.failUnless(window.getWidth() == 4)
        self.failUnless(window.getHeight() == 65)
        self.failUnless(window.getColour() == (54,84,95))
        
    ''' calls Renderer::Tent constructor and its various getter methods to ensure tents can be properly constructed ''' 
    def testTentConstructor(self):
        tent = Tent((9,4))
        self.failUnless(tent.getTopLeft() == (9,4))

    ''' calls Renderer::Block constructor and its various getter methods to ensure blocks can be properly constructed ''' 
    def testBlockConstructor(self):
        block = Block((9,7), 2, 52, (53,63,12))
        self.failUnless(block.getTopLeft() == (9,7))
        self.failUnless(block.getWidth() == 2)
        self.failUnless(block.getLength() == 52)
        self.failUnless(block.getColour() == (53,63,12))
    
    ''' tests Renderer::calculateTallestWindow to ensure that size of tallest window can be properly derived from XML input
        through parsing and processing ''' 
    def testCalculateTallestWindow(self):
        methods = self.xmlPackages[0].getModules()[1].getClasses()[1].getMethods()
        self.failUnless(self.renderer.calculateTallestWindow(methods) == 87)
      
    ''' tests Renderer::buildWindow to ensure that windows can be built properly provided XML input '''  
    def testBuildWindow(self):
        method = self.xmlPackages[0].getModules()[1].getClasses()[1].getMethods()[3]
        window = self.renderer.buildWindow(method, (58,89), 2, 95)
        self.failUnless(window.getTopLeft() == (0,0))
        self.failUnless(window.getWidth() == 0)
        self.failUnless(window.getHeight() == 9)
        self.failUnless(window.getColour() == (179, 242, 239))
        
    ''' tests Renderer::calculateHouseHeight to ensure that height of houses can be properly calculated properly provided XML input ''' 
    def testCalculateHouseHeight(self):
        aclass0 = self.xmlPackages[0].getModules()[1].getClasses()[0]
        aclass = self.xmlPackages[0].getModules()[1].getClasses()[1]
        self.failUnless(self.renderer.calculateHouseHeight(aclass0) == 31)
        self.failUnless(self.renderer.calculateHouseHeight(aclass) == 117)

    ''' tests Renderer::calculateHouseHeight to ensure that width of houses can be properly calculated properly provided XML input ''' 
    def testCalculateHouseWidth(self):
        aclass0 = self.xmlPackages[0].getModules()[1].getClasses()[0]
        aclass = self.xmlPackages[0].getModules()[1].getClasses()[1]
        self.failUnless(self.renderer.calculateHouseWidth(aclass0) == 30)
        self.failUnless(self.renderer.calculateHouseWidth(aclass) == 134)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()