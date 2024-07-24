import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('xgb_model.pkl', 'rb'))

st.title('Dropout Prediction')

st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)

# User inputs
Age_at_enrollment = st.number_input(
    "Umur berapa saat melakukan enrollment",
    min_value=17,
    max_value=70,
    step=1
)
Debtor = st.radio("Apakah mahasiswa tersebut melakukan pinjaman?", [0, 1], index=None)
Gender = st.radio("Gender Mahasiswa", ["Female", "Male"], index=None)
Application_mode = st.selectbox(
    "Mendaftar melalui apa",
    ('1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)', 
     'Holders of other higher courses', 'Ordinance No. 854-B/99', 'International student (bachelor)', 
     '1st phase - special contingent (Madeira Island)', '2nd phase - general contingent', '3rd phase - general contingent', 
     'Ordinance No. 533-A/99, item b2) (Different Plan)', 'Ordinance No. 533-A/99, item b3 (Other Institution)', 
     'Over 23 years old', 'Transfer', 'Change of course', 'Technological specialization diploma holders', 
     'Change of institution/course', 'Short cycle diploma holders', 'Change of institution/course (International)'),
    index=None,
    placeholder="Pilih metode pendaftaran...",
)
Curricular_units_2nd_sem_without_evaluations = st.number_input(
    "Curricular units 2nd sem without evaluations",
    min_value=0,
    max_value=12,
    step=1
)
Marital_status = st.selectbox(
    "Status Kawin",
    ('single', 'married', 'widower', 'divorced', 'facto union', 'legally separated'),
    index=None,
    placeholder="Pilih Status Kawin...",
)
Previous_qualification_grade = st.number_input(
    "Previous qualification grade (0-200)",
    min_value=0,
    max_value=200,
    step=1
)
Curricular_units_2nd_sem_evaluations = st.number_input(
    "Curricular units 2nd sem evaluations 0-33",
    min_value=0,
    max_value=33,
    step=1
)
Displaced = st.radio("Apakah siswa tersebut adalah orang terlantar?", [0, 1], index=None)
Admission_grade = st.number_input(
    "Curricular units 2nd sem grade 0-200",
    min_value=0,
    max_value=200,
    step=1
)
Curricular_units_1st_sem_enrolled = st.number_input(
    "Curricular units 1st sem without evaluations 0-23",
    min_value=0,
    max_value=23,
    step=1
)
Curricular_units_2nd_sem_enrolled = st.number_input(
    "Curricular units 2nd sem enrolled 0-23",
    min_value=0,
    max_value=23,
    step=1
)
Scholarship_holder = st.radio("Apakah siswa tersebut adalah penerima beasiswa?", [0, 1], index=None)
Tuition_fees_up_to_date = st.radio("Apakah biaya sekolah siswa terkini?", [0, 1], index=None)
Curricular_units_1st_sem_grade = st.number_input(
    "Curricular units 1st sem grade 0-19",
    min_value=0,
    max_value=19,
    step=1
)
Curricular_units_1st_sem_approved = st.number_input(
    "Curricular units 1st sem approved 0-22",
    min_value=0,
    max_value=20,
    step=1
)
Curricular_units_2nd_sem_grade = st.number_input(
    "Curricular units 2nd sem grade 0-19",
    min_value=0,
    max_value=19,
    step=1
)
Curricular_units_2nd_sem_approved = st.number_input(
    "Curricular units 2nd sem approved 0-22",
    min_value=0,
    max_value=20,
    step=1
)

Dropout_Prediction = ''

if st.button("Check"):
    # Convert categorical features to numerical codes
    application_mode_mapping = {
        '1st phase - general contingent': 1, 'Ordinance No. 612/93': 2, 
        '1st phase - special contingent (Azores Island)': 5, 'Holders of other higher courses': 7, 
        'Ordinance No. 854-B/99': 10, 'International student (bachelor)': 15, 
        '1st phase - special contingent (Madeira Island)': 16, '2nd phase - general contingent': 17, 
        '3rd phase - general contingent': 18, 'Ordinance No. 533-A/99, item b2) (Different Plan)': 26, 
        'Ordinance No. 533-A/99, item b3 (Other Institution)': 27, 'Over 23 years old': 39, 'Transfer': 42, 
        'Change of course': 43, 'Technological specialization diploma holders': 44, 
        'Change of institution/course': 51, 'Short cycle diploma holders': 53, 
        'Change of institution/course (International)': 57
    }
    marital_status_mapping = {
        'single': 1, 'married': 2, 'widower': 3, 'divorced': 4, 'facto union': 5, 'legally separated': 6
    }
    gender_mapping = {'Female': 0, 'Male': 1}
    
    Application_mode_code = application_mode_mapping[Application_mode]
    Marital_status_code = marital_status_mapping[Marital_status]
    Gender_code = gender_mapping[Gender]

    input_data = np.array([[
        Age_at_enrollment, Debtor, Gender_code, Application_mode_code,
        Curricular_units_2nd_sem_without_evaluations, Marital_status_code,
        Previous_qualification_grade, Curricular_units_2nd_sem_evaluations,
        Displaced, Admission_grade, Curricular_units_1st_sem_enrolled,
        Curricular_units_2nd_sem_enrolled, Scholarship_holder,
        Tuition_fees_up_to_date, Curricular_units_1st_sem_grade,
        Curricular_units_1st_sem_approved, Curricular_units_2nd_sem_grade,
        Curricular_units_2nd_sem_approved
    ]])
    
    st.write("Input data:", input_data)  # Debugging: print the input data
    
    try:
        result = model.predict(input_data)
        if result[0] == 1:
            Dropout_Prediction = " Siswa Tersebut Kemungkinan besar dropout"
            st.error(Dropout_Prediction)
        else:
            Dropout_Prediction = "Siswa Tersebut Kemungkinan besar lulus"
            st.success(Dropout_Prediction)
    except Exception as e:
        st.error(f"An error occurred: {e}")
