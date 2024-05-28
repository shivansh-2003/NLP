import streamlit as st
import spacy_streamlit as spt 
import spacy

nlp = spacy.load('en_core_web_sm')

def main():
    st.title("NER APP")
    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Word Tokenization")
        raw = st.text_area("Text to tokenize", 'Enter Text here')
        if st.button('Tokenize'):
            docs = nlp(raw)
            spt.visualize_tokens(docs)
    
    elif choice == 'NER':
        st.subheader("Named Entity Recognition")
        raw = st.text_area("Text to analyze", 'Enter Text here')
        if st.button('Analyze'):
            docs = nlp(raw)
            spt.visualize_ner(docs)

if __name__ == '__main__':
    main()


