import streamlit as st
st.title("hello Raghuram")      #title
st.header("Hello")              #heaader
st.subheader("Hello")
st.markdown("# HI")
st.markdown("## HI")
st.markdown("### HI")
st.markdown("#### HI")
st.text("my name is raghuram")
st.success('successful')

st.error("erroe")
st.info('information')
st.exception(ZeroDivisionError('div not possible with 0'))
st.write('zebronics')
st.write(range(1,10))
st.text(range(1,10))
st.code(' x = 10 \n '
        'for i in range(x): \n'
            '\tprint(i) ')
if(st.checkbox('male')):
    st.write('you are male')
    
Radio = st.radio('Gender: ',('male','female'))
if(Radio == 'male'):
    st.write('your are male')
elif(Radio == 'female'):
    st.write('your are female')

st.header('button')
if(st.button('click me')):
    st.write('THANKS')


st.header('select box')
select = st.selectbox('Data science : ' , ['Data analysis','Image processing' ,
                                   'web scraping' ,'machine learning' , 
                                   'deep leanring','computer vision'] )
st.write(select)
st.header("Multiselect")

multi = st.multiselect('Data science : ' , ['Data analysis','Image processing' ,
                                   'web scraping' ,'machine learning' , 
                                   'deep leanring','computer vision'])
st.write(multi,len(multi))
st.header('Slider')
vol = st.slider('volume',1,100)
st.write(vol)

st.header("Text Input")
name = st.text_input("Name")
if(name):
    st.write("HI",name)

st.header("Text Area")
Textarea = st.text_area("Define yourself")
if(Textarea):
    st.write(Textarea)
st.header("Number  Input")
age = st.number_input('Age: ', 18,100)
if(age):
    st.write(age)
st.header("Date Input")
st.date_input('Birthdate')
st.header("Time input")
st.time_input('Time')