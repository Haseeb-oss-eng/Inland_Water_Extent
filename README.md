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
"inland_water_extent(startDate, endDate, roi, filename)".

## Explanation
**1. geometry_geoJson(file_path)**:
  This function returns the GeoJSON into ee object.
  **file_path: Input the file of Geojson**

**2.inland_water_extent(startDate, endDate, roi, filename)**:
  This function returns Inland Water Extent Timeseries of given 
  Inland Water Body GeoJSON file.
  **startDate: Enter the Start Date range in string format. (ex:'1984-03-16')**
  **endDate: Enter the End Date range in string format. (ex:'2022-01-01')**
   **roi: Input the output file from geometry_geoJson(file_path) function.**
   **filename: Give the name(user-defined) for naming output file for graph in jpg and Table in csv (ex:LakeMalawai.jpg,LakeMalawi.csv).**
  
## Output
After running the function in Jupyter Notebook and Google Colab
Timeseries and Table displays
then in new code editor enter **"m"** a map displays with Water Body of given
GeoJSON.

## References

