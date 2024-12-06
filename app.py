import streamlit as st

# Predict TSAT based on Hemoglobin
def predict_tsat(hb):
    tsat = -9.40 + 2.63 * hb
    if tsat < 20:
        status = "Iron Deficiency"
    elif 20 <= tsat <= 40:
        status = "Normal"
    else:
        status = "Iron Overload"
    return tsat, status

# Streamlit App
st.title("Iron Status Predictor")
st.write("Enter your Hemoglobin (Hb) level to predict TSAT and your iron status.")

# User Input
hb_input = st.number_input("Hemoglobin (Hb) level", min_value=0.0, step=0.1)

# Display Results
if hb_input > 0:
    tsat, status = predict_tsat(hb_input)
    st.write(f"**Predicted TSAT:** {tsat:.2f}%")
    st.write(f"**Iron Status:** {status}")
