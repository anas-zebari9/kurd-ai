import streamlit as st

# سەردێرا پڕۆژەی
st.set_page_config(page_title="پڕۆژێ من یێ ئای ئای", page_icon="🤖")

st.title("🤖 پڕۆژێ من یێ ئای ئای (AI Project)")
st.write("ئەڤە پڕۆژەکا سادە و دەستپێکێ یە بۆ چێکرنا وێبسایتەکێ ئای ئای ب ڕێکا Streamlit.")

# پشکەک بۆ نڤیسینێ
user_input = st.text_input("پسیار یان بابەتێ خۆ ل ڤێرێ بنڤیسە:")

if st.button("نێرین / Submit"):
    if user_input:
        # ل ڤێرە تو دشێی کۆدێن API یێن OpenAI یان هەر مدلەکا تر زێدە بکەی
        st.success(f"پەیاما تە هاتە وەرگرتن: **{user_input}**")
        st.info("ئەڤە تەنێ نموونەیەکە، تو دشێی کۆدێ خۆ ل ڤێرە پتر پێشڤە ببەی!")
    else:
        st.warning("هشکاتیا پسیارێ ڤالایە، هیڤییە تشتەکی بنڤیسە.")