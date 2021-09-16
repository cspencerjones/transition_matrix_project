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
    
    
createParticlesNC('drifters.res.nc',ids=[1,2,3],ines=[0,0,0],jnes=[0,0,0],lons=[20.1,20.3,20.6],lats=[44.625,44.375,44.875],levs=[1, 1, 1],days=[0,0,0])


