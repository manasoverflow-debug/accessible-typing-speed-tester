# ♿ Accessible Typing Speed Tester

An accessible and user-friendly typing speed testing application designed to make typing practice easier for users with different accessibility needs, including users who rely on screen readers or speech output.

The application provides multiple typing modes, voice assistance, adjustable speech settings, live performance statistics, and accessible controls.

---

## 🚀 Live Demo

🔗 **Live Demo:**  
[Open the Accessible Typing Speed Tester](YOUR_STREAMLIT_APP_LINK_HERE)

---

## 📌 Project Overview

The **Accessible Typing Speed Tester** is a web-based typing practice application developed using Python and Streamlit.

Unlike a traditional typing test, this project focuses on **accessibility and voice-assisted interaction**.

Users can:

- Practice typing using different modes
- Listen to the typing passage using speech output
- Adjust speech speed and volume
- Choose different test durations
- Monitor typing performance in real time
- Pause, resume, replay, finish, and restart tests
- View detailed typing results
- Try another test with a fresh passage
- Use the application with keyboard and screen-reader-friendly controls

The project was designed with accessibility as one of its primary goals.

---

## ✨ Features

### ⌨️ Multiple Typing Modes

The application provides three different typing modes:

#### 1. Normal Mode

A traditional typing test where the complete passage is displayed on the screen.

Available durations:

- 30 seconds
- 60 seconds
- 120 seconds
- Complete Passage

---

#### 2. Voice-Assisted Mode 🔊

The passage can be read aloud using the browser's speech synthesis functionality.

Users can customize:

- Voice
- Speech speed
- Speech volume
- Test duration

Available durations:

- 30 seconds
- 60 seconds
- 120 seconds
- Complete Passage

This mode is especially useful for users who benefit from auditory assistance.

---

#### 3. Word-by-Word Voice Mode 🗣️

A specialized accessibility mode that reads the passage one word at a time.

As the user approaches the end of the current word, the application automatically announces the next word.

Available durations:

- 30 seconds
- 60 seconds

The 30-second test uses a 4-line passage, while the 60-second test uses an 8-line passage.

This mode helps users follow the passage without needing to continuously look at the screen.

---

## 📊 Live Typing Statistics

During the test, users can monitor their performance in real time.

The application tracks:

- Words Per Minute (WPM)
- Accuracy
- Correct Characters
- Incorrect Characters
- Errors
- Correct Words

The statistics update while the user is typing.

---

## 🏆 Results

After completing a test, the application displays a detailed result summary.

Results include:

- Final WPM
- Accuracy
- Correct characters
- Incorrect characters
- Number of errors
- Correct words
- Time taken
- Total typed characters

Users can also start another test immediately.

---

## 🔊 Accessibility Features

Accessibility was a major focus of this project.

The application includes:

- Voice-assisted typing
- Word-by-word speech
- Adjustable speech speed
- Adjustable speech volume
- Keyboard-friendly controls
- Clear interface structure
- Large, readable controls
- High-contrast dark interface
- Live feedback while typing
- Pause and resume functionality
- Replay functionality
- Screen-reader-friendly text content

The goal is to make typing practice more accessible instead of relying only on visual interaction.

---

# 🖥️ Screenshots

## 🏠 Home Page

The home page allows users to select their preferred typing mode and configure the test.

![Accessible Typing Speed Tester Home](screenshot-home.png)

---

## ⌨️ Typing Test

The typing interface displays the selected passage and provides live typing statistics while the user completes the test.

![Accessible Typing Speed Tester Typing Test](screenshot-typing.png)

---

## 📊 Test Results

After completing the test, users receive detailed performance statistics.

![Accessible Typing Speed Tester Results](screenshot-results.png)

---

# 🛠️ Technologies Used

The project was built using:

- **Python**
- **Streamlit**
- **HTML**
- **CSS**
- **JavaScript**
- **Web Speech API**
- **Browser Speech Synthesis**
- **Git**
- **GitHub**
- **Streamlit Community Cloud**

---

# 📂 Project Structure

```text
accessible-typing-speed-tester/
│
├── type_test.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshot-home.png
├── screenshot-typing.png
└── screenshot-results.png
