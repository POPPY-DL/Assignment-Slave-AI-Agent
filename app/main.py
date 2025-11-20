import streamlit as st
import sys
import os

# Add the parent directory to the Python path to allow importing from the 'agents' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.generate_assignment import generate_assignment

def main():
    st.title("Assignment Slave AI Agent")
    st.write("This app uses an AI agent to generate assignments based on your input.")

    # Check for OpenAI API Key
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("The OPENAI_API_KEY environment variable is not set. Please set it to use the app.")
        st.stop()

    # Input fields
    topic = st.text_input("Enter the assignment topic:")
    academic_level = st.selectbox(
        "Select the academic level:",
        ("High School", "University", "Postgraduate", "Middle School", "Elementary School")
    )

    # Generate button
    if st.button("Generate Assignment"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating your assignment... Please wait."):
                assignment_content = generate_assignment(topic, academic_level)
            
            st.subheader("Generated Assignment")
            st.markdown(assignment_content)

if __name__ == "__main__":
    main()
