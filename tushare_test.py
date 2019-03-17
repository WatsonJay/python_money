import tushare as ts
import pandas as pd
from pyecharts import Kline
#正常显示画图时出现的中文和负号


if __name__ == '__main__':
    token = '8b09761b8473e73a0a57bafa07ea2766dfba5d3472d527c40e03d47b'
    pro = ts.pro_api(token)
    from pylab import mpl
    mpl.rcParams['font.sans-serif']=['SimHei']
    mpl.rcParams['axes.unicode_minus']=False

    # 获取平安银行日行情数据
    pa = pro.daily(ts_code='000001.SZ', start_date='20180101',
                   end_date='20190106')
    # pa.head()
    # K线图可视化
    pa.index = pd.to_datetime(pa.trade_date)
    pa = pa.sort_index()
    v1 = list(pa.loc[:, ['open', 'close', 'low', 'high']].values)
    t = pa.index
    v0 = list(t.strftime('%Y%m%d'))
    kline = Kline("平安银行K线图", title_text_size=15)
    kline.add("", v0, v1, is_datazoom_show=True,
              mark_line=["average"],
              mark_point=["max", "min"],
              mark_point_symbolsize=60,
              mark_line_valuedim=['highest', 'lowest'])
    kline.render("上证指数图.html")