import pandas as pd
import os
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_1/DE_m_0_v_1_l_01_1.csv')
df2 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_1/DE_m_0_v_1_l_005_1.csv')

df3 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_05/DE_m_0_v_05_l_01_1.csv')
df4 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_05/DE_m_0_v_05_l_005_1.csv')

df5 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_15/DE_m_0_v_15_l_01_1.csv')
df6 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_0_v_15/DE_m_0_v_15_l_005_1.csv')


df7 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_1/DE_m_05_v_1_l_01_1.csv')
df8 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_1/DE_m_05_v_1_l_005_1.csv')

df9 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_05/DE_m_05_v_05_l_01_1.csv')
df10 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_05/DE_m_05_v_05_l_005_1.csv')

df11 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_15/DE_m_05_v_15_l_01_1.csv')
df12 = pd.read_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/m_05_v_15/DE_m_05_v_15_l_005_1.csv')

S_array = np.array(df1['S'])
call1 = np.array(df1['call'])
call2 = np.array(df2['call'])
call3 = np.array(df3['call'])
call4 = np.array(df4['call'])
call5 = np.array(df5['call'])
call6 = np.array(df6['call'])
call7 = np.array(df7['call'])
call8 = np.array(df8['call'])
call9 = np.array(df9['call'])
call10 = np.array(df10['call'])
call11 = np.array(df11['call'])
call12 = np.array(df12['call'])
fig = plt.figure()
plt.plot(S_array, call1, label='mean=0, var=1, lamda=0.1')#, c=color_array[i]
plt.plot(S_array, call2, label='mean=0, var=1, lamda=0.05')#, c=color_array[i]

plt.plot(S_array, call3, label='mean=0, var=0.5, lamda=0.1')#, c=color_array[i]
plt.plot(S_array, call4, label='mean=0, var=0.5, lamda=0.05')#, c=color_array[i]

plt.plot(S_array, call5, label='mean=0, var=1.5, lamda=0.1')#, c=color_array[i]
plt.plot(S_array, call6, label='mean=0, var=1.5, lamda=0.05')#, c=color_array[i]

plt.plot(S_array, call7, label='mean=0.5, var=1, lamda=0.1')#, c=color_array[i]
plt.plot(S_array, call8, label='mean=0.5, var=1, lamda=0.05')#, c=color_array[i]

plt.plot(S_array, call9, label='mean=0.5, var=0.5, lamda=0.1')#, c=color_array[i]
plt.plot(S_array, call10, label='mean=0.5, var=0.5, lamda=0.05')#, c=color_array[i]

# plt.plot(S_array, call11, label='mean=0.5, var=1.5, lamda=0.1')#, c=color_array[i]
# plt.plot(S_array, call12, label='mean=0.5, var=1.5, lamda=0.05')#, c=color_array[i]


plt.xlabel('$S_0$')
plt.ylabel('call value')
plt.title(f'DE call value')
plt.axvline(100, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()
