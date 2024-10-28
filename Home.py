import streamlit as st

def main():
    st.logo("logo.png")

    dummy1, title_col, dummy2 = st.columns([2, 3, 2])
    with title_col:
        st.header("DANIEL KARORI PORTFOLIO")
        st.caption("Data Scientist | Data Engineer")

    col1, col2 = st.columns(2)

    with col1:
        st.write("My name is Daniel Karori. I am a Data scientist by profesion with 2 yrs experience")
        st.write("My name is Daniel Karori. I am a Data scientist by profesion with 2 yrs experience")
        st.write("My name is Daniel Karori. I am a Data scientist by profesion with 2 yrs experience")

    with col2:
        dm1, ac_col1, dm2=st.columns(3)
        with col2:
            st.image("images/me.jpg", width=(500))

    st.subheader("Links")
    column1, column2 = st.columns(2)
    with column1:
        st.write("Github: https://github.com/")
        st.write("LinkedIn: https://github.com/")
        st.write("IG: https://github.com/ ")
    with column2:
        st.write("X: https://github.com/ ")
        st.write("Whatsapp: https://github.com/ ")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Karori Portfolio",
        page_icon= "📝",
        layout= "wide",
        initial_sidebar_state= "expanded"
    )
    main()