import os
import logging
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_assignment(topic: str, academic_level: str) -> str:
    """
    Generates assignment content using a LangChain-powered AI model.

    Args:
        topic: The subject or topic of the assignment.
        academic_level: The academic level for the assignment's tone and complexity.

    Returns:
        A string containing the formatted assignment content.
    """
    try:
        # It's recommended to use environment variables for API keys
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            logging.error("OPENAI_API_KEY environment variable not set.")
            return "Error: OPENAI_API_KEY is not set."

        # Initialize the LangChain chat model
        chat = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=api_key)

        prompt = f"""
        Generate a well-structured assignment about '{topic}' for a '{academic_level}' level.
        The assignment should include the following sections:
        1. Title
        2. Introduction
        3. Main Body (with at least 3-5 paragraphs)
        4. Conclusion
        5. References (at least 2-3 citations)
        """

        logging.info(f"Generating assignment for topic: {topic}, level: {academic_level}")

        messages = [
            SystemMessage(content="You are a helpful assistant that generates academic assignments."),
            HumanMessage(content=prompt)
        ]
        
        response = chat(messages)
        content = response.content
        
        logging.info("Successfully generated assignment content.")
        
        return content

    except Exception as e:
        logging.error(f"An error occurred during assignment generation: {e}")
        return f"Error: Could not generate the assignment. {e}"

if __name__ == '__main__':
    # Example usage:
    # Make sure to set your OPENAI_API_KEY as an environment variable
    # export OPENAI_API_KEY='your_key_here'
    
    example_topic = "The Impact of Climate Change on Marine Ecosystems"
    example_level = "University"
    
    # To run this example, you need to have the OPENAI_API_KEY environment variable set.
    # If you don't have it set, the function will return an error.
    if os.environ.get("OPENAI_API_KEY"):
        print(f"--- Generating example assignment for topic: '{example_topic}' ---")
        assignment_content = generate_assignment(example_topic, example_level)
        print(assignment_content)
    else:
        print("Cannot run example: Please set the OPENAI_API_KEY environment variable.")
