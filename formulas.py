def map_splitter(upper_left, upper_right, lower_right):
    x_odd = []  # For the odd row of points for longitude and latitude in x-dimension
    x_even = []  # for the even row of points for longitude and latitude in x-dimension

    current_point_x = upper_left[0]

    # untill the current point is not equal to the right most point
    while current_point_x <= upper_right[0]:
        # we append the current point to odd point list
        x_odd.append(current_point_x)
        # 1.0/111.0 <- this is how to convert long/lat into km and multiplying by because we need 2*radius
        current_point_x += (1.0/111.0*2.0)

    # setting the current point for the even row
    current_point_x = upper_left[0] + (1.0/111.0)

    while current_point_x <= upper_right[0]:
        # doing the same thing here for even row points that we did for odd row points
        x_even.append(current_point_x)
        current_point_x += (1.0/111.0 * 2.0)

    y_odd = []      # For the odd row of points for longitude and latitude in y-dimension
    y_even = []     # For the even row of points for longitude and latitude in y-dimension

    current_point_y = upper_left[1]

    while current_point_y >= lower_right[1]:
        y_odd.append(current_point_y)
        current_point_y -= (1.0/111.0 * 2.0)

    current_point_y = upper_left[1] - (1.0/111.0)

    while current_point_y >= lower_right[1]:
        y_even.append(current_point_y)
        current_point_y -= (1.0/111.0 * 2.0)

    even_point = [[str(i), str(j)] for i in x_even for j in y_even]
    odd_points = [[str(i), str(j)] for i in x_odd for j in y_odd]

    output = even_point + odd_points

    return output


def bing_maps_query(center_point_long, center_point_lat, radius, entity_input, BING_MAPS_KEY, base_url):
    # BING_MAPS_KEY is the API key to help pull data
    import requests

    sq_km = str(radius)
    entity_type = str(entity_input)
    bing_maps_key = BING_MAPS_KEY
    # What do I want out of the API
    query_components = "EntityID, DisplayName, Phone, Latitude, Longitude"

    query = "spatialFilter=nearby(" + center_point_lat + "," + center_point_long + "," + sq_km + ")&$filter=EntityTypeID%20eq%20'" + entity_type + \
            "'&key=" + bing_maps_key + " &$format=json"

    URL = base_url + query

    r = requests.get(URL)
    r.encoding = 'utf-8-sig'
    # results = pd.DataFrame(r.json().get("d").get("results")) # Just save the raw JSONs
    results = r.json()
    return results
