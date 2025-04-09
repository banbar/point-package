from preprocess import *
file_name =  'coordinates.csv'

points = open_points(file_name)
# Now data_list contains all your rows (excluding header)
print("Total number of points:", len(points))
print("First point:", points[0])
print("Its coordinates:", (points[0][1], points[0][2]))