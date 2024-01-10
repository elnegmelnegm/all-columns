import streamlit as st

# Display header
st.set_page_config(
    page_title="ُEDA AI Chat",
    page_icon="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png",
    layout="wide",
)
st.markdown('''
<img src="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png" width="250" height="100">''', unsafe_allow_html=True)

st.markdown('''
Powered by Streamlit <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png" width="22" height="22"> Python <img src="https://i.ibb.co/wwCs096/nn-1-removebg-preview-removebg-preview.png" width="22" height="22">''', unsafe_allow_html=True)


st.link_button("Drug Side Effects and Interactions App", "https://column2-jqjzxfvzdadyfkyghokvji.streamlit.app/",use_container_width= True, help="This application enables users to access comprehensive information about HPLC colums using Radar plot. هذا التطبيق يمكّن المستخدمين من الوصول إلى معلومات حول اعمدة الفصل المماثلة عن طريق استخدام رسم رادار ")
