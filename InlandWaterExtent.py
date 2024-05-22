#import the required library
import ee
import geemap
import matplotlib.pyplot as plt
import pandas as pd
import json

#initialise the Geemap
geemap.ee_initialize()

#create a map object
m = geemap.Map(center=[20,0],zoom=2)

#create a function that extracts the Inland Water Extent by 
#data from Google Earth Engine

def geometry_geoJson(file_path):
  with open(file_path) as f:
      json_data = json.load(f)
  moi =  geemap.geojson_to_ee(json_data)
  return moi


def inland_water_extent(startDate, endDate, roi):
    start = startDate
    end = endDate
    waterMonthly = ee.ImageCollection("JRC/GSW1_4/MonthlyHistory").filterDate(start, end)

    def func_nbk(i):
        return i.eq(2).updateMask(i.gt(0)).copyProperties(i, ['system:time_start'])

    waterMonthlyMask = waterMonthly.map(func_nbk)
    waterOccurrence = waterMonthlyMask.mean().clip(roi)

    # Add visualization to map (assuming you have a geemap.Map instance `m`)
    m.addLayer(waterOccurrence, {'min': 0, 'max': 1, 'palette': ['white', 'blue']}, 'Water Occurrence')
    m.centerObject(roi, 9)

    extend = []
    def cal_area(fea):
        area = ee.Image.pixelArea().updateMask(fea).reduceRegion(
             reducer=ee.Reducer.sum(), geometry=roi, scale=30,bestEffort=True,).get('area')
        kmarea = ee.Number(area).divide(1e6)
        extend.append({'m2': ee.Number(area), 'km2': ee.Number(kmarea), 'time': fea.get('system:time_start')})
        return fea.set({'m2': area, 'km2': kmarea})

    data = waterMonthlyMask.map(cal_area)

    data_list = data.getInfo()['features']
    area_list = [{'m2': f['properties']['m2'], 'km2': f['properties']['km2'], 'time': f['properties']['system:time_start']} for f in data_list]

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(area_list,index=[x for x in range(1,len(area_list)+1)])

    # Convert the 'time' column to datetime
    df['time'] = pd.to_datetime(df['time'], unit='ms')

    # Sort the DataFrame by time
    df = df.sort_values(by='time')

    # Display the Table
    print(df)
    print('\n')

    #save the Table
    df.to_csv('SurfaceWaterExtent.csv')

    # Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['km2'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Area (km²)')
    plt.title('Surface Water Extent Time Series')
    #save the plot
    plt.savefig("SurfaceWaterExtent.jpg")
    plt.grid(True)
    plt.show()


#how to call the the function
roi = geometry_geoJson("/content/IndiraSagar.geojson")

inland_water_extent('2018-01-01','2019-01-01',roi)
