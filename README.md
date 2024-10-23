# Outlier_Moving_Window_Filter
Filters Outlier points on non-stationary timeseries data sets. (Works best on individual points rather than clusters).

Works properly on noisy data with a few outlier points in it. If there are lots of outliers or the data is relativelty constant use a different filter. 

Originally designed to filter 3D Wind Data from a TriSonica Sphere Anemometer flown ontop of a BlackSwift E2 Quadcopter.

The Anemometer measurses wind U, V and W component vectors at 10 Hz. This flown on a UAV results in a noisy, non-stationary dataset. 
The noise in the signal is an important measurment of turbulance and needs to be conserved as much as possible. 
The sensor would occasionally return magnitudes that were clearly too large to be a valid wind reading. Outlier Points. This could be from a communication error. Not certian on the cause. Here is an example: 

<p align="center">
  <img src="https://github.com/user-attachments/assets/68bba358-4580-4734-bad3-4cc4301215c5" width="500" />
</p>


Smoothing algorithms will not work well to filter this data. Common statistical filters like z-scores or IQR filters take away too many data points. So the design of this filter came about. 

This 3-point Moving Window filter looks at points before and after it and decides to remove it if it exceeds a certian user controlled threshold. 

The filter works by first transforming the data into a stationary timeseries by differencing the column of interest. The mean of the resulsting column is a good capture of the variability of the signal, or the noise of the signal or in this case of wind data, it is the time rate of change of sampled wind mangiute at 10 Hz. This mean multipled by a user chosen scale factor defines the threshold for the filtering algorithm.
Reccomened using a scale of **10x-20x** the mean of the diff() column. 

To run: 
```
python3 remove_outliers.py Test_Wind_Data_1.csv

```


Results should look like this: 

<p float="left">
  <img src="https://github.com/user-attachments/assets/42116dc7-683e-402d-bb6e-06b7881be0dd" width="400" />
  <img src="https://github.com/user-attachments/assets/54e06de9-fa45-47ab-8fee-7c46e2b44840" width="400" /> 

</p>

<p float="left">
  <img src="https://github.com/user-attachments/assets/6aa9f33d-633c-4182-ba8b-8483a64c9423" width="400" />
  <img src="https://github.com/user-attachments/assets/a4b650a4-78af-4dcd-92c3-ce801bf2770c" width="400" /> 

</p>
