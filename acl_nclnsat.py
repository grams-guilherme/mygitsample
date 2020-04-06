import numpy as np
import matplotlib.pyplot as plt


#read tables with data
#nbc1, ye1, e_cl1, mu_cl_n1                    = np.loadtxt('fort.11', unpack=True)
#nbc2, ye2, e_cl2, mu_cl_n2                    = np.loadtxt('fort.12', unpack=True)
#nbc3, ye3, e_cl,  e_unif_b                    = np.loadtxt('fort.15', unpack=True)
#nbc4, Acl, Zcl,    u                          = np.loadtxt('fort.16', unpack=True)
nbc1, Acl_ncl, Icl_ncl,  ncl_ncl,   ng_ncl,  ye_ncl,  u_ncl, I_unif_ncl, acncl_ncl    = np.loadtxt('var_ncl.dat', unpack=True)
#nbc2, Acl_nsat, Icl_nsat, ncl_nsat, ng_nsat, ye_nsat, u_nsat, I_unif_sat, acncl_nsat, shit  = np.loadtxt('pesado_var.16', unpack=True)
nbc2, Acl_nnsat, Icl_nsat, ncl_nsat, ng_nsat, ye_nsat, u_nsat, I_unif_sat, acncl_nsat, shit  = np.loadtxt('var_eps10menos3.16', unpack=True)

#nbc6, e_unif_cl,  e_coul,  e_surf                        = np.loadtxt('fort.18', unpack=True)
#nbc3, Ecl_ncl,  P_cl_ncl,  mu_cl_n_ncl,   mu_cl_p_ncl             = np.loadtxt('termo_ncl.dat', unpack=True)
#nbc4, Ecl_nsat, P_cl_nsat, mu_cl_n_nsat,  mu_cl_p_nsat          = np.loadtxt('termo_nsat.dat', unpack=True)

#---------------------------------------------------------------------
# 1) plot E/A versus nB
#---------------------------------------------------------------------
#plt.axis([-10, 60, 0, 11])
plt.subplot(121)
plt.plot(nbc1, ye_ncl,   label="ye")
plt.plot(nbc2, ye_nsat, dashes=[6, 2], label="ye_pair")
plt.xlim(0.00001,0.045)
plt.ylim(0.03,0.36)
#plt.ylim(50,550)
plt.xscale('log')
#plt.title("Variables: beta-eq :: ncl versus nsat")
plt.yscale('log')
plt.grid(True)
plt.ylabel("ye")
plt.xlabel("n_B (fm$^{-3}$)")
plt.legend(loc='lower left')
#plt.show()
#---------------------------------------------------------------------
# 2) plot A and Z versus nB
#ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
#---------------------------------------------------------------------
plt.subplot(122)
plt.plot(nbc1, ye_ncl,   label="ye")
plt.plot(nbc2, ye_nsat, dashes=[6, 2], label="ye_pair")
plt.xlim(0.04,0.045)
plt.ylim(0.032,0.04)
#plt.xscale('log')
#plt.yscale('log')
plt.title("Variables in beta-equilibrium")
plt.grid(True)
plt.ylabel("ye")
plt.xlabel("n_B (fm$^{-3}$)")
plt.legend(loc='upper right')
#plt.savefig("A,Z-cl_den.eps")
#plt.show()
#---------------------------------------------
#---------------------------------------------------------------------
# 7) plot gas and cluster pressures
#---------------------------------------------------------------------
#plt.subplot(427)
#plt.plot(nbc7, mu_cl_p,  label="cl_p")
#plt.plot(nbc7, mu_cl_n,  label="cl_n")
#plt.plot(nbc7, mu_g_n,   label="gas")
#plt.xscale('log')
#plt.yscale('log')
#plt.title("Ye=0.3")
#plt.grid(True)
#plt.ylabel("chemical pot")
#plt.xlabel("n_B (fm$^{-3}$)")
#plt.legend(loc='bottom left')
#---------------------------------------------------------------------
# 6) plot mu_n, mu_p and mu_gas
#---------------------------------------------------------------------
#plt.subplot(428)
#plt.plot(nbc7, press_cl,      label="P_cl")
#plt.plot(nbc7, press_unif,   label="P_unif")
#plt.xscale('log')
#plt.yscale('log')
#plt.grid(True)
#plt.ylabel("P (MeV)")
#plt.xlabel("n_B (fm$^{-3}$)")
#plt.legend(loc='bottom left')
plt.savefig("acoul_nclnsat.eps")
plt.show()


