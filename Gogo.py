import simplejson, urllib

orig_lat = raw_input("Enter the origin latitude\n")
orig_long = raw_input("Enter the origin longitude\n")
dest_lat = raw_input("Enter the desitnation latitude\n")
dest_long = raw_input("Enter the destination longitude\n")
orig_coord = orig_lat+","+orig_long
dest_coord = dest_lat+","+dest_long
url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(orig_coord,dest_coord)
result= simplejson.load(urllib.urlopen(url))
driving_time = result['rows'][0]['elements'][0]['duration']['text']
driving_distance =  result['rows'][0]['elements'][0]['distance']['text']
print driving_time + " " + driving_distance