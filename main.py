from preprocess import *
file_name =  'coordinates.csv'
points = open_points(file_name)

id = "X"
query_point = find_point(points, id)
if(query_point[0]):
    print(query_point[1].name)
else:
    print(query_point[1])

export_as_geojson(file_name)