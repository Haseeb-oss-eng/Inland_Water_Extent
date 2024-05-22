# Surface Water Extent
Create function to extract the Surface Water Extent

## Datasets
For Extracting the Inland Water Extent I have used:
1. **"JRC/GSW1_4/MonthlyHistory" - (1984-03-16-2022-01-01)**

## How to use this Script
**Step 1:** Ensure the required libraries are installed in your IDE, Google Colab, or Jupyter Notebook.

**Step 2:** Copy and paste the provided code into your Python environment (Source Code: SurfaceWaterExtend.ipynb).

**Step 3:** There is commented line as Call Function. There are
two functions: 
  1. geometry_geoJson(file_path): Converts a GeoJSON file to an Earth Engine (ee) object.
  2. inland_water_extent(startDate, endDate, roi, filename): Extracts the surface water extent timeseries for the specified region and time period, and saves the results as a CSV file and a plot as a JPG file.

## Explanation
**1. geometry_geoJson(file_path)**:
  This function returns the GeoJSON into ee object.
  
    file_path: Input the file of Geojson

**2. inland_water_extent(startDate, endDate, roi, filename)**:
  This function returns Inland Water Extent Timeseries of given 
  Inland Water Body GeoJSON file.
  
    startDate : Enter the Start Date range in string format. (ex:'1984-03-16')
  
    endDate : Enter the End Date range in string format. (ex:'2022-01-01')
  
     roi : Input the output file from geometry_geoJson(file_path) function.
   
     filename : Give the name(user-defined) for naming output file for graph in jpg and Table in csv (ex:LakeMalawai.jpg,LakeMalawi.csv).
   
  
## Output
After running the function in Jupyter Notebook and Google Colab
Timeseries and Table displays then, in new code editor enter 
**"m"** a map displays with Water Body of given GeoJSON.

1. A Timeseries plot will be displayed.
2. The results will be saved as a CSV file and a JPG file

## References

