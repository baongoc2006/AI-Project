import streamlit as st

st.title('Vo Nguyen Bao Ngoc')
st.header('Web AI cua Bao Ngoc')
st.subheader('NLP')
st.text('tui la bao ngoc')
st.caption('this is a caption')
st.divider()
st.markdown('# Heading 1')
st.markdown('[bngoc viet nam](https://)')
st.markdown("""
            1. Machine Learning
            2.Deep Learning
            
""")
st.markdown(r'$\sqrt{2x}$')
st.divider()
st.latex('\sqrt{2x}')
st.divider()

st.write('ai vietnam')
st.write('# heading')
st.write('1 + 1 =', 2,3)

st.divider()
st.code( """
        import random
        value = value
""" )
def get_year():
    return '20'
with st.echo():
    st.write('this is a text')
    def get_name():
        return 'Ngoc'
    
    name = get_name()
    year = get_year()
    st.write(name, year)

st.divider()
st.logo('./sububinh.jpg')
st.image('./sububinh.jpg', caption='su need milk')

def get_fullname():
    return 'Ngoc'
agree = st.checkbox('I agree!', on_change=get_fullname())
if agree:
    st.write('Thank!')

status = st.radio('Your favorite color:', ['yellow', 'red'], captions=['vang', 'xanh'])
print(status)

status = st.selectbox('your contact', ['email', 'address'])
print(status)

status = st.multiselect('Color:', ['green', 'yellow', 'blue'], ['yellow'])
print(status)

st.select_slider('your colors:', [0,1,2])

st.divider()
if st.button('say hello'):
    st.write('hello')
else:
    st.write('goodbye')

st.text_input('your name', value='ngoc')

uploaded_file = st.file_uploader('choose files', accept_multiple_files=True)
for file in uploaded_file:
    content = file.read()
    st.write('file name:', file.name)

st.divider()

with st.form('my form'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('name:')
    f_age = col2.text_input('age:')

    submitted  = st.form_submit_button('submit')
    if submitted:
        st.write(f"Name: {f_name}, Age: {f_age}")
    
st.divider()

import random
value = random.randint(1,10)
if 'key' not in st.session_state:
    st.session_state['key'] = value
st.write(st.session_state.key)

st.write(st.session_state)

