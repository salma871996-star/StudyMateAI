import re
import requests
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

# 2. تصميم الخلفية والتنسيق (Blue to Green Gradient)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364, #11998e, #38ef7d);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #ffffff;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    [data-testid="stSidebar"] {
        background-color: rgba(15, 32, 39, 0.85);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stButton>button {
        background: linear-gradient(90deg, #11998e, #38ef7d);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. إعدادات رابط الـ API والمفتاح السرّي
API_URL = " API URL "
API_KEY = " API KEY "
headers = {"Authorization": f"Bearer {API_KEY}"}

# 4. الشريط الجانبي (Sidebar)
with st.sidebar:
    try:
        st.image("studymate.png", use_container_width=True)
    except Exception:
        pass
    
    st.markdown("""
        <div style="text-align: center; padding: 5px 0 15px 0;">
            <h1 style="font-family: sans-serif; font-size: 28px; font-weight: 800; margin: 0;">
                <span style="color: #0A49A8;">Study</span><span style="color: #72D02B;">Mate AI</span>
            </h1>
            <p style="color: #72D02B; font-size: 11px; margin-top: 2px; font-weight: 600;">
                Your Intelligent Academic Companion
            </p>
        </div>
    """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    feature = st.radio(
        "Choose Feature:",
        ["📤 Upload PDF", "💬 Chat", "📝 Summary", "🧩 Quiz", "📌 Notes", "📅 Study Planner"],
        key="main_navigation"
    )

# العنوان الرئيسي أعلى الصفحة
st.markdown("""
    <h1 style="font-family: sans-serif; font-size: 40px; font-weight: 800; margin-bottom: 0;">
        <span style="color: #0A49A8;">Study</span><span style="color: #72D02B;">Mate AI</span>
    </h1>
""", unsafe_allow_html=True)
st.caption("Your Intelligent Academic Companion")

# 5. منطق واجهات الميزات المختلفة

if feature == "📤 Upload PDF":
    st.header("Upload Lecture PDF")
    uploaded_pdf = st.file_uploader("Select a PDF file", type=["pdf"])
    
    if uploaded_pdf and st.button("Process Document"):
        with st.spinner("Uploading and processing PDF..."):
            files = {"file": (uploaded_pdf.name, uploaded_pdf.getvalue(), "application/pdf")}
            res = requests.post(f"{API_URL}/upload", headers=headers, files=files)
            
            if res.ok:
                st.success("PDF uploaded and processed successfully!")
            else:
                st.error(f"Error: {res.text}")

elif feature == "💬 Chat":
    st.header("Ask Questions About Your Lecture")
    question = st.text_input("Enter your question:")
    
    if question and st.button("Send Question"):
        with st.spinner("Generating answer..."):
            res = requests.post(f"{API_URL}/chat", headers=headers, json={"question": question})
            if res.ok:
                st.subheader("Answer:")
                st.write(res.json().get("answer"))
            else:
                st.error("Failed to fetch answer. Make sure a PDF is uploaded first.")

elif feature == "📝 Summary":
    st.header("Lecture Summary")
    if st.button("Generate Summary"):
        with st.spinner("Summarizing lecture..."):
            res = requests.post(f"{API_URL}/summary", headers=headers)
            if res.ok:
                st.markdown(res.json().get("summary"))
            else:
                st.error("Error generating summary.")

elif feature == "🧩 Quiz":
    st.header("Generate Practice Quiz")

    num_q = st.slider(
        "Number of Questions",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Create Quiz"):
        with st.spinner("Creating quiz questions..."):
            res = requests.post(
                f"{API_URL}/quiz",
                headers=headers,
                json={"num_questions": num_q}
            )

            if res.ok:
                quiz_text = res.json().get("quiz", "")

                # 1. فصل الأسئلة بناءً على بداية الأرقام (مثل: 1. أو 2.)
                # يضمن هذا التقسيم عدم تداخل الأسئلة حتى لو كانت في سطر واحد
                raw_questions = re.split(r'(?=\b\d+\.\s)', quiz_text)
                questions = [q.strip() for q in raw_questions if q.strip()]

                for q_block in questions:
                    # 2. استخراج الإجابة الخاصة بالسؤال إن وجدت داخل كتلته (Answer: X)
                    answer_text = ""
                    if "Answer:" in q_block:
                        q_body, answer_part = q_block.split("Answer:", 1)
                        # نأخذ فقط حرف الإجابة الأول أو السطر الأول للإجابة
                        answer_text = answer_part.strip().split("\n")[0]
                    else:
                        q_body = q_block

                    # 3. تنسيق الاختيارات (A, B, C, D) لتصبح كل منها في سطر منفصل
                    formatted_q = re.sub(
                        r'\s*([A-D][\.\)-])\s*', 
                        r'\n\n**\1** ', 
                        q_body
                    )

                    # 4. عرض السؤال
                    st.markdown(formatted_q.strip())

                    # 5. عرض الإجابة الخاصة بهذا السؤال فقط
                    if answer_text:
                        with st.expander("🔍 Reveal Answer"):
                            st.success(f"Correct Answer: {answer_text}")

                    st.markdown("---")

            else:
                st.error("Error generating quiz.")

elif feature == "📌 Notes":
    st.header("Detailed Lecture Notes")
    if st.button("Generate Notes"):
        with st.spinner("Extracting structured notes..."):
            res = requests.post(f"{API_URL}/notes", headers=headers)
            if res.ok:
                st.markdown(res.json().get("notes"))
            else:
                st.error("Error generating notes.")

 
elif feature == "📅 Study Planner":
    st.header("Personalized Study Plan")
    col1, col2 = st.columns(2)
    with col1:
        days = st.number_input("Study Duration (Days)", min_value=1, max_value=30, value=7)
    with col2:
        hours = st.number_input("Hours per Day", min_value=1, max_value=12, value=3)
        
    if st.button("Generate Plan"):
        with st.spinner("Creating study schedule..."):
            payload = {"days": days, "hours_per_day": hours}
            res = requests.post(f"{API_URL}/planner", headers=headers, json=payload)
            if res.ok:
                st.markdown(res.json().get("plan"))
            else:
                st.error("Error generating plan.")
