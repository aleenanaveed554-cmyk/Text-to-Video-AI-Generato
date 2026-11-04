
import streamlit as st
import replicate
import time

st.set_page_config(
    page_title="Text to Video AI",
    page_icon="🎬",
    layout="wide"
)

# API Configuration
st.title("🎬 Text to Video AI")
st.markdown(
    "<h3 style='text-align:center;color:#a78bfa;'>"
    "Turn Your Imagination Into Videos ✨"
    "</h3>",
    unsafe_allow_html=True
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10102b, #242052, #40145c);
    color: white;
}
h1 {
    text-align: center;
    color: #ffffff;
    font-size: 45px;
}
.stTextArea textarea {
    background-color: #ffffff;
    color: #111111;
    border-radius: 12px;
}
.stButton button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    border: none;
    border-radius: 12px;
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.write("")
st.subheader("✨ Create Your AI Video")

prompt = st.text_area(
    "Describe your video",
    placeholder="Example: A beautiful futuristic city with flying cars, glowing buildings and colorful lights...",
    height=150
)

st.info("💡 Write a detailed prompt for better results.")

col1, col2 = st.columns(2)

with col1:
    aspect = st.selectbox(
        "Video Style",
        ["16:9 Landscape", "9:16 Portrait"]
    )

with col2:
    quality = st.selectbox(
        "Prompt Enhancement",
        ["Enabled", "Disabled"]
    )

st.write("")

if st.button("🚀 Generate AI Video"):

    if not prompt.strip():
        st.warning("Please enter a video description.")

    else:
        try:
            token = st.secrets["REPLICATE_API_TOKEN"]

            with st.spinner("Creating your AI video... Please wait! 🎥"):

                output = replicate.run(
                    "minimax/video-01",
                    input={
                        "prompt": prompt,
                        "prompt_optimizer": quality == "Enabled"
                    }
                )

                video_url = output.url()

            st.success("Your video is ready! 🎉")

            st.video(video_url)

            st.link_button(
                "⬇️ Download Video",
                video_url
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:#c4b5fd;'>"
    "Made with ❤️ using Python & Generative AI"
    "</p>",
    unsafe_allow_html=True
)
