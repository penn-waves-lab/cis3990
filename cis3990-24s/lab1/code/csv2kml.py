import simplekml
import haversine as hs
from haversine import Unit

# create kml object
kml = simplekml.Kml()
# read file
file = "log_GPS.csv"
f = open(file, 'r')

# get
rows = []
for line in f:
        datas = line.split(",")
        row = []
        i = 0
        for data in datas:
            row.append(data)
            i = i + 1
        rows.append(row)

loc1 = (float(rows[0][1]), float(rows[0][2]))
loc2 = (float(rows[-1][1]), float(rows[-1][2]))
#To calculate distance in miles
print(hs.haversine(loc1,loc2,unit=Unit.MILES))

for row in rows:
  kml.newpoint(name=row[0], coords=[(row[2], row[1])])

kml.save('GPS.kml')
