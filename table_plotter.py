####################################################################################################
#                               MODULES
import os
import csv
import random
from matplotlib import pyplot as plt
####################################################################################################
#                               FUNCTIONS
def readTable():
    fileName = "./alltables.csv"
    table = []
    try:
        with open( fileName , newline='' ) as File:  
            reader = csv.reader( File )
            for row in reader:
                table.append( row )
        print("> " + fileName + " read correctly <")
        File.close()
    except FileNotFoundError:
        table = None
        print("<<<Table name " + fileName + " doesn't exist>>>")
        exit()
    return table

def createColorsLines( count ):
    c , l = "" , ""
    cl = []
    colors = ['b','g','r','c','m','y','k']
    lines = ['-','.','-.',':']

    while len(cl) != count+1:
        c = colors[random.randint(0, 6)]
        l = lines[random.randint(0, 3)]
        c += l
        if c in cl:
            pass
        else:
            cl.append(c)
    return cl

def plotCR( table , count , cl ):
    x , y = [] , []
    numb = 0
    for i in range( 1 , len( table ) ):
        x.append( float( table[i][5+count] ) )
    while count != -1:
        for i in range( 1 , len( table ) ):
            if table[i][3+count] == "":
                y.append( None )
            else:
                y.append( float( table[i][3+count] ) )
        plt.subplot( 1 , 2 , 1 )
        plt.plot( x , y , cl[numb] , alpha=0.5 , label=table[0][3+count] )
        plt.legend()
        plt.title('Contact Resistance')
        count-=1
        numb+=1
        y = []

def plotT( table , count , cl ):
    x , y = [] , []
    num = count-1
    numb = 0
    for i in range( 1 , len( table ) ):
        x.append( float( table[i][5+count] ) )
    while count != -1:
        for i in range( 1 , len( table ) ):
            y.append( float( table[i][7+num+1] ) )
        plt.subplot( 1 , 2 , 2 )
        plt.plot( x , y , cl[numb] , alpha=0.5 , label=table[0][3+count] )
        plt.legend()
        plt.title('Temperature')
        count-=1
        num+=1
        numb+=1
        y = []
####################################################################################################
#                                 MAIN
if __name__ == '__main__':
    count = len(os.listdir( "./tables" ))-1
    table = readTable()
    cl = createColorsLines( count )
    plotCR( table , count , cl )
    plotT( table , count , cl )
    plt.show()
####################################################################################################