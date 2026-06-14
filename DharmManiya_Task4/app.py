import pickle
import string
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# Required when running on a new system or Streamlit Cloud
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)


# Load saved files
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))


st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)


ps = PorterStemmer()


# Your original preprocessing logic
def transform(text):
    # Convert message to lowercase
    text = text.lower()

    # Split message into tokens
    text = nltk.word_tokenize(text)

    y = []

    # Step 1: Keep only letters and numbers
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # Step 2: Remove stop words and punctuation
    for i in text:
        if (
            i not in stopwords.words("english")
            and i not in string.punctuation
        ):
            y.append(i)

    text = y[:]
    y.clear()

    # Step 3: Apply stemming
    for i in text:
        y.append(ps.stem(i))

    # Convert list back into a string
    return " ".join(y)


st.title("📩 SMS Spam Detector")

input_sms = st.text_input("Enter your message")


if st.button("Predict"):

    if not input_sms.strip():
        st.warning("Please enter a message.")

    else:
        # Step 1: Preprocess
        transformed_message = transform(input_sms)

        # Step 2: Vectorize
        vectorized_message = tfidf.transform([transformed_message])

        # Step 3: Predict
        prediction = model.predict(vectorized_message)[0]

        # Step 4: Display result
        if prediction == 1:
            st.error("🚨 This is a spam message.")
        else:
            st.success("✅ This is a ham message.")