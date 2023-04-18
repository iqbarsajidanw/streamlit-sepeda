import pickle
import streamlit as st

model = pickle.load(open('estimasi_sepeda_motor_bekas.sav', 'rb'))

st.title('Estimasi Harga Sepeda Motor Bekas')

year = st.number_input('Input tahun sepeda motor')
km_driven = st.number_input('Input kilometer sepeda motor')
ex_showroom_price = st.number_input('Input harga showroom sepeda motor')


predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, km_driven, ex_showroom_price]]
    )
    st.write ('Estimasi harga sepeda motor dalam US : ', predict)
    st.write ('Estimasi harga sepeda motor bekas dalam IDR (Juta) :', predict*14887)