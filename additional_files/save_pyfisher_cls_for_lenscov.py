import pyfisher
import os
import numpy as np

def save_cls_for_lenscov(output_name,root_name='lowAcc_lensed',accurate=False,lmax=15000):
    fids=pyfisher.get_fiducials(root_name=root_name) #need root_name only for fids
    pparams=dict(fids)
    print('calculating theory...',root_name)
    pyfisher.get_cls(params=pparams,lmax=lmax,accurate=accurate,
                              engine='camb',de='ppf',nonlinear=True,save_raw_camb_output=root_name+'_raw')
    
    print('done, loading and reformatting...')
    total_cls=np.loadtxt(root_name+'_raw'+'_total').T
    lenspot_cls=np.loadtxt(root_name+'_raw'+'_lens_potential').T
    unlensed_cls=np.loadtxt(root_name+'_raw'+'_unlensed_total').T
    
    lmax=len(total_cls[0])
    ells=np.arange(0,lmax)
    unlensed_output=[ells.copy()]
    lensed_output=[ells.copy()]

    for i,spec in enumerate('TT EE BB TE'.split()): 
        lensed_output.append(total_cls[i]*ells*(ells+1)/2/np.pi)
        unlensed_output.append(unlensed_cls[i]*ells*(ells+1)/2/np.pi)
        
    unlensed_output.append(lenspot_cls[0]*(ells*(ells+1))**2/2/np.pi) #pp
    for i,spec in enumerate('pT pE'.split()): #not sure if these are used in lenscov
        unlensed_output.append(lenspot_cls[i+1]*(ells*(ells+1))**2/2/np.pi /ells)

    
    lensed_output=np.nan_to_num(np.array(lensed_output))
    unlensed_output=np.nan_to_num(np.array(unlensed_output))
    
    lensed_output=np.delete(lensed_output,0,1)
    unlensed_output=np.delete(unlensed_output,0,1)
    
    lensed_output=np.delete(lensed_output,0,1)
    unlensed_output=np.delete(unlensed_output,0,1)
    
    np.savetxt(output_name+'_lensedCls.dat',lensed_output.T, fmt='%i %10.5e %10.5e %10.5e %10.5e')
    np.savetxt(output_name+'_lenspotentialCls.dat',unlensed_output.T, fmt='%i %10.5e %10.5e %10.5e %10.5e %10.5e %10.5e %10.5e')
    
    print('done, removing files...')
    os.remove(root_name+'_raw'+'_total')
    os.remove(root_name+'_raw'+'_lens_potential')
    os.remove(root_name+'_raw'+'_unlensed_total')
    
    print('done')
    
    
if __name__=='__main__':
    save_cls_for_lenscov('Bmodes_params_lowAcc',root_name='lowAcc_lensed',accurate=False, lmax=15000)