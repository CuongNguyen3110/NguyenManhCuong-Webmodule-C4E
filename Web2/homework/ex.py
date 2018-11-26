import mlab
from river import River

mlab.connect()

#ex2
africa_river_list = River.objects(continent__icontains="Africa")
for a in africa_river_list:
    print(a.name)

#ex3
america_river_list = River.objects(continent__icontains="S.America", length__lt=1000)
for a in america_river_list:
    print(a.name)

