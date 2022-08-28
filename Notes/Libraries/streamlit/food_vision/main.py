from helper import *
import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
st.set_page_config(page_title="Food Vision", page_icon="🍕")
st.title('Food Vision')
sns.set(style="ticks", context="talk")
plt.style.use("dark_background")
image_types = ["jpg", "png", "jpeg"]
def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('statics',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1    
    except:
        return 0

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file is not None:

    if save_uploaded_file(uploaded_file):
        if uploaded_file.name.split(".")[-1] not in image_types:
            st.error("Please upload an image file")
            file_path = os.path.join('statics',uploaded_file.name)
            os.remove(file_path)
        else:
            try:

                display_image = Image.open(uploaded_file)

                st.image(display_image, use_column_width="auto", caption="Uploaded Image")
                pred = st.markdown('**Predicting...**')
                image_path = os.path.join('statics',uploaded_file.name)
                prediction = predict(image_path=image_path, image_shape=224, n=10)
                pred.markdown("**Done!**")
                st.markdown("___")
                st.subheader('Predictions')

                fig, ax = plt.subplots()

                ax  = sns.barplot(x=prediction['Food'], y=prediction['Probability'])
                ax.set(xlabel='Food', ylabel='Probability')
                for item in ax.get_xticklabels():
                    item.set_rotation(90)
                # st.write(prediction)
                st.pyplot(fig)
            except Exception as e:
                st.write('Error')
                st.write(e)
            finally:
                os.remove(image_path)
    else:
        st.error("Please upload an image file")