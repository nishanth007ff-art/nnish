import streamlit as st
import pandas as pd

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Student Manager",
    page_icon="🎓",
    layout="centered"
)

# ---------------------------
# Login credentials (demo)
# ---------------------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

# ---------------------------
# Session state init
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "students" not in st.session_state:
    st.session_state.students = []

# ---------------------------
# Login Page
# ---------------------------
def login_page():
    st.title("🔐 Login")
    st.caption("Student Management System")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")

# ---------------------------
# Main App
# ---------------------------
def main_app():
    st.title("🎓 Student Management System")

    # Logout
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    students = st.session_state.students

    # -----------------------
    # Add Student (Sidebar)
    # -----------------------
    st.sidebar.header("➕ Add Student")

    with st.sidebar.form("add_form"):
        name = st.text_input("Student Name")
        roll = st.text_input("Roll Number")
        dept = st.text_input("Department")
        add_btn = st.form_submit_button("Add")

        if add_btn:
            if name and roll and dept:
                students.append({
                    "Name": name,
                    "Roll": roll,
                    "Department": dept
                })
                st.sidebar.success("Student added")
            else:
                st.sidebar.warning("Fill all fields")

    # -----------------------
    # Search Section
    # -----------------------
    st.subheader("🔍 Search Students")

    search_term = st.text_input("Search by Name / Roll / Department")

    if students:
        df = pd.DataFrame(students)

        if search_term:
            df = df[
                df["Name"].str.contains(search_term, case=False) |
                df["Roll"].str.contains(search_term, case=False) |
                df["Department"].str.contains(search_term, case=False)
            ]

        st.dataframe(df, use_container_width=True)
    else:
        st.info("No students added yet.")

    # -----------------------
    # Delete Student
    # -----------------------
    st.subheader("🗑️ Delete Student")

    if students:
        rolls = [s["Roll"] for s in students]
        roll_to_delete = st.selectbox("Select Roll", rolls)

        if st.button("Delete Student"):
            st.session_state.students = [
                s for s in students if s["Roll"] != roll_to_delete
            ]
            st.success("Student deleted")
            st.rerun()

# ---------------------------
# App Router
# ---------------------------
if st.session_state.logged_in:
    main_app()
else:
    login_page()
