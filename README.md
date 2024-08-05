# CAMPUS: AI-Powered College Administrative and Management Platform

CAMPUS is an AI-powered platform designed to revolutionize customer interactions and data analysis across various industries, with a specific focus on college administration and management. The platform leverages DistilBERT for its chatbot functionality and uses fuzzy logic for similarity checks to respond to fixed and frequently asked questions.

## Features

- **Dynamic FAQ Management:** Automates the response to frequently asked questions using AI.
- **Grievance Management:** Efficiently handles and resolves student grievances.
- **LIAS (Linguistic Integrity Assurance System):** Ensures Good Environment while interaction between Authority and Students.
- **Multimodal Chatbot:** Provides assistance through various communication modes.
- **Sherlock Robot:** Further automates tasks and provides advanced data analysis.

## Technology Stack

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI Models:** DistilBERT for chatbot functionality
- **Similarity Check:** Fuzzy logic

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kingknight07/CAMPUS.git
    ```
2. Change to the project directory:
    ```sh
    cd CAMPUS
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the Flask app:
    ```sh
    flask run
    ```

## Usage
 
1. Interact with the chatbot by typing your questions in the input field.
2. The chatbot will respond based on the trained DistilBERT model and fuzzy similarity checks.

## License

This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Author

CAMPUS is developed and maintained by **Ayush Shukla**.

## Acknowledgements

- [DistilBERT](https://huggingface.co/transformers/model_doc/distilbert.html) by Hugging Face
- [Flask](https://flask.palletsprojects.com/)
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

## Contact

For any inquiries, please contact Ayush Shukla at shuklaayush0704@gmail.com.
