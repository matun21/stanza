import streamlit as st
import stanza

@st.cache_resource
def load_model():
    return stanza.Pipeline('ru', processors='tokenize,lemma')

def lemmatize_text(text, nlp):
    doc = nlp(text)
    return ' '.join([word.lemma for sent in doc.sentences for word in sent.words])

st.title("Мой дорогой лемматизатор(Stanza)")
st.write("Вывод слов в начальную форму")

examples = [
    "Кошек мышек ели капибарочки",
    "Красивых детей воровали бандитики",
    "Не хотите ли сходить со мной на обедик и нас там вкусно накормили бы"
]

selected_example = st.selectbox("", examples)

user_text = st.text_area("", value=selected_example, height=150)

if st.button("Лемматизировать"):
    if user_text.strip():
        nlp = load_model()
        result = lemmatize_text(user_text, nlp)
        st.code(result)
        
        doc = nlp(user_text)
        for sent in doc.sentences:
            for word in sent.words:
                st.write(f"{word.text:15} → {word.lemma:15}")