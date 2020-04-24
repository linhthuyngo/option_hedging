# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:33:34 2020

@author: Linh Ngo
"""

import matplotlib.pyplot as plt
import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Parse bool")
parser.add_argument("--lc", default=False, action="store_true", help="enable LC")
parser.add_argument("--lcv", nargs='+', default=[0, 0, 0], type=float, help='LC k p n value')
parser.add_argument("--lp", default=False, action="store_true" , help="enable LP")
parser.add_argument("--lpv", nargs='+', default=[0, 0, 0], type=float, help='LP k p n value')
parser.add_argument("--sc", default=False, action="store_true" , help="enable SC")
parser.add_argument("--scv", nargs='+', default=[0, 0, 0], type=float, help='SC k p n value')
parser.add_argument("--sp", default=False, action="store_true" , help="enable SC")
parser.add_argument("--spv", nargs='+', default=[0, 0, 0], type=float, help='SC k p n value')
parser.add_argument("--lpos", default=False, action="store_true", help="enable Long Position")
parser.add_argument("--lposv", nargs='+', default=[0, 0], type=float, help='Long Position k n value')
parser.add_argument("--spos", default=False, action="store_true", help="enable Short Position")
parser.add_argument("--sposv", nargs='+', default=[0, 0], type=float, help='Short Position k n value')


args = parser.parse_args()
LC = args.lc
lcv = args.lcv
SC = args.sc
scv = args.scv
LP = args.lp
lpv = args.lpv
SP = args.sp
spv = args.spv
Lpos = args.lpos
lposv = args.lposv
Spos = args.spos
sposv = args.sposv

print('LC arg: ', LC, lcv)
print('LP arg: ', LP, lpv)
print('SC arg: ', SC, scv)
print('SP arg: ', SP, spv)
print('Lpos arg: ', Lpos, lposv)
print('Spos arg: ', Spos, sposv)

# Stock price range at expiration:
sT = np.arange(start=0, stop=max(lcv[0], lpv[0], scv[0], spv[0])*2)
y0 = np.zeros(len(sT))
total_premium = lcv[1]*lcv[2] + lpv[1]*lpv[2] + scv[1]*scv[2] + spv[1]*spv[2]
# long call
if LC is True:
    y_lc = np.where(sT > lcv[0], (sT-lcv[0]+lcv[1])*lcv[2], lcv[1]*lcv[2])
    lc_break_even = (lcv[0]*lcv[2] - total_premium)/lcv[2]
#    print('LC investment(s) break even if: sT >', lc_break_even)
else:
    y_lc = y0
# long put
if LP is True:
    y_lp = np.where(sT < lpv[0], (lpv[0]-sT+lpv[1])*lpv[2], lpv[1]*lpv[2])
    lp_break_even = (lpv[0]*lpv[2] + total_premium)/lpv[2]
#    print('LP investment(s) break even if: sT <', lp_break_even)
else:
    y_lp = y0
# short call
if SC is True:
    y_sc = np.where(sT > scv[0], (scv[0]-sT+scv[1])*scv[2], scv[1]*scv[2])
    sc_break_even = (scv[0]*scv[2] + total_premium)/scv[2]
#    print('SC ivestment(s) break even if: sT <', sc_break_even)
else:
    y_sc = y0
# short put
if SP is True:
    y_sp = np.where(sT < spv[0], (sT-spv[0]+spv[1])*spv[2], spv[1]*spv[2])
    sp_break_even = (spv[0]*spv[2] - total_premium)/spv[2]
#    print('SP investment(s) break even if: sT >', sp_break_even)
else:
    y_sp = y0
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
y = y_lc + y_lp + y_sc + y_sp + y_lpos + y_spos
break_even_pt = sT[(y == 0)]
print('Hedged position breaks even when sT is: ', break_even_pt)

plt.plot(sT, y, 'k', linewidth=2)
plt.plot(sT, y0, 'k', linewidth=1)
if LC is True:
    plt.plot(sT, y_lc, 'b', linewidth=1, label='Long Call')
if LP is True:
    plt.plot(sT, y_lp, 'r', linewidth=1, label='Long Put')
if SC is True:
    plt.plot(sT, y_sc, 'c', linewidth=1, label='Short Call')
if SP is True:
    plt.plot(sT, y_sp, 'm', linewidth=1, label='Short Put')
if Lpos is True:
    plt.plot(sT, y_lpos, 'b', linewidth=1, label='Long Stock')
if Spos is True:
    plt.plot(sT, y_spos, 'r', linewidth=1, label='Short Stock')

plt.legend()
plt.grid()
plt.xlabel('Terminal Price', fontsize=16)
plt.ylabel('Gain/Loss', fontsize=16)
#plt.savefig('Answer to Qn4 in Practice Questions B', dpi=100, bbox_inches='tight')
plt.show()


