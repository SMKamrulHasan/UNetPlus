import numpy as np
from scipy import stats
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

"""

Myocardial Mass ED

"""

auto_ED_Myo_Mass = np.array([183349.609375
,181792.96875
,182976.822669983
,60789.55078125
,156115.72265625
,157034.118652344
,95858.3605499268
,125610.3515625
,146155.725517273
,66088.8671875
,105493.1640625
,95166.015625
,102083.472846985
,94833.6481323242
,73320.6992340088

])


manual_ED_Myo_Mass = np.array([164257.8125
,183691.40625
,188135.83820343
,70459.716796875
,176676.940917969
,187925.354003906
,92289.4210891724
,137386.322021484
,132912.886299133
,65502.9296875
,98706.0546875
,106298.828125
,97772.5845108032
,93511.6177215576
,68698.119140625
])





def corr(auto, manual):
    stk = np.vstack([auto, np.ones(len(auto))]).T
    slop,intercpt = np.linalg.lstsq(stk,auto)[0]
    rho = np.round(stats.pearsonr(auto, manual),2)
    MSE= mean_squared_error(auto,manual)
    plt.axis([0, (np.max(auto)+5), 0, (np.max(manual)+5)], fontsize = '10', lw = '2')
    plt.plot(auto, manual, marker ='x', mfc = 'green', ls = 'None', mec = 'blue', mew= '1.5', ms = '4', lw = '2')
    plt.plot(auto, slop*auto + intercpt , 'r', lw = '2')
    plt.xlabel('Prediction Myo Mass-ED (g)', fontsize = '11')
    plt.ylabel('GT Myo Mass-ED (g)', fontsize = '11')
    plt.legend()
    plt.tick_params(axis='both', which='major', labelsize= '11', width = '2')

    if rho[1] < 0.01:
            P = '(P<0.01)'
    else:
            P = '(P=' + str(rho[1]) + ')'
    
    plt.text(2, 7, 'rho =' + str(rho[0]) + P, fontsize='9',color='blue')
    plt.text(2, 50, MSE, fontsize='12')
    ax =plt.gca()
    ax.spines['top'].set_linewidth('2')
    ax.spines['left'].set_linewidth('2')
    ax.spines['right'].set_linewidth('2')
    ax.spines['bottom'].set_linewidth('2')
    return;


plt.figure()
corr(auto_ED_Myo_Mass/1000, manual_ED_Myo_Mass/1000)
plt.savefig("corr_Myo_massED.pdf",format='pdf', dpi=1000)
plt.show()





