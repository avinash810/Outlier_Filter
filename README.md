# Outlier_Filter
Filters Outlier points on non-stationary timeseries data sets. (Works best on individual points rather than clusters)

Originally designed to filter 3D Wind Data from a TriSonica Sphere Anemometer flown ontop of a BlackSwift E2 Quadcopter
The Anemometer measurses wind U, V and W component vectors at 10 Hz. This flown on a UAV results in a noisy, non-stationary dataset. 
The noise in the signal is an important measurment of turbulance and needs to be conserved as much as possible. 
The sensor would occasionally return magnitudes that were clearly too large to be a valid wind reading. Outlier Points. This could be from a communication error. Not certian on the cause. 
Smoothing algorithms will not work well to filter this data. Common statistical filters like z-scores or IQR filters take away too many data points. So the design of this filter came about. 

This 3-point Moving Window filter looks at points before and after it and decides to remove it if it exceeds a certian user controlled threshold. 

The filter works by first transforming the data into a stationary timeseries by differencing the column of interest. The mean of the resulsting column is a good capture of the variability of the signal, or the noise of the signal or in my case of wind data, it is the time rate of change of sampled wind mangiute at 10 Hz. This mean multipled by a user chosen scale factor defines the threshold for the filtering algorithm.
Reccomened using a scale of **10x-20x** the mean of the diff() column. 



To run: 
```
python3 outlier.py
```
