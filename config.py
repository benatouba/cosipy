"""
 This is the COSIPY configuration (init) file.
 Please make your changes here.
"""

## Simulation period
time_start = '2018-06-01T10:00'
time_end   = '2018-06-05T10:00'                                       

## Input/Output files 
input_netcdf= './data/input/input_hintereisferner.nc'
output_netcdf = './data/output/output_hintereisferner.nc'
restart_netcdf = './data/restart/restart.nc'

## Time step in the input files [s]
dt = 3600                                           # 3600, 7200, 10800 [s] length of time step per iteration in seconds

## Debug level
debug_level = 0                                     # DEBUG levels: 0, 10, 20, 30

## Merging level
merging_level = 1                                   # Merge layers with similar properties:
                                                    # 0 = False
                                                    # 1 = <5. [kg m^-3] and <0.05 [K]
                                                    # 2 = <10. and <0.1

## Minimum height of layer [m]
merge_snow_threshold = 0.01    

## Max. number of layers, just for the restart file
max_layers = 100

## Lower boundary condition (temperature [K])
temperature_bottom = 272                     

## CFL criteria
c_stab = 0.9                                        

## Parallel
restart = False 
