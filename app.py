import streamlit as st
import os

from utils.file_handler import load_library, save_library, save_uploaded_file
from components.pdf_viewer import view_pdf

st.set_page_config(page_title="📚 E-Library Manager", layout="wide")
st.title("📚 E-Library Manager with PDF Reader")

library = load_library()
menu = ["📤 Upload PDF", "📚 My Library"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "📤 Upload PDF":
    st.header("Upload a New PDF")
    uploaded = st.file_uploader("Choose PDF", type="pdf")
    if uploaded:
        filepath = save_uploaded_file(uploaded)
        title = st.text_input("Enter a title:")
        if st.button("Add to Library") and title:
            library[title] = {
                "file": filepath,
                "notes": {},
                "bookmarks": []
            }
            save_library(library)
            st.success(f"{title} added to your library.")

elif choice == "📚 My Library":
    st.header("Your Library")
    if library:
        selected_title = st.selectbox("Choose a file to read", list(library.keys()))
        file_data = library[selected_title]
        file_path = file_data["file"]

        # Show reader
        updated_notes, updated_bookmarks = view_pdf(file_path, file_data["notes"], file_data["bookmarks"])

        # Save any changes
        library[selected_title]["notes"] = updated_notes
        library[selected_title]["bookmarks"] = updated_bookmarks
        save_library(library)

        # Show bookmarks
        if file_data["bookmarks"]:
            st.info(f"🔖 Bookmarked Pages: {sorted(set(file_data['bookmarks']))}")
    else:
        st.warning("No files found. Upload some PDFs first.")
