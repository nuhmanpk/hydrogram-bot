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

5. Set Environment Variables
  Create a .env file in the root of your project directory and add the following content:
    ```
    DATABASE_URL=your_mongodb_url
    DATABASE_NAME=your_database_name
    BOT_TOKEN=your_bot_token
    API_ID=your_api_id
    API_HASH=your_api_hash
    ```
    Replace the placeholders (your_mongodb_url, your_database_name, your_bot_token, your_api_id, your_api_hash) with your actual values.


6. Run the Bot
  Finally, run the bot with:
    ```
    python3 main.py
    ```

# Connect to Your VM
1. Install PM2
  Install PM2, a process manager for Node.js applications that can also be used to manage Python     processes:

    ```sh
    sudo npm install pm2 -g
    ```

2. Start the Bot with PM2
  Start your bot using PM2:

    ``sh
    pm2 start python3 --name hydrogram-bot -- main.py
    ``
  To make PM2 start on system boot:

    ``sh
    pm2 startup
    pm2 save
    ``
   
3. Monitor and Manage Your Bot
  You can manage your bot with PM2 using the following commands:

  List running processes:

  ```sh
  pm2 list
  ```
  Stop the bot:

  ```sh
  
  pm2 stop hydrogram-bot
  ```
  Restart the bot:

  ```sh
  pm2 restart hydrogram-bot
  ```
  View logs:

  ```sh
  pm2 logs hydrogram-bot
  ```
