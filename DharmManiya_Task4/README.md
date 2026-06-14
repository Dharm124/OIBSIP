# SMS Spam Detection

This project is developed as **Task 4** of my Oasis Infobyte Data Science Internship.

The application classifies SMS messages as **Spam** or **Ham** using Natural Language Processing and Machine Learning. A Streamlit interface allows users to enter a message and receive an instant prediction.

---

## Project Workflow

```text
User enters an SMS message
        ↓
Text preprocessing
        ↓
TF-IDF vectorization
        ↓
Multinomial Naive Bayes model
        ↓
Spam or Ham prediction
```

---

## Text Preprocessing

The input message is processed using the following steps:

1. Convert text to lowercase
2. Tokenize the sentence into words
3. Remove non-alphanumeric characters
4. Remove English stop words and punctuation
5. Apply stemming using `PorterStemmer`
6. Join the processed words into a cleaned sentence

---

## Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Streamlit
* Jupyter Notebook

---

## Machine Learning Model

The project uses:

* `TfidfVectorizer` to convert processed text into numerical features
* `MultinomialNB` to classify the message as spam or ham

---

## Project Structure

```text
DharmManiya_Task4/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── sms-spam-detection.ipynb
├── requirements.txt
└── README.md
```

| File                       | Description                                   |
| -------------------------- | --------------------------------------------- |
| `app.py`                   | Streamlit web application                     |
| `model.pkl`                | Saved trained classification model            |
| `vectorizer.pkl`           | Saved TF-IDF vectorizer                       |
| `sms-spam-detection.ipynb` | Complete model training and analysis notebook |
| `requirements.txt`         | Required Python packages                      |

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Open the project folder:

```bash
cd DharmManiya_Task4
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Requirements

```text
streamlit
nltk
pickle
string
sklearn
```

---

## Example

### Input

```text
Congratulations! You have won a free cash prize. Claim now.
```

### Output

```text
🚨This is a spam message.
```

### Input

```text
I will reach college at 10 AM tomorrow.
```

### Output

```text
✅This is a ham message.
```

---

## Author

**Dharm Maniya**
