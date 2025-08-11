# Telegram Keylogger

A Python-based keylogger that captures keystrokes and sends them to a specified Telegram chat using a Telegram bot. The keylogger can be controlled remotely via Telegram commands. This version includes improved threading, queue-based buffering, environment variable configuration, and enhanced error handling for robustness.

⚠️ **Disclaimer**: This project is for educational purposes only. Unauthorized keylogging is illegal and unethical. Always obtain explicit consent from all parties before using this software.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Disclaimer](#disclaimer)

## Features
- Captures keystrokes in real-time using the `pynput` library, including special keys.
- Sends keystrokes to a specified Telegram chat in batches via a Telegram bot.
- Supports remote control with `/start` and `/stop` commands to enable or disable keylogging.
- Uses thread-safe queue for keystroke buffering and separate threads for listening and sending.
- Configurable via environment variables for security.
- Comprehensive logging and error handling.

## Prerequisites
- Python 3.7 or higher
- A Telegram account
- A Telegram bot and its token (obtained from [BotFather](https://t.me/BotFather))
- Your Telegram chat ID
- Required Python packages:
  - `pynput`
  - `python-telegram-bot`

## Installation
1. **Clone the repository** (Datrix Labs members only):
   ```bash
   git clone https://github.com/datrixlabs/telegram-keylogger.git
   cd telegram-keylogger
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install pynput python-telegram-bot
   ```

## Configuration
1. **Create a Telegram bot**:
   - Open Telegram and search for `@BotFather`.
   - Send `/start` and then `/newbot` to create a new bot.
   - Follow the instructions to get your `BOT_TOKEN`.

2. **Get your Telegram chat ID**:
   - Send a message to your bot or use a service like `@GetIDsBot` to find your `CHAT_ID`.

3. **Set environment variables**:
   - Export the following environment variables:
     ```bash
     export TELEGRAM_BOT_TOKEN="your_bot_token_here"
     export TELEGRAM_CHAT_ID="your_chat_id_here"
     ```
   - On Windows, use `set` instead of `export`.

   Note: Do not hardcode sensitive information in the script. The script will exit if these variables are not set.

## Usage
1. **Run the keylogger**:
   ```bash
   python keylogger.py
   ```

2. **Control the keylogger**:
   - Send `/start` to the bot to begin capturing keystrokes.
   - Send `/stop` to pause keylogging.

3. Keystrokes will be collected in a queue and sent in batches (up to 10 at a time) to the specified Telegram chat.

## Commands
- `/start`: Enables the keylogger to start capturing keystrokes.
- `/stop`: Disables the keylogger, stopping keystroke capture.

## How It Works
- The script uses the `pynput` library to listen for keyboard events in a dedicated listener thread.
- Keystrokes are added to a thread-safe queue (`Queue`) for buffering.
- A separate sender thread processes the queue, sending batches of up to 10 keystrokes to the Telegram chat.
- Threading events (`Event`) are used to control capture enabling/disabling and shutdown.
- The `python-telegram-bot` library handles Telegram bot interactions, allowing remote control via commands.
- Environment variables are used for configuration to enhance security.
- Logging is configured for info-level messages, with error handling to manage failures gracefully.

## Contributing
Contributions are restricted to Datrix Labs members only, as per the DatrixLabs License v1.0. To contribute:
1. Ensure you are an approved member of the Datrix Labs GitHub organization.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request for review by the organization owner.

All contributions must retain Datrix Labs attribution and comply with the license terms.

## License
This project is licensed under the **DatrixLabs License v1.0**.  
© DatrixLabs 2025. All Rights Reserved.  
- **Allowed**: Use and modification by Datrix Labs members for internal projects, learning, research, or publication under Datrix Labs. Personal non-commercial use by members. Commercial use requires written permission from the organization owner.
- **Not Allowed**: Use, modification, or forking by non-members, commercial use without approval, rebranding, redistribution, or public release outside Datrix Labs without consent.
- **Special Rules**: Only Datrix Labs members may modify the code. All code must retain Datrix Labs attribution. Datrix Labs may audit usage at any time. External contributors must be approved and added to the organization.  
See the [LICENSE](LICENSE) file for full details.

## Author
This specific implementation was developed by:  
**Ronit Paikray**

## Disclaimer
This software is intended for educational and research purposes only. Unauthorized use of keyloggers to capture keystrokes without consent is illegal and unethical. Datrix Labs and the author are not responsible for any misuse of this software.
