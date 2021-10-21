# -*- coding:utf-8 -*-
import streamlit as st
import time
import numpy as np
import pandas as pd
import sqlalchemy as sqla
from datetime import timedelta, date
import configparser
st.set_page_config(layout='wide')
def cal_roi(ints, years, perc, value, alq, gas, jove):
	month_rate = ints / 100.0 / 12
	m = years * 12
	debt = value * perc / 100.0
	month_payment = (debt * month_rate * ((1+month_rate)**m)) / ((1+month_rate)**m - 1)
	if jove:
		ent = value * (105 - perc) / 100.0
	else:
		ent = value * (110 - perc) / 100.0
	ibi = value * 0.008 / 12
	roi = (alq - month_payment - gas - ibi) * 12 / ent
	s = """Compra un piso por el valor de {0} euro, con {1}% de hipoteca, durante {2} años:
	Pago inicial: {3} 
	Pago mensual: {4} 
	Si podrías alquilarlo por {5} euros/mes, el ROI anual será: {6}%""".format((value), (perc), (years), (ent), (month_payment), (alq), (roi * 100))
	#st.write(s)
	st.write('El valor de piso:', value)
	st.write('Pago inicial:', ent)
	st.write('Pago mensual:', month_payment)
	st.write('Si podrías alquilarlo por ', alq, ' euros/mes, el ROI anual será: ', (roi * 100), '%')


#cal_roi(1.35, 30, 90, 150000, 800)
col7, col8= st.beta_columns([8,2])
with col7:
	value = st.text_input("Valor de piso (euro): ", '200000')
	value = int(value)
with col8:
	perc = st.selectbox("Porcentaje de hipoteca (%): ", ('50%', '60%', '70%', '80%', '90%', '95%', '100%'))
	perc = int(perc[:-1])

col1, col2= st.beta_columns([7,3])
with col1:
	ints = st.number_input('Tipo de interés (%):', 0.01, 3.00, 0.89, 0.1)
with col2:
	age = st.number_input('Edad:', 18, 54, 30, 1)
if age > 32:
	jove = 0
else:
	jove = 1
duration = min([70 - age, 40])
x = min([duration, 30])
years = st.slider('Duración de hipoteca (años): ', 15, duration, x)

alq = st.slider('Ingresos de alquiler esperados (euros/mes): ', 400, 1500, 800, 50)

gas = st.text_input('Gastos (euros/mes): ', 100)

if st.button('Simular'):
	cal_roi(ints, years, perc, value, alq, int(gas), jove)
