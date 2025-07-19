# LEO AI Assistant

LEO is a **voice-activated and text-command AI assistant** for Windows, inspired by Jarvis from Iron Man. It offers hands-free interaction using speech recognition and natural language processing, along with a powerful graphical user interface for easy access to commands and responses.

## Features

- **Wake Word Activation**: Start the assistant via customizable wake word (default: `jarvis`).
- **GUI Built with Tkinter**: Modern, responsive, themable display for conversations and controls.
- **Speech Recognition**: Uses your microphone to recognize voice commands, with text command fallback.
- **Text-to-Speech**: Responds with realistic voice, supporting Windows system voices.
- **Open/Close Applications**: Launch and force-close common Windows apps (Notepad, Chrome, Word, VLC, etc.).
- **Web Search**: Search Google, YouTube, Wikipedia, and open websites by voice or text.
- **System and Device Info**: Query local IP, computer name, OS version, username, CPU and RAM usage.
- **Productivity Tools**: Set timers, take screenshots, generate passwords, coin flip and dice roll.
- **Clipboard Management**: Copy text to clipboard and read clipboard content.
- **File & Folder Operations**: Create folders in common or specified locations.
- **System Controls**: Minimize all windows, open system tools (Task Manager, Device Manager, Services), shutdown/restart/sleep/lock system.
- **Personalization**: Change wake word, clear chat display, stop voice recognition, and safely exit.
- **Extensible & Well-Documented**: Easy to add new commands and extend responses.

## Getting Started

### Prerequisites

- **Python 3.8+** (Windows 10/11 recommended)
- The following packages:
  - `tkinter`
  - `speechrecognition`
  - `pyttsx3`
  - `pyautogui`
  - `psutil`
  - `pyperclip`
  - `pyaudio` *(for microphone access)*
- Internet access (for some web features)
- Administrative access (for certain system actions)

### Install Dependencies

```bash
pip install -r requirements.txt
```

> You may need to install `pyaudio` from a pre-built wheel if you experience issues on Windows.

### Running the Assistant

```bash
python your_script_name.py
```

Upon launch, the GUI appears. You can interact via text input or click **Start Listening** to talk to LEO.

## Usage Overview

- **Wake Word Mode**: Say "jarvis" (or your chosen name) to activate listening for a command.
- **Supported Commands**: Try prompts like:
  - "Open Notepad"
  - "Close Chrome"
  - "What is my local IP address?"
  - "Take a screenshot"
  - "Search Python tutorials on Google"
  - "Set a timer for 3 minutes"
  - "Flip a coin"
  - "Create a folder Test in Desktop"
  - "Shutdown computer"
- **Command Examples** and internal logic are well-commented in the source code for extensibility.

## Screenshots

*(Add screenshots of the GUI and example interactions here)*

## Customization & Extending

- **Change Wake Word**: "Change Jarvis to Leo"
- **Add commands**: Edit `process_command` logic for new tasks.
- **Voice Tuning**: Alter voice settings in the `speak` method (`pyttsx3`).
- **App Support**: Modify `open_application` and `close_application` for new app shortcuts.

## Limitations

- Some actions (closing Spotify, Control Panel, Task Manager) are not supported due to OS restrictions.
- Certain system actions require admin rights.
- Built for Windows – some features may not work on Linux/Mac.

## Contributing

Pull requests welcome! For suggestions or feature requests, open an issue.

## License

MIT License

## Credits

Developed by **Mister Daanish**.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [psutil](https://pypi.org/project/psutil/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [Pyaudio](https://pypi.org/project/PyAudio/)

*For any issues or ideas, please contact the developer or open a GitHub issue!*
CONTANT ON INSTAGRAM :-  mrdanish7782

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/11488167/50485dc8-6ffe-4c3a-968f-57c3ce55bf0e/paste.txt
