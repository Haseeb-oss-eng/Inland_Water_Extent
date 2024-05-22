# SurfaceWaterExtent
Create function to extract the Surface Water Extent

## Datasets
For Extracting the Inland Water Extent I have used:
1. **"JRC/GSW1_4/MonthlyHistory" - (1984-03-16-2022-01-01)**

## How to use this Script
**Step 1:** Check the required library has been installed in the IDE,
Google colab or Jupyter Notebook

**Step 2:** Copy & paste the code provided in InlandWaterExtend.py

**Step 3:** There is commented line as Call Function. There are
two functions one is "geometry_geoJson(file_path)" which
returns the geojson to ee object, this is considered as "roi"
will be used as input for function to extract Inland Water Extent 
inland_water_extent(startDate, endDate, roi).

## Output
After running the function 
