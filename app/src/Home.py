import streamlit as st
from modules.nav import SideBarLinks

st.session_state['authenticated'] = False

st.set_page_config(layout = 'wide')

SideBarLinks(show_home=True)

# set the title of the page and provide a simple prompt. 
st.title('Warehouse Manager Portal')
st.write('\n\n')
st.write('### Reports')

if st.button("Show All Reorders", 
            type = 'primary', 
            use_container_width=True):
    st.switch_page('pages/41_Reorders.py')

if st.button('Show Low Stock', 
            type = 'primary', 
            use_container_width=True):
    st.switch_page('pages/42_Low_Stock.py')

st.write('\n\n')
st.write('### New Products and Categories')

if st.button('Add New Product Category', 
            type = 'primary', 
            use_container_width=True):
    st.switch_page('pages/43_New_Cat.py')

if st.button('Add New Product', 
            type = 'primary', 
            use_container_width=True):
    st.switch_page('pages/44_New_Product.py')



