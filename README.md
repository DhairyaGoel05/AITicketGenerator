# AI Ticket Manager

## Overview
The **AI Ticket Manager** is a customer support ticket processing application built using Streamlit and AI-powered tools. It automates the process of analyzing, classifying, responding, and tracking customer support tickets. The application integrates with Gmail to send automatic replies to users based on AI-generated responses.

## Features
- **Ticket Classification:** Uses AI to classify customer issues into various categories (e.g., billing, technical, etc.).
- **Sentiment Analysis:** Performs sentiment analysis to understand the customer's mood and tone.
- **Auto-Generated Replies:** Generates helpful responses using AI to resolve the customer's issue.
- **Email Integration:** Automatically sends a reply email to the customer through Gmail.
- **Ticket Tracking:** Logs and tracks tickets in a Google Sheets document.

## Tech Stack
- **Streamlit:** Web framework for building the user interface.
- **AI Models:** For ticket classification and sentiment analysis.
- **Gmail API:** For sending email replies.
- **Google Sheets API:** For ticket management and tracking.
- **Dotenv:** To manage environment variables.

## Installation

### Requirements
1. Python 3.x
2. Streamlit
3. Other necessary Python packages can be installed using the following command:

```bash
pip install -r requirements.txt

Environment Variables
Create a .env file in the root directory and add the following variables:
GMAIL_USERNAME=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
SPREADSHEET_ID=your-google-sheet-id
You will need to set up your Gmail app password and obtain the Google Sheets spreadsheet ID.

Usage
Running the Application
To run the app, use the following command in your terminal:
streamlit run app.py

Submitting a Support Ticket
Go to the Submit a Support Ticket page.

Fill out the required details: Name, Email, Issue Type, and Message.

Click Submit Ticket to send the ticket.

Managing Tickets
The main page displays new support tickets.

Each ticket is analyzed using AI, and a response is generated.

The ticket is classified based on sentiment and issue type, and a reply is automatically sent to the customer via Gmail.

Files in the Project
app.py: Main application file that processes and responds to tickets.

register_ticket.py: Ticket submission form where users can submit new support tickets.

tools/: Directory containing helper modules for handling Gmail integration, ticket processing, and Google Sheets management.

Screenshots
AI Ticket Manager Dashboard
![Screenshot 2025-04-28 133156](https://github.com/user-attachments/assets/b0ddd6ff-fc07-4e80-be13-3e5a15513a99)

![Screenshot 2025-04-28 133215](https://github.com/user-attachments/assets/e09e4905-3fce-45c0-832f-5fafb8f67821)

![Screenshot 2025-04-28 133318](https://github.com/user-attachments/assets/dcab2a96-0d91-4098-8345-7160a88d8016)

![Screenshot 2025-04-28 133345](https://github.com/user-attachments/assets/133bb56e-9d58-43e5-90eb-1b68e5b52618)

![image](https://github.com/user-attachments/assets/1a9eff77-7420-40a3-82fa-c09ca318cfa6)


Submit a Support Ticket Page

Ticket Response View

<!-- Add your screenshot images to the screenshots directory --> <!-- Replace the file names with actual image files you upload -->
Contributing
Feel free to fork this repository and create pull requests. We welcome contributions!

License
This project is licensed under the MIT License.

