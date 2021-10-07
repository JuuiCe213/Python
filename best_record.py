# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:19:16 2021

@author: ajaya
"""

def performance(total_record):
    #績效計算
    total_profit=[i[4]-i[2] if i[0]=='Buy' else i[2]-i[4] for i in total_record]
    print('總績效',sum(total_profit),'交易次數',len(total_profit),'平均績效',sum(total_profit)/len(total_profit))
    return sum(total_profit)/len(total_profit)
    '''
    buy_profit=[i[4]-i[2] for i in total_record if i[0]=='Buy']
    sell_profit=[i[2]-i[4] for i in total_record if i[0]=='Sell']
    if buy_profit != []:
        print('買方績效',sum(buy_profit),'交易次數',len(buy_profit),'平均買方',sum(buy_profit)/len(buy_profit))
    if sell_profit != []:
        print('賣方績效',sum(sell_profit),'交易次數',len(sell_profit),'平均賣方',sum(sell_profit)/len(sell_profit))
    earn_profit=[i for i in total_profit if i>0]
    loss_profit=[i for i in total_profit if i<0]
    earn_ratio=int((len(earn_profit)/len(total_profit))*100)
    print('勝率',earn_ratio,'%')
    avg_earn=sum(earn_profit)/len(earn_profit)
    avg_loss=sum(loss_profit)/len(loss_profit)
    earn_loss=avg_earn/abs(avg_loss)
    print('賺賠比',earn_loss)
    max_con_loss,con_loss=0,0
    for p in total_profit:
        if p<0:
            con_loss+=p
            max_con_loss=min(max_con_loss,con_loss)
        else:
            con_loss=0
    print('最大連續虧損',max_con_loss)
    # 最大資金回落
    acc_capital=[0]
    mdd,max_capital,c_capital=0,0,0
    for p in total_profit:
        acc_capital.append(acc_capital[-1]+p)
        c_capital += p
        max_capital = max(max_capital,c_capital)
        dd = max_capital - c_capital
        mdd = max(mdd,dd)
        #print('max_capital',max_capital,'c_capital',c_capital , 'dd',dd, 'mdd',mdd)
    print('最大資金回落',mdd)
    # 權益曲線圖
    #print(acc_capital)
    import matplotlib.pyplot as plt
    ax=plt.subplot(111)
    ax.plot(acc_capital)
    plt.show()
    '''