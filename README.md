# Assignment-Slave-AI-Agent

This project is an AI-powered assignment generator that creates educational content based on a given topic and academic level. It uses OpenAI's GPT models to generate well-structured assignments, including sections like Title, Introduction, Main Body, Conclusion, and References.

## Features

-   **Dynamic Content Generation**: Creates unique assignments on any topic.
-   **Customizable Academic Level**: Adjusts the complexity and tone for different educational levels (e.g., High School, University).
-   **Structured Output**: Formats the assignment into clear, organized sections.
-   **Error Handling**: Includes logging and error management for robust operation.

## Prerequisites

-   Python 3.7+
-   An OpenAI API key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/POPPY-DL/Assignment-Slave-AI-Agent.git
    cd Assignment-Slave-AI-Agent
    ```

2.  **Install the required packages:**
    ```bash
    pip install openai
    ```

3.  **Set up your OpenAI API Key:**

    To use the assignment generation feature, you need to set your OpenAI API key as an environment variable.

    -   **On macOS/Linux:**
        ```bash
        export OPENAI_API_KEY='your_api_key_here'
        ```
    -   **On Windows:**
        ```powershell
        $env:OPENAI_API_KEY='your_api_key_here'
        ```
    *Replace `your_api_key_here` with your actual OpenAI API key.*

## Usage

The core functionality is provided by the `generate_assignment` function in `ai/generate_assignment.py`. You can use it as a module in your own scripts or run it directly to see an example.

### Example

To generate an assignment, you can run the `generate_assignment.py` script directly from the terminal. This will execute the example usage block within the script.

```bash
python ai/generate_assignment.py
```

This will generate an assignment on the topic "The Impact of Climate Change on Marine Ecosystems" at a "University" level and print the output to the console.

### Integrating into your own script

You can also import and use the function in your own Python scripts like this:

```python
from ai.generate_assignment import generate_assignment

# Define the topic and academic level
topic = "The history of the Roman Empire"
academic_level = "High School"

# Generate the assignment
assignment_content = generate_assignment(topic, academic_level)

# Print or save the content
print(assignment_content)
```