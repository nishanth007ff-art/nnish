import streamlit as st
import pandas as pd

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Student Manager",
    page_icon="🎓",
    layout="centered"
)

# ---------------------------
# Demo Login Credentials
# ---------------------------
USERNAME = "admin"
PASSWORD = "1234"

# ---------------------------
# Session State
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "students" not in st.session_state:
    st.session_state.students = []

# ---------------------------
# Login Page
# ---------------------------
def login_page():
    st.title("🎓 Student Management System")
    st.subheader("🔐 Login")

    with st.form("login_form"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")

        if login:
            if user == USERNAME and pwd == PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

# ---------------------------
# Main App
# ---------------------------
def main_app():
    st.title("🎓 Student Management Dashboard")

    # Logout
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    students = st.session_state.students

    # ---------------------------
    # Sidebar - Add Student
    # ---------------------------
    st.sidebar.header("➕ Add Student")

    with st.sidebar.form("add_student"):
        name = st.text_input("Student Name")
        roll = st.text_input("Roll Number")
        dept = st.text_input("Department")

        st.markdown("**Enter Marks**")
        m1 = st.number_input("Maths", 0, 100, 0)
        m2 = st.number_input("Physics", 0, 100, 0)
        m3 = st.number_input("Computer", 0, 100, 0)

        add = st.form_submit_button("Add Student")

        if add:
            if name and roll and dept:
                total = m1 + m2 + m3
                avg = round(total / 3, 2)

                students.append({
                    "Name": name,
                    "Roll": roll,
                    "Department": dept,
                    "Maths": m1,
                    "Physics": m2,
                    "Computer": m3,
                    "Total": total,
                    "Average": avg
                })

                st.sidebar.success("Student added successfully")
            else:
                st.sidebar.warning("Please fill all details")

    # ---------------------------
    # Search Students
    # ---------------------------
    st.subheader("🔍 Search Students")
    search = st.text_input("Search by Name / Roll / Department")

    if students:
        df = pd.DataFrame(students)

        if search:
            df = df[
                df["Name"].str.contains(search, case=False) |
                df["Roll"].str.contains(search, case=False) |
                df["Department"].str.contains(search, case=False)
            ]

        st.dataframe(df, use_container_width=True)
    else:
        st.info("No students added yet")

    # ---------------------------
    # Delete Student
    # ---------------------------
    st.subheader("🗑️ Delete Student")

    if students:
        roll_list = [s["Roll"] for s in students]
        roll_del = st.selectbox("Select Roll Number", roll_list)

        if st.button("Delete"):
            st.session_state.students = [
                s for s in students if s["Roll"] != roll_del
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
