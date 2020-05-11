# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:33:34 2020
Option Trading Strategy Visualisation
@author: Linh Ngo
"""

import matplotlib.pyplot as plt
import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Parse bool")
parser.add_argument("--lc", default=False, action="store_true", help="enable LC")
parser.add_argument("--lcv", nargs='+', default=[0, 0, 0], type=float, help='LC k p n value')
parser.add_argument("--lc2", default=False, action="store_true", help="enable LC2")
parser.add_argument("--lcv2", nargs='+', default=[0, 0, 0], type=float, help='LC2 k p n value')
parser.add_argument("--lp", default=False, action="store_true" , help="enable LP")
parser.add_argument("--lpv", nargs='+', default=[0, 0, 0], type=float, help='LP k p n value')
parser.add_argument("--lp2", default=False, action="store_true" , help="enable LP2")
parser.add_argument("--lpv2", nargs='+', default=[0, 0, 0], type=float, help='LP2 k p n value')
parser.add_argument("--sc", default=False, action="store_true" , help="enable SC")
parser.add_argument("--scv", nargs='+', default=[0, 0, 0], type=float, help='SC k p n value')
parser.add_argument("--sc2", default=False, action="store_true" , help="enable SC2")
parser.add_argument("--scv2", nargs='+', default=[0, 0, 0], type=float, help='SC2 k p n value')
parser.add_argument("--sp", default=False, action="store_true" , help="enable SP")
parser.add_argument("--spv", nargs='+', default=[0, 0, 0], type=float, help='SP k p n value')
parser.add_argument("--sp2", default=False, action="store_true" , help="enable SP2")
parser.add_argument("--spv2", nargs='+', default=[0, 0, 0], type=float, help='SP2 k p n value')
parser.add_argument("--lpos", default=False, action="store_true", help="enable Long stock position")
parser.add_argument("--lposv", nargs='+', default=[0, 0], type=float, help='Long stock position k n value')
parser.add_argument("--spos", default=False, action="store_true", help="enable Short stock position")
parser.add_argument("--sposv", nargs='+', default=[0, 0], type=float, help='Short stock position k n value')


args = parser.parse_args()
LC = args.lc
lcv = args.lcv
LC2 = args.lc2
lcv2 = args.lcv2
SC = args.sc
scv = args.scv
SC2 = args.sc2
scv2 = args.scv2
LP = args.lp
lpv = args.lpv
LP2 = args.lp2
lpv2 = args.lpv2
SP = args.sp
spv = args.spv
SP2 = args.sp2
spv2 = args.spv2
Lpos = args.lpos
lposv = args.lposv
Spos = args.spos
sposv = args.sposv

print('LC arg: ', LC, lcv)
print('LC2 arg: ', LC2, lcv2)
print('LP arg: ', LP, lpv)
print('LP2 arg: ', LP2, lpv2)
print('SC arg: ', SC, scv)
print('SC2 arg: ', SC2, scv2)
print('SP arg: ', SP, spv)
print('SP2 arg: ', SP2, spv2)
print('Lpos arg: ', Lpos, lposv)
print('Spos arg: ', Spos, sposv)

# Stock price range at expiration:
if LC is True and SC is True:
    maxx = max(lcv[0], lcv2[0], lpv[0], lpv2[0], scv[0], scv2[0], spv[0], spv2[0])*1.5
if LP is True and SP is True:
    maxx = max(lcv[0], lcv2[0], lpv[0], lpv2[0], scv[0], scv2[0], spv[0], spv2[0])*1.5
if LC2 is True or SC2 is True or LP2 is True or SP2 is True:
    maxx = max(lcv[0], lcv2[0], lpv[0], lpv2[0], scv[0], scv2[0], spv[0], spv2[0])*1.25
else:
    maxx = max(lcv[0], lcv2[0], lpv[0], lpv2[0], scv[0], scv2[0], spv[0], spv2[0])*2
sT = np.linspace(0, maxx, maxx*1000)
y0 = np.zeros(len(sT))
total_premium = (lcv[1]*lcv[2] + lcv2[1]*lcv2[2] + lpv[1]*lpv[2] + lpv2[1]*lpv2[2] + 
                 scv[1]*scv[2] + scv2[1]*scv2[2] + spv[1]*spv[2] + spv2[1]*spv2[2])
# long call
if LC is True:
    y_lc = np.where(sT > lcv[0], (sT-lcv[0]+lcv[1])*lcv[2], lcv[1]*lcv[2])
    lc_break_even = (lcv[0]*lcv[2] - total_premium)/lcv[2]
else:
    y_lc = y0
if LC2 is True:
    y_lc2 = np.where(sT > lcv2[0], (sT-lcv2[0]+lcv2[1])*lcv2[2], lcv2[1]*lcv2[2])
    lc2_break_even = (lcv2[0]*lcv2[2] - total_premium)/lcv2[2]
else:
    y_lc2 = y0
# long put
if LP is True:
    y_lp = np.where(sT < lpv[0], (lpv[0]-sT+lpv[1])*lpv[2], lpv[1]*lpv[2])
    lp_break_even = (lpv[0]*lpv[2] + total_premium)/lpv[2]
else:
    y_lp = y0
if LP2 is True:
    y_lp2 = np.where(sT < lpv2[0], (lpv2[0]-sT+lpv2[1])*lpv2[2], lpv2[1]*lpv2[2])
    lp2_break_even = (lpv2[0]*lpv2[2] + total_premium)/lpv2[2]
else:
    y_lp2 = y0
# short call
if SC is True:
    y_sc = np.where(sT > scv[0], (scv[0]-sT+scv[1])*scv[2], scv[1]*scv[2])
    sc_break_even = (scv[0]*scv[2] + total_premium)/scv[2]
else:
    y_sc = y0
if SC2 is True:
    y_sc2 = np.where(sT > scv2[0], (scv2[0]-sT+scv2[1])*scv2[2], scv2[1]*scv2[2])
    sc2_break_even = (scv2[0]*scv2[2] + total_premium)/scv2[2]
else:
    y_sc2 = y0
# short put
if SP is True:
    y_sp = np.where(sT < spv[0], (sT-spv[0]+spv[1])*spv[2], spv[1]*spv[2])
    sp_break_even = (spv[0]*spv[2] - total_premium)/spv[2]
else:
    y_sp = y0
if SP2 is True:
    y_sp2 = np.where(sT < spv2[0], (sT-spv2[0]+spv2[1])*spv2[2], spv2[1]*spv2[2])
    sp2_break_even = (spv2[0]*spv2[2] - total_premium)/spv2[2]
else:
    y_sp2 = y0
# Long stock
if Lpos is True:
    y_lpos = (sT-lposv[0]) * lposv[1]
else:
    y_lpos = y0
# Short stock
if Spos is True:
    y_spos = (sposv[0]-sT) * sposv[1]
else:
    y_spos = y0
# Plot all
y = y_lc + y_lc2 + y_lp + y_lp2 + y_sc + y_sc2 + y_sp + y_sp2 + y_lpos + y_spos
#break_even_pt = sT[(y == 0)]
#y_neg_id = np.where(y <= 0)[0]
#break_id = [y_neg_id[0], y_neg_id[-1]]
break_id = []
for i in range(len(y)-1):
    if y[i] == 0 or y[i]*y[i+1] < 0:
        break_id.append(i)
break_even_pt = sT[break_id]
strings = ["%.2f" % number for number in break_even_pt]
join = '; '.join(strings)
if len(strings) < 10:
    print('Break-even point(s): ', join)
else:
    print('Minimum/maximum gain is 0')

if LP is True and Lpos is True:
    title = 'Protective Put Strategy'
    y_label = 'Synthetic Long Call'
if LC is True and Spos is True:
    title = 'Covered Call Strategy'
    y_label = 'Synthetic Long Put'
if LC is True and LP is True and lcv[0] == lpv[0]:
    title = 'Long Straddle Strategy'
    y_label = 'Long Straddle'
if SC is True and SP is True and scv[0] == spv[0]:
    title = 'Short Straddle Strategy'
    y_label = 'Short Straddle'
if LC is True and LP is True and lcv[0] > lpv[0]:
    title = 'Long Strangle Strategy'
    y_label = 'Long Strangle'
if SC is True and SP is True and scv[0] > spv[0]:
    title = 'Short Strangle Strategy'
    y_label = 'Short Strangle'
if LC is True and SC is True and lcv[0] < scv[0]:
    title = 'Bull Spread Strategy'
    y_label = 'Bull Spread'
if LP is True and SP is True and lpv[0] < spv[0]:
    title = 'Bull Spread Strategy'
    y_label = 'Bull Spread'
if LC is True and SC is True and lcv[0] > scv[0]:
    title = 'Bear Spread Strategy'
    y_label = 'Bear Spread'
if LP is True and SP is True and lpv[0] > spv[0]:
    title = 'Bear Spread Strategy'
    y_label = 'Bear Spread'
if LC2 is True or LP2 is True or SC2 is True or SP2 is True:
    title = 'Butterfly Spread Strategy'
    y_label = 'Butterfly Spread'

plt.plot(sT, y, 'k', linewidth=2, label=y_label)
#plt.plot(sT, y0, 'k', linewidth=1)
if LC is True:
    plt.plot(sT, y_lc, 'b', linewidth=1, label='Long Call')
if LC2 is True:
    plt.plot(sT, y_lc2, 'r', linewidth=1, label='Long Call 2')
if LP is True:
    plt.plot(sT, y_lp, 'r', linewidth=1, label='Long Put')
if LP2 is True:
    plt.plot(sT, y_lp2, 'b', linewidth=1, label='Long Put 2')
if SC is True:
    plt.plot(sT, y_sc, 'c', linewidth=1, label='Short Call')
if SC2 is True:
    plt.plot(sT, y_sc2, 'm', linewidth=1, label='Short Call 2')
if SP is True:
    plt.plot(sT, y_sp, 'm', linewidth=1, label='Short Put')
if SP2 is True:
    plt.plot(sT, y_sp2, 'c', linewidth=1, label='Short Put 2')
if Lpos is True:
    plt.plot(sT, y_lpos, 'b', linewidth=1, label='Long Stock')
if Spos is True:
    plt.plot(sT, y_spos, 'r', linewidth=1, label='Short Stock')
if len(strings) < 10:
    plt.plot(break_even_pt, [0]*len(break_even_pt), 'r*--', markersize=8, 
             linewidth=0, label='Break-even point(s): %s' % join)
plt.title(label=title, fontsize=18)
plt.legend()
plt.grid()
plt.xlabel('Terminal Price', fontsize=16)
plt.ylabel('Gain/Loss', fontsize=16)
plt.minorticks_on()
#plt.text(110, 0, 'Break-even point')
plt.savefig(title + '.png', dpi=100, bbox_inches='tight')
#plt.show()

