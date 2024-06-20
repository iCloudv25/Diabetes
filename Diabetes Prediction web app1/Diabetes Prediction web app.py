import numpy as np
import pickle
import streamlit as st
from fpdf import FPDF
import base64

# Load the saved model
loaded_model = pickle.load(open(r"C:\Users\Edriane\Desktop\Diabetes Prediction web app\trained_model.sav", 'rb'))

# Function for Prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

# Function to save result as PDF
def save_as_pdf(name, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Diabetes Prediction Result", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    filename = "diabetes_prediction_result.pdf"
    pdf.output(filename)
    return filename

# Function to download file
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}" target="_blank">{file_label}</a>'
    return href

# Main function
def main():
    # Set page title and icon
    st.set_page_config(page_title="Diabetes Decision Support System", page_icon=":hospital:", layout="wide")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .css-18e3th9 {
            padding: 10px 0px;
        }
        .css-1d391kg {
            padding: 10px 0px;
        }
        .css-1q8dd3e {
            padding: 0px 10px;
        }
        .css-1j4j9li {
            background: #f0f2f6;
            border-radius: 10px;
            border: 2px solid #007bff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        .css-1v3fvcr {
            border-radius: 10px;
            background: #fff;
            border: 2px solid #007bff;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        .css-1l8iqjj {
            color: #007bff;
        }
        .stButton>button {
            display: flex;
            align-items: center;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            margin: 5px 0;
            width: 100%;
            border: none;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #007bff;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stButton>button:active {
            background-color: #004080;
        }
        .stButton>button svg {
            margin-right: 8px;
        }
        .stNumberInput>div>input, .stTextInput>div>input {
            border-radius: 5px;
            border: 1px solid #007bff;
        }
        .css-1v3fvcr h1, .css-1v3fvcr h2, .css-1v3fvcr h3, .css-1v3fvcr h4, .css-1v3fvcr h5, .css-1v3fvcr h6 {
            color: #007bff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state for page navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'Dashboard'

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button('Dashboard'):
        st.session_state.page = 'Dashboard'
    if st.sidebar.button('Prediction'):
        st.session_state.page = 'Prediction'
    if st.sidebar.button('Profile'):
        st.session_state.page = 'Profile'

    # Main content
    if st.session_state.page == 'Dashboard':
        st.markdown("""
        <div class='css-1v3fvcr'>
            <h1>Dashboard</h1>
            <div style='display: flex; align-items: center;'>
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3 13H5V21H3V13Z" fill="#007bff"/>
                    <path d="M8 9H10V21H8V9Z" fill="#007bff"/>
                    <path d="M13 5H15V21H13V5Z" fill="#007bff"/>
                    <path d="M18 1H20V21H18V1Z" fill="#007bff"/>
                </svg>
                <span style='margin-left: 10px;'>Welcome to the Diabetes Decision Support System Dashboard</span>
            </div>
            <p>Here you can find insights and data about diabetes.</p>
            <h3>Key Insights</h3>
            <ul>
                <li><strong>Insight 1</strong>: Description</li>
                <li><strong>Insight 2</strong>: Description</li>
                <li><strong>Insight 3</strong>: Description</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.page == 'Prediction':
        st.markdown("""
        <div class='css-1v3fvcr'>
            <h1>Diabetes Prediction</h1>
            <div style='display: flex; align-items: center;'>
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C13.1046 2 14 2.89543 14 4V20C14 21.1046 13.1046 22 12 22C10.8954 22 10 21.1046 10 20V4C10 2.89543 10.8954 2 12 2Z" fill="#007bff"/>
                    <path d="M4 7C5.10457 7 6 7.89543 6 9V20C6 21.1046 5.10457 22 4 22C2.89543 22 2 21.1046 2 20V9C2 7.89543 2.89543 7 4 7Z" fill="#007bff"/>
                    <path d="M20 12C21.1046 12 22 12.8954 22 14V20C22 21.1046 21.1046 22 20 22C18.8954 22 18 21.1046 18 20V14C18 12.8954 18.8954 12 20 12Z" fill="#007bff"/>
                </svg>
                <span style='margin-left: 10px;'>Enter the details to predict if the person is diabetic</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Getting the input data from the user
        with st.form(key='prediction_form'):
            name = st.text_input('Name')
            col1, col2 = st.columns(2)
            
            with col1:
                Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=1, step=1)
                Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, value=100)
                BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=200, value=80)
                SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100, value=20)
            
            with col2:
                Insulin = st.number_input('Insulin Level', min_value=0, max_value=900, value=30)
                BMI = st.number_input('BMI value', min_value=0.0, max_value=70.0, value=25.0)
                DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.5, value=0.5)
                Age = st.number_input('Age of the Person', min_value=0, max_value=120, value=30)
            
            # Create a button for Prediction
            submit_button = st.form_submit_button(label='Diabetes Test Result')

        # Code for Prediction
        if submit_button:
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
            result = f'{name}, {diagnosis}' if name else diagnosis
            st.success(result)
            st.write(result)
            
            if st.button('Save Result as PDF'):
                filename = save_as_pdf(name, result)
                st.success("Result saved as PDF successfully!")
                st.markdown(get_binary_file_downloader_html(filename, 'Download Result PDF'), unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.page == 'Profile':
        st.markdown("""
        <div class='css-1v3fvcr'>
            <h1>Profile</h1>
            <div style='display: flex; align-items: center;'>
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C13.1046 2 14 2.89543 14 4V20C14 21.1046 13.1046 22 12 22C10.8954 22 10 21.1046 10 20V4C10 2.89543 10.8954 2 12 2Z" fill="#007bff"/>
                    <path d="M4 7C5.10457 7 6 7.89543 6 9V20C6 21.1046 5.10457 22 4 22C2.89543 22 2 21.1046 2 20V9C2 7.89543 2.89543 7 4 7Z" fill="#007bff"/>
                    <path d="M20 12C21.1046 12 22 12.8954 22 14V20C22 21.1046 21.1046 22 20 22C18.8954 22 18 21.1046 18 20V14C18 12.8954 18.8954 12 20 12Z" fill="#007bff"/>
                </svg>
                <span style='margin-left: 10px;'>User Profile</span>
            </div>
            <p>This is the profile page. Add user profile components here.</p>
        </div>
        """, unsafe_allow_html=True)

# Run the main function
if __name__ == '__main__':
    main()
