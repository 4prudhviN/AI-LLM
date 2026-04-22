# AI Question Answering Script (Groq API)

## Overview

This project is a Python-based AI application that takes a user's question as input, sends it to a Large Language Model (LLM) using the Groq API, and prints the generated response in the terminal.

The script uses the `llama-3.1-8b-instant` model for fast and efficient responses.

---

## Features

* Accepts user input from the command line
* Integrates with Groq's free LLM API
* Fast response generation using LLaMA model
* Error handling for API and network issues
* Clean and structured output

---

## Requirements

* Python 3.8 or higher
* Internet connection
* Groq API key

---

## Installation

1. Clone the repository or download the files

2. Install required dependencies:

pip install requests

---

## Setup

1. Create a free account on Groq:
   https://console.groq.com

2. Generate an API key

3. Open `main.py` and replace:

API_KEY = "YOUR_API_KEY_HERE"

with your actual API key.

---

## Usage

Run the script using:

python main.py

Then enter your question when prompted.

---

## Example

Input:
What is Artificial Intelligence?

Output:
Artificial Intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.

---

## Error Handling

The script handles:

* Invalid API responses
* Network failures
* Empty user input

If an error occurs, a descriptive message will be displayed.

---


