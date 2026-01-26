# Streamlit Teaching Material

## Overview
This repository contains Streamlit teaching materials designed to help juniors learn how to build interactive web applications using Python. The materials include a teaching example (`app.py`) and a hands-on assignment (`StudentManagement.py`).

## Files in this Repository

###  app.py - Teaching Material
This file demonstrates core Streamlit concepts through four progressive sections:
- **Section 1: Basic Input** - Text and number input with button submission
- **Section 2: Static Table** - Displaying hardcoded data in table format
- **Section 3: Session State** - Persistent data storage across reruns
- **Section 4: Bar Chart** - Data visualization with charts

###  Portfolio.py - Student Assignment
A simplified student management system where learners apply concepts from `app.py`:
- Add students with name, roll number, and department
- View all students in a table
- Delete students by roll number
- Uses session_state for data persistence

## Getting Started

### Prerequisites
Make sure you have Python installed on your system.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jeremiah-Jefry/Streamlit.git
   cd Streamlit
   ```

2. **Install required packages**:
   ```bash
   pip install streamlit pandas
   ```

### Running the Applications

**For the teaching material:**
```bash
streamlit run app.py
```

**For the student assignment:**
```bash
streamlit run Portfolio.py
```

Your browser will automatically open to `http://localhost:8501`.

## Learning Path

1. **Start with app.py** - Go through each section to understand:
   - How to create input fields with unique keys
   - The difference between local variables and session_state
   - How to display data in tables and charts

2. **Practice with Portfolio.py** - Apply what you learned:
   - Build a complete CRUD (Create, Read, Delete) application
   - Manage persistent data across user interactions
   - Structure a multi-section Streamlit app

## Key Concepts Covered
- `st.text_input()` and `st.number_input()` for user input
- `st.button()` for triggering actions
- `st.session_state` for maintaining data across reruns
- `st.table()` and `st.dataframe()` for displaying data
- `st.bar_chart()` for data visualization
- Widget keys to avoid duplicate IDs

## Tips for Students
- Always use unique `key` parameters when you have multiple input widgets of the same type
- Initialize `session_state` variables before using them
- Use `st.divider()` to separate different sections visually
- Test your app frequently as you build to catch errors early

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Thanks to the Streamlit community for their support and resources.
