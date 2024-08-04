# Hydrogram-bot
This is a template for a [Hydrogram](https://hydrogram.org/) bot using the Pyrogram framework. Follow the steps below to set up and run the bot.

# Prerequisites
  - Python 3.8 or higher
  - MongoDB
  - Telegram account

# Getting Started
1. Clone the Repository 
   Clone this repository to your local machine using:
   
    ```sh
    git clone https://github.com/nuhmanpk/hydrogram-bot.git
    cd hydrogram-bot
    ```
2. Create a Virtual Environment
  Create a virtual environment to manage dependencies:

    ```sh
    python3 -m venv venv
    ```
    Activate the virtual environment:

    On Windows:

      ```sh
      venv\Scripts\activate
      
      ```
    On macOS/Linux:
   
      ```sh
      source venv/bin/activate
      ```
3. Install Dependencies
   Install the required Python packages:
   
     ```sh
     pip install -r requirements.txt
     ```

4. Obtain Required Values
    You need to gather the following values to configure your bot:

      - DATABASE_URL: The URL for your [MongoDB](https://mongodb.com) database.
      - DATABASE_NAME: The name of your [MongoDB](https://mongodb.com) database.
      - BOT_TOKEN: Your bot token from [BotFather](https://t.me/botfather) on Telegram.
      - API_ID: Your API ID from [my.telegram.org](https://my.telegram.org).
      - API_HASH: Your API hash from [my.telegram.org](https://my.telegram.org).


