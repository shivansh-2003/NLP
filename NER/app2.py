import streamlit as st
import spacy_streamlit as spt
import spacy

nlp = spacy.load('en_core_web_sm')

def main():
    st.title("NLP App")

    menu = ['Home', 'NER', 'POS Tagging', 'Dependency Parsing']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Word Tokenization")
        raw_text = st.text_area("Enter text for tokenization", 'Enter Text here')
        uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])
        
        if uploaded_file is not None:
            raw_text = uploaded_file.read().decode("utf-8")
        
        if st.button('Tokenize'):
            if raw_text:
                docs = nlp(raw_text)
                spt.visualize_tokens(docs)
            else:
                st.warning("Please enter text or upload a file to tokenize.")
    
    elif choice == 'NER':
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Enter text for NER", 'Enter Text here')
        uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])
        
        if uploaded_file is not None:
            raw_text = uploaded_file.read().decode("utf-8")
        
        if st.button('Analyze'):
            if raw_text:
                docs = nlp(raw_text)
                spt.visualize_ner(docs)
            else:
                st.warning("Please enter text or upload a file for NER analysis.")
    
    elif choice == 'POS Tagging':
        st.subheader("Part-of-Speech Tagging")
        raw_text = st.text_area("Enter text for POS tagging", 'Enter Text here')
        uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])
        
        if uploaded_file is not None:
            raw_text = uploaded_file.read().decode("utf-8")
        
        if st.button('Tag POS'):
            if raw_text:
                docs = nlp(raw_text)
                spt.visualize_tokens(docs, attrs=["text", "pos_", "tag_"])
            else:
                st.warning("Please enter text or upload a file for POS tagging.")
    
    elif choice == 'Dependency Parsing':
        st.subheader("Dependency Parsing")
        raw_text = st.text_area("Enter text for dependency parsing", 'Enter Text here')
        uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])
        
        if uploaded_file is not None:
            raw_text = uploaded_file.read().decode("utf-8")
        
        if st.button('Parse'):
            if raw_text:
                docs = nlp(raw_text)
                spt.visualize_parser(docs)
            else:
                st.warning("Please enter text or upload a file for dependency parsing.")

if __name__ == '__main__':
    main()
