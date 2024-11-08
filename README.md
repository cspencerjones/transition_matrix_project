# transition_matrix_project

This project contains very preliminary code for running particles online using MOM6. DO NOT use this code to do real science: it has not been extensively tested. You are welcome to try it and provide feedback. 

To compile the code:
Create the files structure described in the `MOM6-examples` tutorial. 

From your `repro` directory, run
```
make clean 

rm -f path_names

../../../../src/mkmf/bin/list_paths -l ./ ../../../../src/MOM6/{config_src/infra/FMS1,config_src/memory/dynamic_symmetric,config_src/drivers/solo_driver,config_src/external/ODA_hooks,config_src/external/database_comms,config_src/external/GFDL_ocean_BGC,config_src/external/stochastic_physics,src/{*,*/*}}/ ../../../../src/drifters/
../../../../src/mkmf/bin/mkmf -t linux-intel.mk -o '-I../../shared/repro' -p MOM6 -l '-L../../shared/repro -lfms' path_names

make NETCDF=3 TEST=1 MOM6 -j
```

I recommend running the double_gyre test case first. To run with particles you must set `USE_PARTICLES = TRUE` in MOM_OVERRIDE. 

There are two options for initializing particles:
Option 1: Fake a restart file
The file `double_gyre/initialize_drifters.py` will allow you to create a restart file. If you put this restart file in `INPUT` and start the run in restart mode, the particles will automatically be initialized. 

Option 2: Set the parameters
```
generate_days = 0
generate_lons = 0.001,22,0.1
generate_lats = 35.001,39,5
```
inside  &particles_nml. 
