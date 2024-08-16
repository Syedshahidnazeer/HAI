import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests
import yaml
import time

# Set up Gemini AI (you'll need to add your API key)
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)


GEMINI_AI_API_KEY = config['gemini_api_key']
genai.configure(api_key=GEMINI_AI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def humanize_text(input_text):
    prompt = f"""
    Hey there! 👋 I've got a fun challenge for you. You know how sometimes AI-written text can sound a bit... well, robotic? We're gonna fix that!

    I've got a piece of text here that's screaming for a personal touch. Your mission, should you choose to accept it (and I know you will!), is to work your magic and transform it into something that sounds like it came straight from the fingertips of a real, coffee-fueled human.

    Here's what I'm thinking:
    - Keep the main points and meaning intact - we don't want to lose the essence!
    - Sprinkle in some casual phrases, you know, the kind you'd use when chatting with a friend over lunch.
    - Maybe throw in a rhetorical question or two? People love those!
    - If you can slide in a relatable analogy or a touch of humor, even better!

    Basically, make it sound like it was written by someone who binges Netflix, occasionally forgets their keys, and has strong opinions about pineapple on pizza.

    Here's the text that needs your human touch:
    {input_text}

    Alright, time to work your magic! Show me what you've got, and let's make this text so human-like that it'll be asking for a coffee break by the end of it! 😉
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="HAI - Humanize AI Content", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: black; /* Changed to black for better visibility */
    }

    /* Responsive Styles */
    @media (max-width: 768px) { /* Adjust breakpoint as needed */
        .stApp {
            background-size: cover; /* Cover background on smaller screens */
        }
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            padding: 8px; /* Reduce padding for smaller screens */
        }
        .stButton>button {
            padding: 8px 15px; /* Adjust padding for smaller buttons */
        }
    }

    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: black; /* Changed to black for better visibility */
    }
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.1);
        color: black; /* Changed to black for better visibility */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .user-quote {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("💡 Writing Tips")
    tips_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jR229r.json")
    st.lottie(tips_lottie, key="tips_lottie", height=200)
    st.write("""
    1. Use contractions (e.g., "don't" instead of "do not")
    2. Incorporate casual phrases and idioms
    3. Vary sentence length and structure
    4. Add personal anecdotes or examples
    5. Include rhetorical questions
    6. Use emotive language where appropriate
    """)

    st.markdown("""
    ---
    ### 🌟 Discover More
    For more insights and to see my work in action, visit my portfolio site: [https://syed-shahid-nazeer-portfolio.streamlit.app/#education]
    I look forward to connecting with you and exploring new opportunities together!
    """)

# Main content
st.title("HAI: Humanize AI-Generated Content")
st.write("Transform robotic AI text into natural, conversational language.")

col1, col2 = st.columns([2, 1])

with col1:
    input_text = st.text_area("Paste your AI-generated text here:", height=200)
    if st.button("✨ Humanize"):
        if input_text:
            with st.spinner("Transforming your text..."):
                # Simulating processing time with a progress bar
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                humanized_text = humanize_text(input_text)
            st.success("Transformation complete!")
            st.subheader("🎉 Humanized Result:")
            st.write(humanized_text)
        else:
            st.warning("Please enter some text to humanize.")

with col2:
    main_lottie_url = "https://assets5.lottiefiles.com/packages/lf20_kq5rGs.json"
    main_lottie_animation = load_lottieurl(main_lottie_url)
    st_lottie(main_lottie_animation, key="main_lottie", height=300)

st.markdown("""
---
### How it works
1. Paste your AI-generated text in the input box.
2. Click the "✨ Humanize" button.
3. Our advanced AI will transform the text to sound more natural and human-like.
4. Review the humanized version and use it in your communications!

Perfect for HR professionals, content creators, and anyone looking to add a human touch to AI-generated text.
""")

# Testimonials
st.subheader("What our users say")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="user-quote">"HAI turned my robotic job descriptions into warm, inviting narratives!" - Sarah, HR Manager</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="user-quote">"My blog posts now sound like they\'re written by a real person, not a bot!" - Sameer Khan, Content Creator</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="user-quote">"This tool is a game-changer for our customer communications." - Lisa, Marketing Director</div>', unsafe_allow_html=True)

# Call to Action
st.markdown("---")
st.header("Ready to humanize your content?")
st.button("Get Started Now!", key="cta_button")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by AI Enthusiast SYED SHAHID NAZEER")