import pandas

def dict_create():
    df = pandas.read_excel("Canteen.xlsx", 'Sheet1')
    di = {}
    for i in df.index:
        di[i] = {"Canteen": df["Canteen"][i], "Cuisine": df["Cuisine"][i],
                 "Stall": df["Stall"][i], "Dish" : df["Dish"][i],
                 "Price": df["Price"][i], "Vegetarian": df["Vegetarian"][i],
                 "Halal": df["Halal"][i], "Opening time": df["Opening time"][i],
                 "Closing time": df["Closing time"][i], "Traffic": df["Traffic"][i],
                 "Rating": df["Rating"][i], "Dish type": df["Dish type"][i] }
    return di
