import fitz  # PyMuPDF
import streamlit as st
import os

def view_pdf(file_path, notes, bookmark):
    doc = fitz.open(file_path)
    st.subheader("📖 PDF Reader")

    page_number = st.number_input("Go to page:", min_value=1, max_value=len(doc), step=1)

    page = doc[int(page_number)-1]
    image = page.get_pixmap()
    st.image(image.tobytes("png"))

    # Notes
    with st.expander("📝 Add/View Notes"):
        current_note = notes.get(str(page_number), "")
        new_note = st.text_area("Note for this page:", value=current_note)
        if st.button("Save Note"):
            notes[str(page_number)] = new_note
            st.success("Note saved!")

    # Bookmark
    if st.button("🔖 Bookmark this page"):
        bookmark.append(int(page_number))
        st.success(f"Page {page_number} bookmarked!")

    return notes, bookmark
