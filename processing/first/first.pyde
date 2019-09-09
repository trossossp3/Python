places =[]
minX,maxX=0,0
minY,maxY=0,0

def setup():
            size(800,800)
            noLoop()
            readData()
def draw():
    background(255)
    black = color(0)
    for place in places:
        x,y=place
        x=map(x,minX,maxX,0,width)        
        inv_map = {v: k for k, v in my_map.items()}
        y=map(y,minY,maxY,0,width)
        try:
            set(x,y,black)
        except Exception, e:
            print "error drawing place at ({},{}):{}".format(x,y,e)
def readData():
    global minX, maxX, minY, maxY
    lines = loadStrings("http://www.infres.enst.fr/~eagan/class/igr204/data/population.tsv")
    print "loaded",len(lines),"lines"
    for line in lines[2:]:
        columns = line.split()
        longitude = float(columns[1])
        latitude = float(columns[2])
        places.append( (longitude, latitude) )
    minX = min(places, key=lambda place: place[0])[0]
    maxX = max(places, key=lambda place: place[0])[0]
    minY = min(places, key=lambda place: place[1])[1]
    maxY = max(places, key=lambda place: place[1])[1]
