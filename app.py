import streamlit as st
from multiapp import MultiApp
from apps import steth,home,compare,bluna,beth
# import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.markdown("""
# 
""")

# Add all your application here
app.add_app("home", home.app)
app.add_app("steth", steth.app)
app.add_app("compare", compare.app)
app.add_app("bluna", bluna.app)
app.add_app("beth", beth.app)





# The main app
app.run()