import streamlit as st
import markdown
import codecs

# Streamlitアプリのタイトル
st.title('Markdown Viewer')

# ファイルアップローダーを作成
uploaded_file = st.file_uploader("Choose a Markdown file", type=["md"])

if uploaded_file is not None:
    # アップロードされたファイルを読み込む
    stringio = codecs.iterdecode(uploaded_file, 'utf-8')
    content = ''.join(stringio)

    # MarkdownをHTMLに変換
    html_content = markdown.markdown(content)

    # HTMLコンテンツを表示
    st.markdown(html_content, unsafe_allow_html=True)
else:
    st.write("Please upload a Markdown file.")
