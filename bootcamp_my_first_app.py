import streamlit as st
st.write('Hello from the Mojix Bootcamp')
result = st.button('Click here')
if result:
    st.write(':smile:')

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.write('Simple but effective tips for every python lovers')

st.image('imagen.jpeg', caption='Photo by Miesha Maiden from Pexels', width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

st.write('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities')

st.write('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

st.write('**1. Walrus operator**')
st.write('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')
st.write('**_Example_**')
code = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
    print(l)''' 
st.code(code,language = 'python')

st.write('**_Output_**')
result = '''3'''
st.code(result,language = 'python')

st.write('**2.Splitting a string**')
st.write('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')
st.write('**_Example_**')
code = '''string = “hello world”
string.split()'''
st.code(code,language = 'python')

st.write('**_Output_**')
result = '''[‘hello’, ‘world’]'''
st.code(result,language= 'python')





