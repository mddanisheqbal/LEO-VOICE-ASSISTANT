# CURRENTLY SPOTIFY CLOSING IS NOT SUPPORTED, BUT OPENING IT IS
# CURRENTLY CLOSING CONTROL PANEL IS NOT SUPPORTED, BUT OPENING IT IS

import tkinter as tk
from tkinter import scrolledtext, messagebox
import speech_recognition as sr
import pyttsx3
import subprocess
import os
import sys
import threading
import datetime
import time
import pyautogui
import random
import socket
import webbrowser
import platform # For operating system info
import getpass # For username
import string # For password generation
import pyperclip # For clipboard operations (if you want to add copy/paste later)
import psutil 
import shutil
import json # New import for handling JSON API responses
import asyncio # New import for async operations if needed, though threading used here



recognizer = sr.Recognizer()
engine_lock = threading.Lock() 

def open_application(app_name):
    print(f"[OPEN_APP] Attempting to open application: '{app_name}'")
    app_name_lower = app_name.lower()
    if sys.platform.startswith('win'):
        print(f"[OPEN_APP] Detected Windows OS. Checking common Windows apps.")
        try:
            if 'notepad' in app_name_lower:
                print("[OPEN_APP] Matched 'notepad'. Executing 'notepad.exe'.")
                subprocess.Popen(['notepad.exe'])
                return True
            
            elif 'word' in app_name_lower:
                print("[OPEN_APP] Matched 'word'. Executing 'WINWORD.EXE' using os.startfile.")
                os.startfile('WINWORD.EXE')
                return True
            
            elif 'excel' in app_name_lower:
                print("[OPEN_APP] Matched 'excel'. Executing 'EXCEL.EXE' using os.startfile.")
                os.startfile('EXCEL.EXE')
                return True
            
            elif 'powerpoint' in app_name_lower:
                print("[OPEN_APP] Matched 'powerpoint'. Executing 'POWERPNT.EXE' using os.startfile.")
                os.startfile('POWERPNT.EXE')
                print("[OPEN_APP DEBUG] os.startfile for PowerPoint executed. Attempting return True.") # NEW DEBUG PRINT
                return True
            
            
            elif 'chrome' in app_name_lower:
                print("[OPEN_APP] Matched 'chrome'. Executing 'chrome.exe'.")
                subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
                return True
            elif 'edge' in app_name_lower or 'microsoft edge' in app_name_lower:
                print("[OPEN_APP] Matched 'edge'. Executing 'msedge.exe'.")
                subprocess.Popen(['msedge.exe'])
                return True
            
            elif 'youtube' in app_name_lower:
                print("[OPEN_APP] Matched 'youtube'. Executing 'https://www.youtube.com' in web browser.")
                webbrowser.open_new_tab('https://www.youtube.com')
                return True
            
            elif 'brave' in app_name_lower:
                print("[OPEN_APP] Matched 'brave'. Executing 'brave.exe'.")
                subprocess.Popen(['brave.exe'])
                return True
            
            elif 'firefox' in app_name_lower:
                print("[OPEN_APP] Matched 'firefox'. Executing 'firefox.exe'.")
                subprocess.Popen(['firefox.exe'])
                return True
            
            elif 'calculator' in app_name_lower:
                print("[OPEN_APP] Matched 'calculator'. Executing 'calc.exe'.")
                subprocess.Popen(['calc.exe'])
                return True
            
            elif 'paint' in app_name_lower:
                print("[OPEN_APP] Matched 'paint'. Executing 'mspaint.exe'.")
                subprocess.Popen(['mspaint.exe'])
                return True
            
            elif 'cmd' in app_name_lower or 'command prompt' in app_name_lower:
                print("[OPEN_APP] Matched 'cmd'/'command prompt'. Executing 'start cmd.exe' with shell=True.")
                subprocess.Popen(['start', 'cmd.exe'], shell=True) 
                return True
            
            elif 'setting' in app_name_lower:
                print("[OPEN_APP] Matched 'settings'. Executing 'ms-settings:' using os.startfile.")
                os.startfile('ms-settings:')
                return True
            
            # RIGHT NOW CLOSING TASK MANAGER IS NOT SUPPORTED, BUT OPENING IT IS
            elif 'task manager' in app_name_lower:
                print("[OPEN_APP] Matched 'task manager'. Executing 'Taskmgr.exe' using os.startfile.")
                os.startfile('Taskmgr.exe')
                return True
            
            elif 'file explorer' in app_name_lower or 'explorer' in app_name_lower or 'file manager' in app_name_lower:
                print("[OPEN_APP] Matched 'file explorer'. Executing 'explorer.exe' using os.startfile.")
                os.startfile('explorer.exe')
                return True
            
            elif 'control panel' in app_name_lower:
                print("[OPEN_APP] Matched 'control panel'. Executing 'control.exe' using os.startfile.")
                os.startfile('control.exe')
                return True
            
            elif 'notepad++' in app_name_lower:
                print("[OPEN_APP] Matched 'notepad++'. Executing 'notepad++.exe' using os.startfile.")
                os.startfile('notepad++.exe')
                return True
            
            elif 'vlc' in app_name_lower or 'video player' in app_name_lower or 'vlc media player' in app_name_lower:
                print("[OPEN_APP] Matched 'vlc'. Executing 'vlc.exe' using os.startfile.")
                os.startfile('vlc.exe')
                return True
            
            elif 'spotify' in app_name_lower:
                spotify_profile_url = 'https://open.spotify.com/?flow_ctx=2d594cce-d37e-401a-8d12-52333a28ca09%3A1752605460'
                print(f"[OPEN_APP] Matched 'spotify'. Opening specific Spotify profile URL: {spotify_profile_url}")
                webbrowser.open_new_tab(spotify_profile_url)
                print("[OPEN_APP DEBUG] webbrowser.open_new_tab for Spotify profile executed. Attempting return True.")
                return True
            
            elif 'zoom' in app_name_lower:
                print("[OPEN_APP] Matched 'zoom'. Attempting to open Zoom Desktop App via URI scheme 'zoommtg:'.")
                try: 
                    os.startfile('zoommtg:')
                    print("[OPEN_APP DEBUG] os.startfile for Zoom URI executed. Attempting return True.")
                    return True
                except Exception as uri_e: 
                    print(f"[OPEN_APP ERROR] Failed to open Zoom via URI scheme: {uri_e}. Falling back to Zoom.exe.")
                    try: 
                        os.startfile('Zoom.exe')
                        print("[OPEN_APP DEBUG] os.startfile for Zoom.exe executed. Attempting return True.")
                        return True
                    except FileNotFoundError:
                        print(f"[OPEN_APP ERROR] Zoom.exe not found in PATH for direct execution. Trying explicit path.")
                        zoom_exe_path = None 

                        if zoom_exe_path and os.path.exists(zoom_exe_path):
                            subprocess.Popen([zoom_exe_path])
                            print(f"[OPEN_APP DEBUG] Zoom opened from explicit path: {zoom_exe_path}. Attempting return True.")
                            return True
                        else:
                            print(f"[OPEN_APP ERROR] Explicit Zoom path not set or file not found at: {zoom_exe_path}")
                            return False
                        
                
            
            
            
        except FileNotFoundError:
            print(f"[OPEN_APP ERROR] Executable for '{app_name}' not found in PATH. Check if app is installed or path is correct.")
            return False
        
        except Exception as e:
            print(f"[OPEN_APP ERROR] An unexpected error occurred while trying to open '{app_name}': {e}")
            return False
        
    return False

def close_application(app_name):
    """
    Attempts to close an application. This is a best-effort, forceful close
    and may result in unsaved data loss.
    """
    app_name_lower = app_name.lower()
    command = []
    process_found = False

    if sys.platform.startswith('win'):
        if 'notepad' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'notepad.exe']
            process_found = True
        elif 'word' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'winword.exe']
            process_found = True
        elif 'excel' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'excel.exe']
            process_found = True
        elif 'powerpoint' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'powerpnt.exe']
            process_found = True
        elif 'chrome' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'chrome.exe']
            process_found = True
            
        elif 'edge' in app_name_lower or 'microsoft edge' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'msedge.exe']
            process_found = True
            
        elif 'youtube' in app_name_lower:
            print("[CLOSE_APP] YouTube is a website, not an application. Cannot close.")
            return True, "YouTube is a website, not an application. Cannot close."
        
        elif 'brave' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'brave.exe']
            process_found = True
            
        elif 'firefox' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'firefox.exe']
            process_found = True
            
        elif 'calculator' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'CalculatorApp.exe']
            process_found = True
            
        elif 'paint' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'mspaint.exe']
            process_found = True
            
        elif 'cmd' in app_name_lower or 'command prompt' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'cmd.exe'] 
            process_found = True
            
        elif 'setting' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'SystemSettings.exe']
            process_found = True
            
        elif 'task manager' in app_name_lower:
            print("[CLOSE_APP] Task Manager cannot be closed using taskkill. Please close it manually.")
            return True, "Task Manager cannot be closed using taskkill. Please close it manually."  
        
        elif 'file explorer' in app_name_lower or 'explorer' in app_name_lower or 'file manager' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'explorer.exe']
            process_found = True    
            
        # CURRENTLY CLOSING CONTROL PANEL IS NOT SUPPORTED, BUT OPENING IT IS
        elif 'control panel' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'control.exe']
            process_found = True
            
        elif 'notepad++' in app_name_lower: 
            command = ['taskkill', '/f', '/im', 'notepad++.exe']
            process_found = True
            
        elif 'vlc' in app_name_lower or 'video player' in app_name_lower or 'vlc media player' in app_name_lower:
            command = ['taskkill', '/f', '/im', 'vlc.exe']
            process_found = True
            
            
        # CURRENTLY SPOTIFY CLOSING IS NOT SUPPORTED, BUT OPENING IT IS 
        elif 'spotify' in app_name_lower: # This is the block you asked about
            command = ['taskkill', '/f', '/im', 'Spotify.exe']
            process_found = True
            
        elif 'zoom' in app_name_lower: # This is the block for Zoom
            command = ['taskkill', '/f', '/im', 'Zoom.exe']
            process_found = True
            
            

    if process_found and command:
        try:
            print(f"[CLOSE_APP] Attempting to execute close command: {command}")
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            if result.returncode == 0:
                print(f"[CLOSE_APP] Close command successful for '{app_name}'.")
                return True, f"Successfully attempted to close {app_name}."
            
            else:
                print(f"[CLOSE_APP ERROR] Close command failed for '{app_name}'. Return code: {result.returncode}, Stderr: {result.stderr.strip()}")
                return False, f"Could not close {app_name}. Error: {result.stderr.strip()}"
            
        except Exception as e:
            print(f"[CLOSE_APP ERROR] An error occurred while trying to close {app_name}: {e}")
            return False, f"An error occurred while trying to close {app_name}: {e}"
        
    print(f"[CLOSE_APP] No matching close command found for '{app_name}'.")
    return False, f"I don't know how to close {app_name}."

# --- Jarvis Application Class ---

class JarvisApp:
    def __init__(self, master):
        print("[INIT] JarvisApp __init__ started.")
        self.master = master
        master.title("LEO AI Assistant")
        master.geometry("900x700")
        master.resizable(True, True)
        master.config(bg="#1a202c") # Dark background

        self.listening_for_command = False 
        self.current_wake_word = "jarvis" 
        self.listening_thread = None
        self.stop_listening_event = threading.Event() 

        self.setup_gui()
        print("[INIT] Calling initial speak.")
        self.speak(f"Hello, I am leo. How can I assist you today?")
        print("[INIT] JarvisApp __init__ finished.")

    def setup_gui(self):
        print("[SETUP_GUI] GUI setup started.")
        # Header
        header_frame = tk.Frame(self.master, bg="#1a202c")
        header_frame.pack(pady=20)
        tk.Label(header_frame, text="LEO AI Assistant", font=("Inter", 30, "bold"), fg="#63b3ed", bg="#1a202c").pack()

        # Display Area
        self.display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, state='disabled',
                                                 font=("Inter", 12),
                                                 fg="#a0aec0", bg="#1a202c",
                                                 insertbackground="#63b3ed", selectbackground="#4a5568",
                                                 height=12, relief="flat", bd=0)
        self.display.tag_config('user', foreground='#90CDF4', font=("Inter", 12, "bold"))
        self.display.tag_config('jarvis', foreground='#63B3ED', font=("Inter", 12, "bold"))
        self.display.pack(padx=25, pady=15, fill=tk.BOTH, expand=True)

        # Input and Buttons Frame
        input_frame = tk.Frame(self.master, bg="#2a3342", bd=0, relief="solid", padx=20, pady=20)
        input_frame.pack(fill=tk.X, padx=25, pady=10)

        # Command Input
        self.command_input = tk.Entry(input_frame, font=("Inter", 12), fg="#e2e8f0", bg="#1a202c",
                                      insertbackground="#63b3ed", relief="flat", bd=1, highlightbackground="#4a5568", highlightthickness=1)
        self.command_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.command_input.bind("<Return>", self.send_command_from_entry)

        send_btn = tk.Button(input_frame, text="Send Command", command=self.send_command_from_entry,
                             font=("Inter", 10, "bold"), bg="#63b3ed", fg="#1a202c",
                             activebackground="#4299e1", activeforeground="#1a202c",
                             relief="flat", bd=0, padx=10, pady=5)
        send_btn.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        # Action Buttons Frame
        action_buttons_frame = tk.Frame(input_frame, bg="#2a3342")
        action_buttons_frame.grid(row=1, column=0, columnspan=3, pady=10)

        self.start_btn = tk.Button(action_buttons_frame, text="Start Listening", command=self.start_listening,
                                   font=("Inter", 10, "bold"), bg="#63b3ed", fg="#1a202c",
                                   activebackground="#4299e1", activeforeground="#1a202c",
                                   relief="flat", bd=0, padx=10, pady=5)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(action_buttons_frame, text="Stop Listening", command=self.stop_listening,
                                  font=("Inter", 10, "bold"), bg="#4a5568", fg="#e2e8f0",
                                  activebackground="#2d3748", activeforeground="#e2e8f0",
                                  relief="flat", bd=0, padx=10, pady=5, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(action_buttons_frame, text="Clear Display", command=self.clear_display,
                              font=("Inter", 10, "bold"), bg="#4a5568", fg="#e2e8f0",
                              activebackground="#2d3748", activeforeground="#e2e8f0",
                              relief="flat", bd=0, padx=10, pady=5)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # Status Message
        self.status_label = tk.Label(input_frame, text=f"Ready for command. Waiting for '{self.current_wake_word}'.", font=("Inter", 10), fg="#a0aec0", bg="#2a3342")
        self.status_label.grid(row=2, column=0, columnspan=3, pady=5)

        input_frame.grid_columnconfigure(0, weight=1) 

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        print("[SETUP_GUI] GUI setup finished.")


    def on_closing(self):
        """Handle window closing event to stop listening thread."""
        print("[ON_CLOSING] Window closing initiated.")
        self.stop_listening_event.set() 
        if self.listening_thread and self.listening_thread.is_alive():
            print("[ON_CLOSING] Waiting for listening thread to join.")
            self.listening_thread.join(timeout=2) 
        self.master.destroy()
        print("[ON_CLOSING] Master destroyed.")


    def display_message(self, sender, message):
        self.display.config(state='normal')
        self.display.insert(tk.END, f"{sender}: ", sender.lower())
        self.display.insert(tk.END, f"{message}\n", 'default')
        self.display.see(tk.END) # Scroll to bottom
        self.display.config(state='disabled')

    def speak(self, text):
        print(f"[SPEAK] Attempting to speak: '{text}'")
        def _speak_thread():
            with engine_lock: # Ensure only one TTS call at a time
                engine_instance = None
                try:
                    print(f"[SPEAK_THREAD] Initializing pyttsx3 engine for text: '{text}'")
                    engine_instance = pyttsx3.init() 

                    # Attempt to set a specific voice (Microsoft Zira Desktop)
                    zira_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"

                    voices = engine_instance.getProperty('voices')
                    found_zira = False
                    for voice in voices:
                        if voice.id == zira_voice_id:
                            engine_instance.setProperty('voice', voice.id)
                            found_zira = True
                            print(f"[SPEAK_THREAD] Set voice to: {voice.name}")
                            break
                    if not found_zira:
                        print(f"[SPEAK_THREAD] Zira voice not found, using default voice: {engine_instance.getProperty('voice')}")

                    time.sleep(0.1) # Small delay before speaking
                    engine_instance.say(text)
                    engine_instance.runAndWait()
                    time.sleep(0.1) # Small delay after speaking
                    print(f"[SPEAK_THREAD] Finished speaking: '{text}'")
                    
                except Exception as e:
                    print(f"[SPEAK_THREAD ERROR] Failed to speak '{text}': {e}")
                    print("Please check your audio output, volume, and system's speech engine configuration.")
                    
                finally:
                    if engine_instance:
                        try:
                            engine_instance.stop() # Stop any ongoing speech
                            engine_instance.quit() # Crucial: Quit the engine instance
                            print(f"[SPEAK_THREAD] Engine instance quit for '{text}'")
                        except Exception as e_quit:
                            print(f"[SPEAK_THREAD ERROR] Error quitting engine instance: {e_quit}")

        threading.Thread(target=_speak_thread).start()

    def start_listening(self):
        print("[START_LISTENING] Attempting to start listening.")
        if self.listening_thread and self.listening_thread.is_alive():
            self.master.after(0, lambda: self.status_label.config(text="Already listening."))
            print("[START_LISTENING] Already listening, returning.")
            return

        self.stop_listening_event.clear() 
        self.listening_for_command = False 
        self.master.after(0, lambda: self.status_label.config(text=f"Listening... Waiting for '{self.current_wake_word}'."))
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

        self.listening_thread = threading.Thread(target=self._listen_loop)
        self.listening_thread.daemon = True 
        self.listening_thread.start()
        print("[START_LISTENING] Listening thread started.")

    def stop_listening(self):
        print("[STOP_LISTENING] Attempting to stop listening.")
        self.stop_listening_event.set() 
        if self.listening_thread and self.listening_thread.is_alive():
            print("[STOP_LISTENING] Waiting for listening thread to join.")
            self.listening_thread.join(timeout=2) 
        self.listening_thread = None
        self.listening_for_command = False 
        self.master.after(0, lambda: self.status_label.config(text="Speech recognition stopped."))
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        print("[STOP_LISTENING] Listening stopped.")

    def _listen_loop(self):
        print("[_LISTEN_LOOP] Listener thread started.")
        with sr.Microphone() as source:
            print("[_LISTEN_LOOP] Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[_LISTEN_LOOP] Ambient noise adjustment complete.")
            self.master.after(0, lambda: self.status_label.config(text=f"Listening... Waiting for '{self.current_wake_word}'."))
            print(f"[_LISTEN_LOOP] Entering wake word mode. Waiting for '{self.current_wake_word}'.")

            while not self.stop_listening_event.is_set():
                if not self.listening_for_command:
                    try:
                        self.master.after(0, lambda: self.status_label.config(text=f"Listening for wake word '{self.current_wake_word}'..."))
                        print(f"[_LISTEN_LOOP] Currently in wake word phase. Listening for '{self.current_wake_word}'...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        wake_phrase = recognizer.recognize_google(audio).lower()
                        print(f"[_LISTEN_LOOP] Heard (wake word phase): '{wake_phrase}'")

                        if self.current_wake_word in wake_phrase:
                            self.listening_for_command = True
                            self.master.after(0, lambda: self.status_label.config(text=f"Wake word detected! Listening for command..."))
                            self.speak("Yes mister daanish?") 
                            time.sleep(2.0) # Short delay to allow user to prepare for command
                            print("[_LISTEN_LOOP] Wake word detected. Transitioning to command phase.")
                    
                        else:
                            print(f"[_LISTEN_LOOP] Wake word '{self.current_wake_word}' not detected. Staying in wake word phase.")
                            pass

                    except sr.WaitTimeoutError:
                        print("[_LISTEN_LOOP] No speech detected in wake word phase (timeout).")
                        pass
                    
                    except sr.UnknownValueError:
                        print("[_LISTEN_LOOP] Could not understand audio in wake word phase.")
                        pass
                    
                    except sr.RequestError as e:
                        self.master.after(0, lambda: self.status_label.config(text=f"Speech service error; {e}"))
                        self.master.after(0, self.speak, f"I'm having trouble connecting to the speech service. Please check your internet connection.")
                        self.stop_listening_event.set() 
                        print(f"[_LISTEN_LOOP ERROR] Speech service error: {e}. Stopping listener.")
                        break
                    
                    except Exception as e:
                        self.master.after(0, lambda: self.status_label.config(text=f"An error occurred in wake word phase: {e}"))
                        self.master.after(0, self.speak, "An unexpected error occurred in wake word detection. Please try again.")
                        self.stop_listening_event.set() 
                        print(f"[_LISTEN_LOOP ERROR] Unexpected error in wake word phase: {e}. Stopping listener.")
                        break
                else:
                    try:
                        self.master.after(0, lambda: self.status_label.config(text="Listening for your command..."))
                        print("[_LISTEN_LOOP] Currently in command phase. Listening for command...")
                        audio = recognizer.listen(source, timeout=7, phrase_time_limit=7) 
                        command = recognizer.recognize_google(audio)
                        print(f"[_LISTEN_LOOP] Heard (command phase): '{command}'")
                        self.master.after(0, self.process_command, command)
                        self.master.after(0, self.command_input.delete, 0, tk.END)
                        self.master.after(0, self.command_input.insert, 0, command)
                        self.listening_for_command = False # Go back to wake word mode after command
                        self.master.after(0, lambda: self.status_label.config(text=f"Processed command. Waiting for '{self.current_wake_word}'."))
                        print(f"[_LISTEN_LOOP] Command processed. Transitioning back to wake word mode. Waiting for '{self.current_wake_word}'.")

                    except sr.WaitTimeoutError:
                        self.master.after(0, lambda: self.status_label.config(text=f"No command detected. Waiting for '{self.current_wake_word}'."))
                        self.speak("Command timed out. Waiting for your next instruction.")
                        self.listening_for_command = False # Go back to wake word mode
                        print("[_LISTEN_LOOP] No command detected (timeout). Returning to wake word mode.")
                    except sr.UnknownValueError:
                        self.master.after(0, lambda: self.status_label.config(text=f"Could not understand command. Waiting for '{self.current_wake_word}'."))
                        self.speak("I could not understand that command. Please try again.")
                        self.listening_for_command = False # Go back to wake word mode
                        print("[_LISTEN_LOOP] Could not understand command. Returning to wake word mode.")
                    except sr.RequestError as e:
                        self.master.after(0, lambda: self.status_label.config(text=f"Speech service error; {e}"))
                        self.master.after(0, self.speak, f"I'm having trouble connecting to the speech service. Please check your internet connection.")
                        self.stop_listening_event.set() 
                        print(f"[_LISTEN_LOOP ERROR] Speech service error: {e}. Stopping listener.")
                        break
                    except Exception as e:
                        self.master.after(0, lambda: self.status_label.config(text=f"An error occurred in command phase: {e}"))
                        self.master.after(0, self.speak, "An unexpected error occurred during command processing. Please try again.")
                        self.stop_listening_event.set() 
                        print(f"[_LISTEN_LOOP ERROR] Unexpected error in command phase: {e}. Stopping listener.")
                        break
            self.master.after(0, lambda: self.status_label.config(text="Speech recognition stopped.")) # Final state if loop exits
            print("[_LISTEN_LOOP] Listening loop ended.")


    def send_command_from_entry(self, event=None):
        command = self.command_input.get().strip()
        if command:
            print(f"[TEXT_COMMAND] Processing text command: '{command}'")
            self.stop_listening_event.set() 
            if self.listening_thread and self.listening_thread.is_alive():
                 print("[TEXT_COMMAND] Waiting for listening thread to join after text command.")
                 self.listening_thread.join(timeout=1)
            self.process_command(command)
            self.command_input.delete(0, tk.END)
            print("[TEXT_COMMAND] Restarting listening after text command.")
            self.master.after(100, self.start_listening) 


    def process_command(self, command):
        self.display_message("User", command)
        lower_command = command.lower()
        response = ""

        self.status_label.config(text="Jarvis is thinking...")
        
        if lower_command.startswith(self.current_wake_word + " "):
            lower_command = lower_command.replace(self.current_wake_word + " ", "", 1).strip()
            print(f"[PROCESS_COMMAND] Wake word stripped. New lower_command: '{lower_command}'")
        elif lower_command == self.current_wake_word:
            # If only wake word was spoken/typed, prompt for command
            response = "Yes, mister daanish, what is your command?"
            self.display_message("Jarvis", response)
            self.speak(response)
            self.status_label.config(text=f"Ready for command. Waiting for '{self.current_wake_word}'.")
            return 

        print(f"[PROCESS_COMMAND] Final command for processing: '{lower_command}'") 

        if "hello" in lower_command or "hi" in lower_command:
            response = "Hello there! How can I assist you today?"
            
        elif "how are you" in lower_command:
            response = "I am good, thank you for asking! How can I help you today?"
        
        elif "what is your name" in lower_command:
            response = "I am Leo, your AI assistant. How can I assist you today?"
        
        elif "who is your creator" in lower_command or "who created you" in lower_command or "who made you" in lower_command or "who developed you" in lower_command:
            response = "I was created by Mister Daanish. He is a talented developer and I am here to assist you both."
            
        elif "what can you do" in lower_command or "what are your capabilities" in lower_command:
            response = ("I can assist you with various tasks such as:\n"
                        "- Answering questions\n"
                        "- Providing information\n"
                        "- Opening applications\n"
                        "- Taking screenshots\n"
                        "- Setting timers\n"
                        "- Playing music or videos on YouTube\n"
                        "- Searching the web\n"
                        "- And much more! Just ask and I'll do my best to help.")
            
        elif "time" in lower_command or "what time is it" in lower_command or "what is the current time" in lower_command:
            now = datetime.datetime.now()
            response = f"The current time is {now.strftime('%I:%M %p')}."
            
        elif "date" in lower_command or "today's date" in lower_command or "what is the date" in lower_command:
            now = datetime.datetime.now()
            response = f"Today's date is {now.strftime('%A, %B %d, %Y')}."
            
        elif "weather" in lower_command:
            response = "I currently do not have access to real-time weather data. Please check a weather website or app for the latest updates."
            
        elif lower_command.startswith("search ") and "on google" in lower_command:
            query = lower_command.replace("search ", "").replace(" on google", "").strip()
            if query:
                try:
                    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
                    response = f"Searching Google for {query}."
                except Exception as e:
                    response = f"Sorry, I couldn't open the web browser. Error: {e}"
            else:
                response = "Please tell me what you want to search on Google."
                
        elif lower_command.startswith("open website "):
            url = lower_command.replace("open website ", "").strip()
            if url:
                if not (url.startswith("http://") or url.startswith("https://")):
                    url = "http://" + url
                try:
                    webbrowser.open_new_tab(url)
                    response = f"Opening {url}."
                except Exception as e:
                    response = f"Sorry, I couldn't open that website. Error: {e}"
            else:
                response = "Please provide a website URL to open."
        # elif lower_command.startswith("play ") and "on youtube" in lower_command:
        #     query = lower_command.replace("play ", "").replace(" on youtube", "").strip()
        #     if query:
        #         try:
        #             webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
        #             response = f"Searching YouTube for {query}."
        #         except Exception as e:
        #             response = f"Sorry, I couldn't open YouTube. Error: {e}"
        #     else:
        #         response = "Please tell me what you want to play on YouTube."
        elif lower_command.startswith("search ") and "on youtube" in lower_command: # NEW COMMAND for explicit search 
            query = lower_command.replace("search ", "").replace(" on youtube", "").strip()
            if query:
                try:
                    webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
                    response = f"Searching YouTube for {query}."
                except Exception as e:
                    response = f"Sorry, I couldn't open YouTube. Error: {e}"
            else:
                response = "Please tell me what you want to search on YouTube." 
                      
        elif "minimize all windows" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    pyautogui.hotkey('win', 'd')
                    response = "All windows minimized."
                except Exception as e:
                    response = f"Sorry, I couldn't minimize windows. Make sure PyAutoGUI is installed and has necessary permissions. Error: {e}"
            else:
                response = "This command is currently only supported on Windows."
                
        elif "take a screenshot" in lower_command:
            try:
                screenshot_filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pyautogui.screenshot(screenshot_filename)
                response = f"Screenshot saved as {screenshot_filename}."
            except Exception as e:
                response = f"Sorry, I couldn't take a screenshot. Make sure PyAutoGUI is installed and has necessary permissions. Error: {e}"
    
        elif "flip a coin" in lower_command:
            response = f"It's {random.choice(['Heads', 'Tails'])}!"
            
        elif "roll a die" in lower_command or "roll a dice" in lower_command:
            response = f"You rolled a {random.randint(1, 6)}."
            
        elif lower_command.startswith("set a timer for "):
            parts = lower_command.replace("set a timer for ", "").strip().split()
            if len(parts) == 2:
                try:
                    value = int(parts[0])
                    unit = parts[1]
                    duration_seconds = 0
                    if "minute" in unit:
                        duration_seconds = value * 60
                        response = f"Setting a timer for {value} minute{'s' if value != 1 else ''}."
                    elif "second" in unit:
                        duration_seconds = value
                        response = f"Setting a timer for {value} second{'s' if value != 1 else ''}."
                    else:
                        response = "I can only set timers in minutes or seconds. Please specify, for example, 'set a timer for 5 minutes'."

                    if duration_seconds > 0:
                        self.display_message("Jarvis", response) # Display immediately
                        self.speak(response) # Speak immediately
                        # Start timer in a new thread
                        threading.Timer(duration_seconds, self._timer_finished, [value, unit]).start()
                        return # Exit process_command to avoid default response
                except ValueError:
                    response = "I didn't understand the timer duration. Please say a number, like 'set a timer for 5 minutes'."
            else:
                response = "Please specify the timer duration. For example, 'set a timer for 5 minutes'."
                
        elif "what is my local ip address" in lower_command:
            try:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                response = f"Your local IP address is {ip_address}."
            except Exception as e:
                response = f"Sorry, I couldn't find your local IP address. Error: {e}"
            
        elif "what is my computer name" in lower_command or "what is my device name" in lower_command:
            try:
                computer_name = socket.gethostname()
                response = f"Your computer name is HP Omen 16."
            except Exception as e:
                response = f"Sorry, I couldn't find your computer name. Error: {e}"
            
            
        elif "what is my operating system" in lower_command:
            response = f"You are running {platform.system()} {platform.release()}."
            
        elif "what is my username" in lower_command:
            try:
                username = getpass.getuser()
                response = f"Your username is {username}."
            except Exception as e:
                response = f"Sorry, I couldn't retrieve your username. Error: {e}"
                
                
        elif lower_command.startswith("create a folder ") or lower_command.startswith("create folder ") or lower_command.startswith("make a folder "): 
            # Example: "create a folder My New Folder in C:\Users\Public"
            # Example: "create a folder My Docs in Desktop"

            parts = lower_command.split(" in ")
            if len(parts) < 2:
                response = "Please specify both the folder name and the location. For example, 'create a folder My Documents in Desktop'."
            else:
                folder_name_part = parts[0].replace("create a folder ", "").strip()
                raw_target_path = parts[1].strip()

                if not folder_name_part:
                    response = "Please provide a name for the folder."
                elif not raw_target_path:
                    response = "Please specify the location where you want to create the folder."
                else:
                    # Resolve common special paths
                    target_path_lower = raw_target_path.lower()
                    resolved_path = ""

                    if target_path_lower == "desktop":
                        resolved_path = os.path.join(os.path.expanduser('~'), 'Desktop')
                    elif target_path_lower == "documents":
                        resolved_path = os.path.join(os.path.expanduser('~'), 'Documents')
                    elif target_path_lower == "downloads":
                        resolved_path = os.path.join(os.path.expanduser('~'), 'Downloads')
                    elif sys.platform.startswith('win') and (target_path_lower.endswith(" drive") or target_path_lower.endswith(":\\")):
                        # Handle "C drive" -> "C:\" or "C:\" directly
                        if target_path_lower.endswith(" drive"):
                            drive_letter = target_path_lower[0].upper()
                            resolved_path = f"{drive_letter}:\\"
                        else: # Already "C:\" etc.
                            resolved_path = raw_target_path.upper() # Keep original casing for direct path if it's already a drive letter
                    else:
                        # Assume it's a direct path provided by the user
                        resolved_path = raw_target_path

                    # Construct the full path for the new folder
                    full_new_folder_path = os.path.join(resolved_path, folder_name_part)

                    try:
                        os.makedirs(full_new_folder_path, exist_ok=True)
                        response = f"Folder '{folder_name_part}' created successfully at '{resolved_path}'."
                    except OSError as e:
                        if e.errno == 13: # Permission denied
                            response = f"Permission denied. I cannot create the folder at '{resolved_path}'. Please ensure Jarvis is running as an administrator and you have write access to that location."
                        elif e.errno == 2: # No such file or directory (path doesn't exist)
                            response = f"The path '{resolved_path}' does not exist. Please provide a valid existing location."
                        else:
                            response = f"Sorry, I couldn't create the folder. An unexpected error occurred: {e}"
                    except Exception as e:
                        response = f"Sorry, I couldn't create the folder. An unexpected error occurred: {e}"
                        
                        
                        
        elif lower_command.startswith("search ") and "on wikipedia" in lower_command:
            query = lower_command.replace("search ", "").replace(" on wikipedia", "").strip()
            if query:
                try:
                    webbrowser.open_new_tab(f"https://en.wikipedia.org/wiki/Special:Search?search={query}")
                    response = f"Searching Wikipedia for {query}."
                except Exception as e:
                    response = f"Sorry, I couldn't open Wikipedia. Error: {e}"
            else:
                response = "Please tell me what you want to search on Wikipedia."
        elif "show me news" in lower_command or "open news" in lower_command:
            try:
                webbrowser.open_new_tab("https://news.google.com/") # Or your preferred news site
                response = "Opening Google News."
            except Exception as e:
                response = f"Sorry, I couldn't open the news website. Error: {e}"
        elif lower_command.startswith("generate a password"):
            try:
                parts = lower_command.split()
                length = 12 # Default length
                if "long" in parts:
                    try:
                        length_index = parts.index("long") - 1
                        length = int(parts[length_index])
                    except (ValueError, IndexError):
                        pass # Use default length if not specified correctly
                elif len(parts) > 3 and parts[-2].isdigit(): # e.g., "password 12"
                    length = int(parts[-2])

                if length < 6: # Minimum reasonable password length
                    length = 6
                    response = "Password length too short, generating a 6-character password."

                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for i in range(length))
                response = f"Here is a password for you: {password}"
            except Exception as e:
                response = f"Sorry, I couldn't generate a password. Error: {e}"
        elif "open device manager" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    subprocess.Popen(['devmgmt.msc'])
                    response = "Opening Device Manager."
                except Exception as e:
                    response = f"Sorry, I couldn't open Device Manager. Error: {e}"
            else:
                response = "This command is only available on Windows."
        elif "open services" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    subprocess.Popen(['services.msc'])
                    response = "Opening Services."
                except Exception as e:
                    response = f"Sorry, I couldn't open Services. Error: {e}"
            else:
                response = "This command is only available on Windows."
        elif "shutdown computer" in lower_command or "restart computer" in lower_command:
            action = "shutdown" if "shutdown" in lower_command else "restart"
            confirm = messagebox.askyesno("Confirm System Action", f"Are you sure you want to {action} your computer? Any unsaved work will be lost.")
            if confirm:
                if sys.platform.startswith('win'):
                    try:
                        if action == "shutdown":
                            subprocess.Popen(['shutdown', '/s', '/t', '1']) # /s for shutdown, /t 1 for 1 second delay
                            response = "Shutting down your computer."
                        else:
                            subprocess.Popen(['shutdown', '/r', '/t', '1']) # /r for restart
                            response = "Restarting your computer."
                    except Exception as e:
                        response = f"Sorry, I couldn't {action} your computer. Error: {e}"

            else:
                response = f"Okay, I will not {action} your computer."
        
        
        elif "sleep computer" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    # FIX: Use pyautogui to simulate Win+X, U, S for reliable sleep
                    pyautogui.hotkey('win', 'x')
                    time.sleep(0.1) # Give time for the menu to appear
                    pyautogui.press('u')
                    time.sleep(0.1) # Give time for the submenu to appear
                    pyautogui.press('s')
                    response = "Putting your computer to sleep."
                except Exception as e:
                    response = f"Sorry, I couldn't put your computer to sleep. Error: {e}. Ensure PyAutoGUI is installed and has necessary permissions."
        
            else:
                response = "I cannot put this computer to sleep on this operating system."
                
                
        elif lower_command.startswith("copy ") and "to clipboard" in lower_command:
            text_to_copy = lower_command.replace("copy ", "").replace(" to clipboard", "").strip()
            if text_to_copy:
                try:
                    pyperclip.copy(text_to_copy)
                    response = f"Copied '{text_to_copy}' to clipboard."
                except Exception as e:
                    response = f"Sorry, I couldn't copy to clipboard. Error: {e}"
            else:
                response = "Please tell me what text you want to copy to the clipboard."
        elif "paste from clipboard" in lower_command or "read clipboard" in lower_command:
            try:
                clipboard_content = pyperclip.paste()
                if clipboard_content:
                    response = f"The clipboard contains: '{clipboard_content}'."
                else:
                    response = "The clipboard is empty."
            except Exception as e:
                response = f"Sorry, I couldn't read from clipboard. Error: {e}"
        elif "what is my cpu usage" in lower_command:
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                response = f"Your CPU usage is currently {cpu_percent:.1f} percent."
            except Exception as e:
                response = f"Sorry, I couldn't get CPU usage. Error: {e}"
        elif "what is my ram usage" in lower_command or "what is my memory usage" in lower_command:
            try:
                ram = psutil.virtual_memory()
                total_gb = ram.total / (1024**3)
                used_gb = ram.used / (1024**3)
                percent_used = ram.percent
                response = f"Your RAM usage is {percent_used:.1f} percent. You are using {used_gb:.2f} gigabytes out of {total_gb:.2f} gigabytes."
            except Exception as e:
                response = f"Sorry, I couldn't get RAM usage. Error: {e}"
        elif "lock my computer" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    subprocess.Popen(['rundll32.exe', 'user32.dll,LockWorkStation'])
                    response = "Locking your computer."
                except Exception as e:
                    response = f"Sorry, I couldn't lock your computer. Error: {e}. You might need to run Jarvis as an administrator."
            elif sys.platform.startswith('linux'):
                try:
                    subprocess.Popen(['xdg-screensaver', 'lock'])
                    response = "Locking your computer."
                except Exception as e:
                    response = f"Sorry, I couldn't lock your computer. Error: {e}. You might need to run Jarvis with sudo privileges or install a screen locker."
            elif sys.platform.startswith('darwin'):
                try:
                    subprocess.Popen(['pmset', 'sleepnow'])
                    response = "Locking your computer."
                except Exception as e:
                    response = f"Sorry, I couldn't lock your computer. Error: {e}."
            else:
                response = "I cannot lock the computer on this operating system."
        elif "open display settings" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    os.startfile('ms-settings:display')
                    response = "Opening Display Settings."
                except Exception as e:
                    response = f"Sorry, I couldn't open Display Settings. Error: {e}"
            else:
                response = "This command is only available on Windows."
        elif "open network settings" in lower_command:
            if sys.platform.startswith('win'):
                try:
                    os.startfile('ms-settings:network-status')
                    response = "Opening Network Settings."
                except Exception as e:
                    response = f"Sorry, I couldn't open Network Settings. Error: {e}"
            else:
                response = "This command is only available on Windows."
                
            
                
                
                
                
        
                
        elif lower_command.startswith("open"):
            app_to_open = lower_command.replace("open ", "").strip()
            print(f"[PROCESS_COMMAND] Attempting to open: '{app_to_open}'") 
            if open_application(app_to_open):
                response = f"Opening {app_to_open}."
            else:
                response = f"I cannot find or open '{app_to_open}'. Please provide a valid application name or ensure it's in your system's PATH."
                
        elif lower_command.startswith("close"):
            app_to_close = lower_command.replace("close ", "").strip()
            print(f"[PROCESS_COMMAND] Attempting to close: '{app_to_close}'") 
            success, msg = close_application(app_to_close)
            if success:
                response = msg
            else:
                response = f"Could not close {app_to_close}. {msg}"
                if "forcefully" in msg or "method" in msg:
                    response += " Please be aware that forcefully closing applications might lead to unsaved data loss."
        elif "change jarvis to" in lower_command:
            new_wake_word = lower_command.replace("change jarvis to ", "").strip()
            if new_wake_word:
                self.current_wake_word = new_wake_word
                response = f"Understood. My new activation word is now '{self.current_wake_word}'. Please use it to get my attention."
                # Restart listening to apply new wake word immediately
                self.stop_listening()
                self.master.after(500, self.start_listening) # Short delay before restarting
            else:
                response = "Please tell me what you want to change my activation word to. For example, 'change Jarvis to Leo'."
        elif "clear display" in lower_command or "clear screen" in lower_command:
            self.clear_display()
            response = "Display cleared. How may I help you now?"
        elif "stop listening" in lower_command or "stop voice command" in lower_command:
            self.stop_listening()
            response = "Voice recognition stopped."
        elif "exit" in lower_command or "quit" in lower_command:
            response = "Goodbye! I am shutting down."
            self.speak(response)
            self.master.after(2000, self.master.destroy) 
            return
        else:
            response = "I am sorry, I do not understand that command yet. Please try again."

        self.display_message("Jarvis", response)
        self.speak(response)
        self.status_label.config(text=f"Ready for command. Waiting for '{self.current_wake_word}'.")

    def clear_display(self):
        self.display.config(state='normal')
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, f"Hello, I am {self.current_wake_word}. How can I assist you today?\n", 'jarvis')
        self.display.config(state='disabled')
        self.speak("Display cleared.")




if __name__ == "__main__":
    print("[MAIN] Script started.")
    root = tk.Tk()
    app = JarvisApp(root)
    print("[MAIN] Entering Tkinter mainloop.")
    root.mainloop()
    print("[MAIN] Tkinter mainloop exited.")