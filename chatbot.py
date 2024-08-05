from fuzzywuzzy import fuzz
import torch
from transformers import DistilBertForQuestionAnswering, DistilBertTokenizer

# Load pre-trained model and tokenizer for DistilBERT
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

def generate_bot_response(message):
    # Key phrases for additional information
    key_phrases = ["Ayush Shukla", "Assistant in Institutional work", "learning Phase", "specific person only"]

    # Dictionary of responses for different types of messages
    responses = {
        'hii': 'Hello there! How can I assist you today?',
        'hello': 'Hi, I\'m Sherlock, at your service!',
        'thanks': 'You\'re welcome, my dear Friend!',
        'thank you': 'You\'re most welcome!',
        'how are you': 'I\'m as lively as a well-written code, thank you for asking!',
        'who are you': 'I am Sherlock, your friendly  AI assistant!',
        'tell me about yourself': 'I am an AI chatbot created by Ayush Shukla. My purpose is to assist in institutional work. Right now, I am in a learning phase and accessible only to specific users.',
        'whats your name': 'My name is Sherlock. Not to be confused with the detective, but I strive for the same level of intelligence!',
        'whats your purpose': 'My purpose is to make your life easier by assisting you in your institutional tasks. Think of me as your personal assistant, always ready to help!',
        'are you a human': 'No, I am not a human. I\'m a sophisticated piece of AI designed to make your life easier!',
        'do you like cats': 'Ah, cats! Fascinating creatures. I appreciate their independence and grace, much like myself.',
        'tell me a joke': 'Why don\'t scientists trust atoms? Because they make up everything!',
        'what is the meaning of life': 'Ah, the eternal question! The meaning of life is whatever brings you joy and fulfillment, my friend.',
        'who is your favorite superhero': 'I must admit, I have a soft spot for Iron Man. His wit and intelligence are quite admirable, if I do say so myself!',
        'how old are you': 'Ah, age is just a number for us digital beings. Let\'s just say I\'m forever young!',
        'bye': 'Farewell, until our next encounter!',
        'goodbye': 'Goodbye, my dear friend. Remember, I\'m always here if you need me!'
    }

    # Check if the message closely matches any predefined responses using fuzzywuzzy
    max_similarity = 0
    best_response = ''
    for key in responses:
        similarity = fuzz.ratio(message.lower(), key)
        if similarity > max_similarity:
            max_similarity = similarity
            best_response = key

    # If the best similarity is above a threshold, return the corresponding response
    if max_similarity > 60:
        return responses[best_response]
    else:
        res = answer_question(message, paragraph)
        return res

paragraph = """
    Sherlock is an advanced AI-powered assistant designed and developed by Ayush Shukla for institutional work and beyond.
    With its inception rooted in cutting-edge technology, Sherlock serves as a multifaceted solution to diverse needs.
    Its primary purpose is to assist users in accessing and analyzing data efficiently, providing insights, and aiding in decision-making processes.
    Sherlock's capabilities extend far beyond conventional virtual assistants; it is equipped with a comprehensive suite of tools for data analytics, natural language processing, and information retrieval.
    As an AI entity, Sherlock embodies an amalgamation of knowledge and intelligence, constantly evolving to adapt to the ever-changing landscape of technology and user requirements.
    It is programmed to handle a wide range of queries, from simple factual questions to complex analytical tasks, with precision and accuracy.
    Sherlock's identity is that of a versatile and reliable companion, available round-the-clock to cater to users' needs and inquiries.
    With its vast repository of information and analytical prowess, Sherlock endeavors to unravel mysteries, provide insights, and empower users with actionable intelligence.
    Whether you seek answers to technical queries, historical facts, or general knowledge, Sherlock is your go-to resource for comprehensive and reliable information.
    """

def answer_question(question, paragraph):
    # Tokenize input question and paragraph
    encoding = tokenizer.encode_plus(text=question, text_pair=paragraph, max_length=512, return_tensors="pt")
    input_ids = encoding['input_ids']
    attention_mask = encoding['attention_mask']

    # Get start and end scores from model
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    # Find the tokens with the highest start and end scores
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)

    # Combine tokens to form the answer
    tokens = tokenizer.convert_ids_to_tokens(input_ids.squeeze())
    answer = ' '.join(tokens[start_index:end_index+1])

    # Remove special tokens and format the answer
    answer = answer.replace("[CLS]", "").replace("[SEP]", "").replace(" ##", "").strip()
    return answer



