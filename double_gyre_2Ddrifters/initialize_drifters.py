import xarray as xr
import netCDF4 as nc
import numpy as np

def createParticlesNC(fnam,ids,ines,jnes,lons,lats,levs,days):
    f=nc.Dataset(fnam,'w',format='NETCDF3_64BIT_OFFSET',clobber=True)
    idim=f.createDimension('i',None)
    ivv=f.createVariable('i',np.float64)
    iv=f.createVariable('drifter_num',np.int32,('i',))
    inev=f.createVariable('ine',np.int32,('i',))
    jnev=f.createVariable('jne',np.int32,('i',))
    latv=f.createVariable('lat',np.float64,('i',))
    lonv=f.createVariable('lon',np.float64,('i',))
    levv=f.createVariable('depth',np.float64,('i',))
    dv=f.createVariable('time',np.float64,('i',))

    f.file_format_major_version=1
    f.file_format_minor_version=1
    f.time_axis = 0
    iv.long_name='identification of the drifter'
    iv.units='dimensionless'
    iv.packing=0
    inev.long_name='i index'
    inev.units='none'
    inev.packing=0
    jnev.long_name='j index'
    jnev.units='none'
    jnev.packing=0
    lonv.long_name='longitude'
    lonv.units='degrees_E'
    latv.long_name='latitude'
    latv.units='degrees_N'
    levv.long_name= 'depth below surface'
    levv.units='m'
    dv.units='days since 1900-01-01 00:00:00'
    ivv[:]=len(ids[:])
    iv[:] = ids[:]
    inev[:]=ines[:]
    jnev[:]=jnes[:]
    lonv[:]=lons[:]
    latv[:]=lats[:]
    levv[:]=levs[:]
    dv[:]=days[:]
    f.sync()
    f.close()

lon1D = np.arange(5,15,1)
lat1D = np.arange(-60,5,1)

lonmesh,latmesh = np.meshgrid(lon1D,lat1D)

sizemesh = lonmesh.ravel().size
    
id_list = np.arange(1,sizemesh+1,1).tolist()
ines_list = [0] * sizemesh
jnes_list = [0] * sizemesh
lons_list = lonmesh.ravel().tolist()
lats_list = latmesh.ravel().tolist()
levs_list = [500]* (sizemesh//2) + [1060]* (sizemesh//2)
days_list = [0]* sizemesh

createParticlesNC('drifters.res.nc',ids=id_list,ines=ines_list ,jnes=jnes_list,lons=lons_list,lats=lats_list,levs=levs_list,days=days_list)


