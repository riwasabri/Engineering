import streamlit as st
import pickle
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


#Loading data_frame
books = pickle.load(open('data.pkl' , 'rb'))
books_list = books['title'].values
st.image('https://i0.wp.com/thebashfulbookworm.com/wp-content/uploads/2021/05/Goodreads-2.png?w=1140&ssl=1')
st.title('Meet your next favorite book.')
selected_book_name=st.selectbox('Type in a book that you love',books_list)
similarity = pickle.load(open('similarity.pkl' , 'rb'))
def recommend(book):
    index = books[books['title'] == book].index[0]
    similar_books = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)[1:6]

    recommended_books = []
    recommended_books_poster = []
    for i in similar_books:

        recommended_books.append(books.iloc[i[0]].title)
    return recommended_books

def remove_first(genre):
    return str(genre)[1:len(genre)]
books['genre']=books['genre'].apply(lambda x:remove_first(x))
if st.button('Show me something similar'):
    st.subheader('We think you will like:')
    names = recommend(selected_book_name)


    st.subheader(names[0])
    col1, col2 = st.columns(2)
    col1.image(str(books[books['title']==names[0]]['img'].values[0]))
    col2.markdown('Genre:')
    col2.caption(str(books[books['title']==names[0]]['genre'].values[0]).replace(',',', ') )
    col2.markdown('Author:')
    col2.caption(books[books['title'] == names[0]]['author'].values[0])
    col2.markdown('Average Rating: ')
    col2.caption(str(books[books['title'] == names[0]]['rating'].values[0]))

    #st.image(str(books[books['title']==names[0]]['img'].values[0]))

    st.subheader(names[1])
    col1, col2 = st.columns(2)
    col1.image(str(books[books['title'] == names[1]]['img'].values[0]))
    col2.markdown('Genre:')
    col2.caption(str(books[books['title'] == names[1]]['genre'].values[0]).replace(',', ', '))
    col2.markdown('Author:')
    col2.caption(books[books['title'] == names[1]]['author'].values[0])
    col2.markdown('Average Rating: ')
    col2.caption(str(books[books['title'] == names[1]]['rating'].values[0]))


    st.subheader(names[2])
    col1, col2 = st.columns(2)
    col1, col2 = st.columns(2)
    col1.image(str(books[books['title'] == names[2]]['img'].values[0]))
    col2.markdown('Genre:')
    col2.caption(str(books[books['title'] == names[2]]['genre'].values[0]).replace(',', ', '))
    col2.markdown('Author:')
    col2.caption(books[books['title'] == names[2]]['author'].values[0])
    col2.markdown('Average Rating: ')
    col2.caption(str(books[books['title'] == names[2]]['rating'].values[0]))

