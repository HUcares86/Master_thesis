"""
要求：由三種model CF 透過FFT得到option價格
並寫自己的傅立葉轉換法與套用套件之傅立葉轉換法

先建立函式 -> 給參數出CF
以BSmodel為例
給五個參數得CF，
建立單一積分計算選擇權價格函式 需要參數 -> α η N(for put N跟η擇一給就好)
建立手動FFT函式 需要參數 -> α η N(for put N跟η擇一給就好)也要設定
設定 λ、β

"""
from CfOptionPricing import *
from Config import *
config = Config()


paramsMat = np.ones([len(config.times), config.PARAM_NUM])
cfOptionPricing = CfOptionPricing(config)
imply_volMat = cfOptionPricing.IVSurface()
iVParamOptim = IVParamOptim(paramsMat, config.times, config.log_Moneyness, imply_volMat, calendar=True, butterfly=False)
fitVol1, fitVol2, result1ParaMat, result2ParaMat = iVParamOptim.optimizing()

iVParamOptim.toCsv(result1ParaMat, "fit1_parameters.csv")
iVParamOptim.toCsv(result2ParaMat, "fit2_parameters.csv")

plot3D0 = Plot3D(config.times, config.log_Moneyness, imply_volMat)
plot3D0.plot("ModelIV")

plot3D1 = Plot3D(config.times, config.log_Moneyness, fitVol1)
plot3D1.plot("Optim1ModelIV Calendar_w=0 Butterfly_w=0")

plot3D2 = Plot3D(config.times, config.log_Moneyness, fitVol2)
plot3D2.plot(f"Optim2ModelIV Calendar_w={config.pen_weight_cale} Butterfly_w={config.pen_weight_butt}")
