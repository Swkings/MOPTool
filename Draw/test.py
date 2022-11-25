#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : test.py
@Date  : 2020/07/15
@Desc  : 
"""

import numpy as np
import matplotlib.pyplot as plt


def model(x, p):
	return x ** (2 * p + 1) / (1 + x ** (2 * p))


x = np.linspace(0.75, 1.25, 201)


def f1():
	with plt.style.context(['science']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig1.pdf')  # fig.savefig('figures/fig1.jpg', dpi=300)


def f2():
	with plt.style.context(['science', 'ieee']):
		fig, ax = plt.subplots()
		for p in [10, 20, 50]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig2.pdf')  # fig.savefig('figures/fig2.jpg', dpi=300)


def f3():
	with plt.style.context(['science', 'scatter']):
		fig, ax = plt.subplots(figsize=(4, 4))
		ax.plot([-2, 2], [-2, 2], 'k--')
		ax.fill_between([-2, 2], [-2.2, 1.8], [-1.8, 2.2], color='dodgerblue', alpha=0.2, lw=0)
		for i in range(7):
			x1 = np.random.normal(0, 0.5, 10)
			y1 = x1 + np.random.normal(0, 0.2, 10)
			ax.plot(x1, y1, label='$^\#${}'.format(i + 1))
		ax.legend(title='Sample', loc=2)
		# ax.set_xlabel(r"$\log_{10}\left(\frac{L_\mathrm{IR}}{\mathrm{L}_\odot}\right)$")
		# ax.set_ylabel(r"$\log_{10}\left(\frac{L_\mathrm{6.2}}{\mathrm{L}_\odot}\right)$")
		ax.set_xlim([-2, 2])
		ax.set_ylim([-2, 2])  # fig.savefig('figures/fig3.pdf')  # fig.savefig('figures/fig3.jpg', dpi=300)


def f4():
	with plt.style.context(['science', 'high-vis']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig4.pdf')  # fig.savefig('figures/fig4.jpg', dpi=300)


def f5():
	with plt.style.context(['dark_background', 'science', 'high-vis']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig5.pdf')  # fig.savefig('figures/fig5.jpg', dpi=300)


def f6():
	with plt.style.context(['science', 'notebook']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig10.pdf')  # fig.savefig('figures/fig10.jpg', dpi=300)


# Plot different color cycles

def f7():
	with plt.style.context(['science', 'bright']):
		fig, ax = plt.subplots()
		for p in [5, 10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig6.pdf')  # fig.savefig('figures/fig6.jpg', dpi=300)


def f8():
	with plt.style.context(['science', 'vibrant']):
		fig, ax = plt.subplots()
		for p in [5, 10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig7.pdf')  # fig.savefig('figures/fig7.jpg', dpi=300)


def f9():
	with plt.style.context(['science', 'muted']):
		fig, ax = plt.subplots()
		for p in [5, 7, 10, 15, 20, 30, 38, 50, 100, 500]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order', fontsize=7)
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig8.pdf')  # fig.savefig('figures/fig8.jpg', dpi=300)


def f10():
	with plt.style.context(['science', 'retro']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig9.pdf')  # fig.savefig('figures/fig9.jpg', dpi=300)


def f11():
	with plt.style.context(['science', 'grid']):
		fig, ax = plt.subplots()
		for p in [10, 15, 20, 30, 50, 100]:
			ax.plot(x, model(x, p), label=p)
		ax.legend(title='Order')
		ax.set(xlabel='Voltage (mV)')
		ax.set(ylabel='Current ($\mu$A)')
		ax.autoscale(tight=True)  # fig.savefig('figures/fig11.pdf')  # fig.savefig('figures/fig11.jpg', dpi=300)


if __name__ == '__main__':
	f11()
	plt.show()
