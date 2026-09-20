import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Accessible Typing Speed Tester",
    page_icon="⌨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Accessible Typing Speed Tester</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 20px;
    font-family: Arial, Helvetica, sans-serif;
    background: #101318;
    color: #ffffff;
}

#app {
    max-width: 1150px;
    margin: auto;
}

h1 {
    text-align: center;
    font-size: 38px;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #c8ced8;
    font-size: 18px;
    margin-bottom: 30px;
}

.mode-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-bottom: 25px;
}

.mode-card {
    background: #1b2028;
    border: 2px solid #3b4350;
    border-radius: 16px;
    padding: 25px;
}

.mode-card h2 {
    margin-top: 0;
    font-size: 27px;
}

.mode-card p {
    color: #c8ced8;
    line-height: 1.6;
    font-size: 16px;
}

.normal-card {
    border-color: #4f8cff;
}

.voice-card {
    border-color: #9b6cff;
}

.setting {
    margin-top: 18px;
}

.setting label {
    display: block;
    font-weight: bold;
    margin-bottom: 7px;
}

select,
input[type="range"] {
    width: 100%;
}

select {
    background: #0f1217;
    color: white;
    border: 1px solid #555f6e;
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
}

.range-row {
    display: flex;
    align-items: center;
    gap: 12px;
}

.range-row input {
    flex: 1;
}

.value-display {
    min-width: 55px;
    text-align: right;
    font-weight: bold;
}

button {
    border: none;
    border-radius: 10px;
    padding: 14px 20px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    margin-top: 18px;
    background: #2864ff;
    color: white;
}

button:hover {
    filter: brightness(1.15);
}

button:focus,
select:focus,
textarea:focus,
input:focus {
    outline: 3px solid #ffd43b;
    outline-offset: 2px;
}

.voice-start {
    background: #8b5cf6;
}

.secondary {
    background: #3d4653;
}

.danger {
    background: #c83b3b;
}

.success {
    background: #248a52;
}

.hidden {
    display: none !important;
}

#testArea {
    background: #181d24;
    border: 2px solid #424b58;
    border-radius: 16px;
    padding: 25px;
    margin-top: 25px;
}

.test-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 20px;
}

.test-title {
    font-size: 25px;
    font-weight: bold;
}

.status {
    color: #bfc6d1;
}

.passage-box {
    background: #0d1015;
    border: 2px solid #596474;
    border-radius: 12px;
    padding: 22px;
    font-size: 22px;
    line-height: 1.8;
    min-height: 150px;
    margin-bottom: 20px;
}

textarea {
    width: 100%;
    min-height: 190px;
    resize: vertical;
    background: #0c0f13;
    color: white;
    border: 2px solid #596474;
    border-radius: 12px;
    padding: 18px;
    font-size: 20px;
    line-height: 1.6;
    font-family: Arial, Helvetica, sans-serif;
}

.stats {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 10px;
    margin-top: 20px;
}

.stat {
    background: #222934;
    border-radius: 10px;
    padding: 15px 8px;
    text-align: center;
}

.stat-value {
    font-size: 25px;
    font-weight: bold;
}

.stat-label {
    color: #b9c1cc;
    font-size: 13px;
    margin-top: 5px;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.controls button {
    margin-top: 15px;
}

#results {
    background: #181d24;
    border: 2px solid #424b58;
    border-radius: 16px;
    padding: 28px;
    margin-top: 25px;
}

.results-title {
    font-size: 30px;
    margin-top: 0;
}

.result-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
}

.result-card {
    background: #232a34;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

.result-number {
    font-size: 30px;
    font-weight: bold;
}

.result-name {
    color: #bec6d2;
    margin-top: 6px;
}

.history {
    margin-top: 25px;
}

.history table {
    width: 100%;
    border-collapse: collapse;
}

.history th,
.history td {
    padding: 10px;
    border-bottom: 1px solid #3b4350;
    text-align: left;
}

#message {
    background: #242b35;
    padding: 12px 15px;
    border-radius: 8px;
    margin-top: 15px;
    color: #dbe1ea;
}

@media (max-width: 850px) {

    .mode-container {
        grid-template-columns: 1fr;
    }

    .stats {
        grid-template-columns: repeat(3, 1fr);
    }

    .result-grid {
        grid-template-columns: repeat(2, 1fr);
    }

}

@media (max-width: 500px) {

    body {
        padding: 10px;
    }

    h1 {
        font-size: 30px;
    }

    .stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .result-grid {
        grid-template-columns: 1fr;
    }

    .passage-box {
        font-size: 19px;
    }

    textarea {
        font-size: 18px;
    }

}

</style>
</head>

<body>

<div id="app">

<h1>⌨️ Accessible Typing Speed Tester</h1>

<div class="subtitle">
Choose a typing mode to begin
</div>

<div id="openingScreen">

<div class="mode-container">

<div class="mode-card normal-card">

<h2>Normal Mode</h2>

<p>
A standard typing-speed test. Press Start and a passage
will appear immediately. The timer starts automatically.
</p>

<div class="setting">

<label for="normalDuration">
Test Duration
</label>

<select id="normalDuration">

<option value="30">30 seconds</option>
<option value="60" selected>60 seconds</option>
<option value="120">120 seconds</option>
<option value="passage">Complete Passage</option>

</select>

</div>

<button id="normalStart">
Start Normal Test
</button>

</div>


<div class="mode-card voice-card">

<h2>🔊 Voice-Assisted Mode</h2>

<p>
The passage will automatically be read aloud when you
start the test. Adjust the voice settings below first.
</p>

<div class="setting">

<label for="voiceSelect">
Voice
</label>

<select id="voiceSelect">
<option>Loading voices...</option>
</select>

</div>

<div class="setting">

<label for="speechRate">
Speech Speed
</label>

<div class="range-row">

<input
    type="range"
    id="speechRate"
    min="0.5"
    max="2"
    step="0.1"
    value="1"
>

<span
    id="rateValue"
    class="value-display">
1.0x
</span>

</div>

</div>

<div class="setting">

<label for="speechVolume">
Volume
</label>

<div class="range-row">

<input
    type="range"
    id="speechVolume"
    min="0"
    max="1"
    step="0.05"
    value="1"
>

<span
    id="volumeValue"
    class="value-display">
100%
</span>

</div>

</div>

<div class="setting">

<label for="voiceDuration">
Test Duration
</label>

<select id="voiceDuration">

<option value="30">30 seconds</option>
<option value="60" selected>60 seconds</option>
<option value="120">120 seconds</option>
<option value="passage">Complete Passage</option>

</select>

</div>

<button
    id="voiceStart"
    class="voice-start">
Start Voice Test
</button>

</div>

</div>

</div>

<div id="testArea" class="hidden">

<div class="test-header">

<div>

<div
    id="testTitle"
    class="test-title">
Typing Test
</div>

<div
    id="status"
    class="status"
    aria-live="polite">
Ready
</div>

</div>

</div>

<div
    id="passage"
    class="passage-box"
    aria-live="polite">
</div>

<textarea
    id="typingArea"
    placeholder="Start typing here..."
    aria-label="Typing area"></textarea>

<div class="stats">

<div class="stat">
<div id="liveWpm" class="stat-value">0</div>
<div class="stat-label">WPM</div>
</div>

<div class="stat">
<div id="liveAccuracy" class="stat-value">100%</div>
<div class="stat-label">Accuracy</div>
</div>

<div class="stat">
<div id="liveCorrectChars" class="stat-value">0</div>
<div class="stat-label">Correct Characters</div>
</div>

<div class="stat">
<div id="liveIncorrectChars" class="stat-value">0</div>
<div class="stat-label">Incorrect Characters</div>
</div>

<div class="stat">
<div id="liveErrors" class="stat-value">0</div>
<div class="stat-label">Errors</div>
</div>

<div class="stat">
<div id="liveTime" class="stat-value">0s</div>
<div class="stat-label">Time</div>
</div>

</div>

<div class="controls">

<button
    id="pauseButton"
    class="secondary">
Pause
</button>

<button
    id="replayButton"
    class="voice-start hidden">
🔊 Replay Passage
</button>

<button
    id="finishButton"
    class="success">
Finish Test
</button>

<button
    id="restartButton"
    class="danger">
Restart
</button>

</div>

<div id="message"
     aria-live="polite">
Your statistics will update while you type.
</div>

</div>

<div id="results" class="hidden">

<h2 class="results-title">
🎉 Test Results
</h2>

<div class="result-grid">

<div class="result-card">
<div id="resultWpm" class="result-number">0</div>
<div class="result-name">WPM</div>
</div>

<div class="result-card">
<div id="resultAccuracy" class="result-number">0%</div>
<div class="result-name">Accuracy</div>
</div>

<div class="result-card">
<div id="resultCorrectChars" class="result-number">0</div>
<div class="result-name">Correct Characters</div>
</div>

<div class="result-card">
<div id="resultIncorrectChars" class="result-number">0</div>
<div class="result-name">Incorrect Characters</div>
</div>

<div class="result-card">
<div id="resultErrors" class="result-number">0</div>
<div class="result-name">Errors</div>
</div>

<div class="result-card">
<div id="resultCorrectWords" class="result-number">0</div>
<div class="result-name">Correct Words</div>
</div>

<div class="result-card">
<div id="resultTime" class="result-number">0s</div>
<div class="result-name">Time</div>
</div>

<div class="result-card">
<div id="resultTotalChars" class="result-number">0</div>
<div class="result-name">Typed Characters</div>
</div>

</div>

<div class="controls">

<button
    id="anotherTest"
    class="success">
Start Another Test
</button>

</div>

<div class="history">

<h3>Recent Test History</h3>

<table>

<thead>

<tr>
<th>Mode</th>
<th>WPM</th>
<th>Accuracy</th>
<th>Time</th>
</tr>

</thead>

<tbody id="historyBody">
</tbody>

</table>

</div>

</div>

</div>
"""

html_code += r"""

<script>

const passages = [

"Technology has changed the way people learn, work, communicate, and solve problems. With the right tools, information can be organized and shared quickly.",

"Learning to type accurately is an important computer skill. Regular practice can improve speed, confidence, concentration, and overall productivity.",

"Artificial intelligence is becoming an important part of modern technology. It can help people analyze information, recognize patterns, and make useful predictions.",

"Good communication requires patience and attention. Listening carefully and expressing ideas clearly can help people understand one another more effectively.",

"Every successful project begins with a clear goal. Breaking a large task into smaller steps makes it easier to plan, complete, and evaluate.",

"Computers are powerful tools for education and creativity. Students can use them to research information, write programs, create presentations, and explore new ideas.",

"Accessibility makes technology easier to use for everyone. Features such as screen readers, speech recognition, keyboard navigation, and text enlargement can remove barriers.",

"Practice is one of the most effective ways to improve a skill. Small improvements made consistently can produce significant results over time.",

"The internet provides access to an enormous amount of information. However, users should always check important information against trustworthy sources.",

"Modern factories use sensors and software to monitor machines and production processes. Data can help engineers identify problems before they become serious.",

"Data analysis helps organizations understand what is happening in their systems. Good analysis combines accurate data, appropriate methods, and careful interpretation.",

"Programming teaches people how to break complex problems into logical steps. A well-designed program is easier to understand, test, maintain, and improve.",

"Time management can make difficult tasks feel more manageable. Setting priorities and working on one important task at a time can improve focus.",

"Reading regularly can strengthen vocabulary and comprehension. It also exposes people to different ideas, writing styles, experiences, and perspectives.",

"Problem solving involves identifying the problem, understanding the available information, considering possible solutions, and evaluating the result.",

"Cloud computing allows people to access applications and data through internet-connected services. It has become an important part of modern digital infrastructure.",

"Cybersecurity helps protect computers, networks, accounts, and information from unauthorized access. Strong passwords and careful online behavior are important safeguards.",

"Good software should be useful, reliable, understandable, and accessible. Testing is important because even small problems can affect the user experience.",

"Learning something new does not require perfection. Mistakes provide useful information about what needs more practice and attention.",

"Digital skills are increasingly valuable in education and employment. Understanding common software and online tools can make many tasks easier.",

"Successful teamwork depends on communication, responsibility, respect, and a shared understanding of the goal. Each person can contribute different strengths.",

"Science helps us understand the world through observation, experimentation, evidence, and careful reasoning. New discoveries often lead to new questions.",

"A healthy learning routine includes focused practice as well as regular breaks. Giving the mind time to rest can help maintain attention.",

"Maps, charts, and visualizations can make complex information easier to understand. The best visualization depends on the question being asked.",

"Good decisions are easier to make when people clearly understand the available choices and the possible consequences of each option.",

"Modern applications often combine databases, user interfaces, software services, and automated processes. These components work together to provide useful experiences.",

"Typing tests measure several aspects of performance. Speed is important, but accuracy and consistency are also valuable indicators of typing skill.",

"Voice technology can make computers more accessible. Speech output allows users to receive information without relying entirely on visual interfaces.",

"Education is a continuous process. People can develop new skills throughout their lives by practicing, asking questions, and exploring unfamiliar subjects.",

"Clear instructions make technical tasks easier to complete. When instructions are organized into logical steps, users can understand what to do and why it matters."

];


let currentMode = "";
let currentPassage = "";
let currentPassageIndex = -1;

let testRunning = false;
let testPaused = false;

let startTime = 0;
let pausedStarted = 0;
let totalPausedTime = 0;

let timerInterval = null;

let selectedDuration = 60;

let speechAvailable =
    ("speechSynthesis" in window);

let currentUtterance = null;


/* ---------------------------------------------------------
   ELEMENT REFERENCES
--------------------------------------------------------- */

const openingScreen =
    document.getElementById("openingScreen");

const testArea =
    document.getElementById("testArea");

const results =
    document.getElementById("results");

const passageElement =
    document.getElementById("passage");

const typingArea =
    document.getElementById("typingArea");

const statusElement =
    document.getElementById("status");

const messageElement =
    document.getElementById("message");

const normalStart =
    document.getElementById("normalStart");

const voiceStart =
    document.getElementById("voiceStart");

const pauseButton =
    document.getElementById("pauseButton");

const replayButton =
    document.getElementById("replayButton");

const finishButton =
    document.getElementById("finishButton");

const restartButton =
    document.getElementById("restartButton");

const anotherTest =
    document.getElementById("anotherTest");

const voiceSelect =
    document.getElementById("voiceSelect");

const speechRate =
    document.getElementById("speechRate");

const speechVolume =
    document.getElementById("speechVolume");

const rateValue =
    document.getElementById("rateValue");

const volumeValue =
    document.getElementById("volumeValue");

const normalDuration =
    document.getElementById("normalDuration");

const voiceDuration =
    document.getElementById("voiceDuration");


/* ---------------------------------------------------------
   RANDOM PASSAGE
--------------------------------------------------------- */

function getNewPassage() {

    let index;

    do {

        index =
            Math.floor(
                Math.random() * passages.length
            );

    } while (
        passages.length > 1 &&
        index === currentPassageIndex
    );

    currentPassageIndex = index;

    return passages[index];
}


/* ---------------------------------------------------------
   VOICE LIST
--------------------------------------------------------- */

function loadVoices() {

    if (!speechAvailable) {

        voiceSelect.innerHTML =
            "<option>Speech not supported</option>";

        voiceStart.disabled = true;

        return;
    }

    const voices =
        window.speechSynthesis.getVoices();

    voiceSelect.innerHTML = "";

    if (voices.length === 0) {

        const option =
            document.createElement("option");

        option.textContent =
            "Default browser voice";

        option.value = "";

        voiceSelect.appendChild(option);

        return;
    }

    voices.forEach((voice, index) => {

        const option =
            document.createElement("option");

        option.value = index;

        option.textContent =
            voice.name +
            " (" +
            voice.lang +
            ")";

        voiceSelect.appendChild(option);

    });

}

if (speechAvailable) {

    loadVoices();

    window.speechSynthesis.onvoiceschanged =
        loadVoices;

}


/* ---------------------------------------------------------
   SPEECH SETTINGS
--------------------------------------------------------- */

speechRate.addEventListener(
    "input",
    function() {

        rateValue.textContent =
            Number(this.value).toFixed(1) + "x";

    }
);

speechVolume.addEventListener(
    "input",
    function() {

        volumeValue.textContent =
            Math.round(
                Number(this.value) * 100
            ) + "%";

    }
);


/* ---------------------------------------------------------
   SPEAK PASSAGE
--------------------------------------------------------- */

function speakPassage() {

    if (!speechAvailable) {

        messageElement.textContent =
            "Your browser does not support speech synthesis.";

        return;

    }

    window.speechSynthesis.cancel();

    currentUtterance =
        new SpeechSynthesisUtterance(
            currentPassage
        );

    currentUtterance.rate =
        Number(speechRate.value);

    currentUtterance.volume =
        Number(speechVolume.value);

    const voices =
        window.speechSynthesis.getVoices();

    const selectedIndex =
        Number(voiceSelect.value);

    if (
        voices.length > 0 &&
        !isNaN(selectedIndex) &&
        voices[selectedIndex]
    ) {

        currentUtterance.voice =
            voices[selectedIndex];

    }

    currentUtterance.onstart =
        function() {

            messageElement.textContent =
                "🔊 Passage is being read aloud.";

        };

    currentUtterance.onend =
        function() {

            if (testRunning) {

                messageElement.textContent =
                    "Voice reading finished. Continue typing.";

            }

        };

    window.speechSynthesis.speak(
        currentUtterance
    );

}


/* ---------------------------------------------------------
   TIMER
--------------------------------------------------------- */

function getElapsedSeconds() {

    if (!startTime) {
        return 0;
    }

    let now =
        performance.now();

    let pausedTime =
        totalPausedTime;

    if (testPaused) {

        pausedTime +=
            now - pausedStarted;

    }

    let elapsed =
        (
            now -
            startTime -
            pausedTime
        ) / 1000;

    return Math.max(0, elapsed);

}


function startTimer() {

    clearInterval(timerInterval);

    timerInterval =
        setInterval(
            updateTimer,
            100
        );

}


function updateTimer() {

    if (!testRunning) {
        return;
    }

    const elapsed =
        getElapsedSeconds();

    const rounded =
        Math.floor(elapsed);

    document.getElementById(
        "liveTime"
    ).textContent =
        rounded + "s";


    if (
        selectedDuration !== "passage" &&
        elapsed >= Number(selectedDuration)
    ) {

        finishTest();

    }

}

"""

html_code += r"""

/* ---------------------------------------------------------
   START TEST
--------------------------------------------------------- */

function startTest(mode) {

    currentMode = mode;

    if (mode === "normal") {

        selectedDuration =
            normalDuration.value;

    } else {

        selectedDuration =
            voiceDuration.value;

    }

    currentPassage =
        getNewPassage();

    passageElement.textContent =
        currentPassage;

    typingArea.value = "";

    openingScreen.classList.add(
        "hidden"
    );

    results.classList.add(
        "hidden"
    );

    testArea.classList.remove(
        "hidden"
    );

    testRunning = true;
    testPaused = false;

    startTime =
        performance.now();

    pausedStarted = 0;
    totalPausedTime = 0;

    pauseButton.textContent =
        "Pause";

    statusElement.textContent =
        mode === "voice"
        ? "Voice-Assisted Test"
        : "Normal Typing Test";

    messageElement.textContent =
        "Start typing the passage.";

    replayButton.classList.toggle(
        "hidden",
        mode !== "voice"
    );

    document.getElementById(
        "testTitle"
    ).textContent =
        mode === "voice"
        ? "🔊 Voice-Assisted Typing Test"
        : "⌨️ Normal Typing Test";


    resetLiveStats();

    startTimer();

    /*
       IMPORTANT:
       Speech is started directly from the Start button
       event path so browsers are much more likely to
       allow automatic speech playback.
    */

    if (mode === "voice") {

        speakPassage();

    }

    typingArea.focus();

}


/* ---------------------------------------------------------
   RESET LIVE STATS
--------------------------------------------------------- */

function resetLiveStats() {

    document.getElementById(
        "liveWpm"
    ).textContent = "0";

    document.getElementById(
        "liveAccuracy"
    ).textContent = "100%";

    document.getElementById(
        "liveCorrectChars"
    ).textContent = "0";

    document.getElementById(
        "liveIncorrectChars"
    ).textContent = "0";

    document.getElementById(
        "liveErrors"
    ).textContent = "0";

    document.getElementById(
        "liveTime"
    ).textContent = "0s";

}


/* ---------------------------------------------------------
   CALCULATE STATISTICS
--------------------------------------------------------- */

function calculateStatistics() {

    const typed =
        typingArea.value;

    let correctChars = 0;
    let incorrectChars = 0;

    const compareLength =
        Math.min(
            typed.length,
            currentPassage.length
        );

    for (
        let i = 0;
        i < compareLength;
        i++
    ) {

        if (
            typed[i] ===
            currentPassage[i]
        ) {

            correctChars++;

        } else {

            incorrectChars++;

        }

    }

    if (
        typed.length >
        currentPassage.length
    ) {

        incorrectChars +=
            typed.length -
            currentPassage.length;

    }

    const totalTyped =
        typed.length;

    const totalChecked =
        correctChars +
        incorrectChars;

    let accuracy = 100;

    if (totalChecked > 0) {

        accuracy =
            (
                correctChars /
                totalChecked
            ) * 100;

    }

    const elapsed =
        Math.max(
            getElapsedSeconds(),
            0.1
        );

    const minutes =
        elapsed / 60;

    const wpm =
        minutes > 0
        ? (correctChars / 5) / minutes
        : 0;


    /*
       Count words that are completely correct.
    */

    const typedWords =
        typed.trim() === ""
        ? []
        : typed.trim().split(/\s+/);

    const passageWords =
        currentPassage.trim().split(/\s+/);

    let correctWords = 0;

    for (
        let i = 0;
        i < typedWords.length &&
        i < passageWords.length;
        i++
    ) {

        if (
            typedWords[i] ===
            passageWords[i]
        ) {

            correctWords++;

        }

    }


    return {

        wpm: Math.round(wpm),

        accuracy:
            Math.round(
                accuracy * 10
            ) / 10,

        correctChars,

        incorrectChars,

        errors: incorrectChars,

        correctWords,

        time:
            Math.floor(elapsed),

        totalChars:
            totalTyped

    };

}


/* ---------------------------------------------------------
   UPDATE LIVE STATISTICS
--------------------------------------------------------- */

function updateLiveStats() {

    if (!testRunning) {
        return;
    }

    const stats =
        calculateStatistics();

    document.getElementById(
        "liveWpm"
    ).textContent =
        stats.wpm;

    document.getElementById(
        "liveAccuracy"
    ).textContent =
        stats.accuracy + "%";

    document.getElementById(
        "liveCorrectChars"
    ).textContent =
        stats.correctChars;

    document.getElementById(
        "liveIncorrectChars"
    ).textContent =
        stats.incorrectChars;

    document.getElementById(
        "liveErrors"
    ).textContent =
        stats.errors;

}


/* ---------------------------------------------------------
   TYPING INPUT
--------------------------------------------------------- */

typingArea.addEventListener(
    "input",
    function() {

        updateLiveStats();

        if (
            selectedDuration ===
            "passage" &&
            typingArea.value.length >=
            currentPassage.length
        ) {

            finishTest();

        }

    }
);


/* ---------------------------------------------------------
   PAUSE / RESUME
--------------------------------------------------------- */

function togglePause() {

    if (!testRunning) {
        return;
    }

    if (!testPaused) {

        testPaused = true;

        pausedStarted =
            performance.now();

        pauseButton.textContent =
            "Resume";

        statusElement.textContent =
            "Paused";

        messageElement.textContent =
            "Test paused.";

        if (
            currentMode === "voice" &&
            speechAvailable
        ) {

            window.speechSynthesis.pause();

        }

        typingArea.disabled = true;

    } else {

        const now =
            performance.now();

        totalPausedTime +=
            now - pausedStarted;

        pausedStarted = 0;

        testPaused = false;

        pauseButton.textContent =
            "Pause";

        statusElement.textContent =
            currentMode === "voice"
            ? "Voice-Assisted Test"
            : "Normal Typing Test";

        messageElement.textContent =
            "Test resumed.";

        if (
            currentMode === "voice" &&
            speechAvailable
        ) {

            window.speechSynthesis.resume();

        }

        typingArea.disabled = false;

        typingArea.focus();

    }

}


/* ---------------------------------------------------------
   FINISH TEST
--------------------------------------------------------- */

function finishTest() {

    if (!testRunning) {
        return;
    }

    testRunning = false;

    clearInterval(
        timerInterval
    );

    if (speechAvailable) {

        window.speechSynthesis.cancel();

    }

    typingArea.disabled = true;

    const stats =
        calculateStatistics();

    document.getElementById(
        "resultWpm"
    ).textContent =
        stats.wpm;

    document.getElementById(
        "resultAccuracy"
    ).textContent =
        stats.accuracy + "%";

    document.getElementById(
        "resultCorrectChars"
    ).textContent =
        stats.correctChars;

    document.getElementById(
        "resultIncorrectChars"
    ).textContent =
        stats.incorrectChars;

    document.getElementById(
        "resultErrors"
    ).textContent =
        stats.errors;

    document.getElementById(
        "resultCorrectWords"
    ).textContent =
        stats.correctWords;

    document.getElementById(
        "resultTime"
    ).textContent =
        stats.time + "s";

    document.getElementById(
        "resultTotalChars"
    ).textContent =
        stats.totalChars;

    testArea.classList.add(
        "hidden"
    );

    results.classList.remove(
        "hidden"
    );

    saveHistory(stats);

    showHistory();

}


/* ---------------------------------------------------------
   REPLAY VOICE
--------------------------------------------------------- */

replayButton.addEventListener(
    "click",
    function() {

        if (
            currentMode === "voice" &&
            currentPassage
        ) {

            speakPassage();

        }

    }
);


/* ---------------------------------------------------------
   BUTTON EVENTS
--------------------------------------------------------- */

normalStart.addEventListener(
    "click",
    function() {

        startTest("normal");

    }
);


voiceStart.addEventListener(
    "click",
    function() {

        startTest("voice");

    }
);


pauseButton.addEventListener(
    "click",
    function() {

        togglePause();

    }
);


finishButton.addEventListener(
    "click",
    function() {

        finishTest();

    }
);


restartButton.addEventListener(
    "click",
    function() {

        if (speechAvailable) {

            window.speechSynthesis.cancel();

        }

        clearInterval(
            timerInterval
        );

        testRunning = false;

        testPaused = false;

        typingArea.disabled = false;

        testArea.classList.add(
            "hidden"
        );

        results.classList.add(
            "hidden"
        );

        openingScreen.classList.remove(
            "hidden"
        );

        messageElement.textContent =
            "Your statistics will update while you type.";

    }
);


/* ---------------------------------------------------------
   START ANOTHER TEST
--------------------------------------------------------- */

anotherTest.addEventListener(
    "click",
    function() {

        results.classList.add(
            "hidden"
        );

        openingScreen.classList.remove(
            "hidden"
        );

    }
);


/* ---------------------------------------------------------
   HISTORY
--------------------------------------------------------- */

function getHistory() {

    try {

        return JSON.parse(
            localStorage.getItem(
                "accessibleTypingHistory"
            )
        ) || [];

    } catch (error) {

        return [];

    }

}


function saveHistory(stats) {

    const history =
        getHistory();

    history.unshift({

        mode:
            currentMode === "voice"
            ? "Voice"
            : "Normal",

        wpm:
            stats.wpm,

        accuracy:
            stats.accuracy,

        time:
            stats.time

    });

    /*
       Keep the latest 10 tests.
    */

    const limited =
        history.slice(0, 10);

    try {

        localStorage.setItem(
            "accessibleTypingHistory",
            JSON.stringify(limited)
        );

    } catch (error) {

        console.log(
            "History could not be saved."
        );

    }

}


function showHistory() {

    const history =
        getHistory();

    const body =
        document.getElementById(
            "historyBody"
        );

    body.innerHTML = "";

    if (history.length === 0) {

        const row =
            document.createElement("tr");

        row.innerHTML =
            "<td colspan='4'>No previous tests.</td>";

        body.appendChild(row);

        return;

    }

    history.forEach(
        function(item) {

            const row =
                document.createElement("tr");

            row.innerHTML =

                "<td>" +
                item.mode +
                "</td>" +

                "<td>" +
                item.wpm +
                "</td>" +

                "<td>" +
                item.accuracy +
                "%</td>" +

                "<td>" +
                item.time +
                "s</td>";

            body.appendChild(row);

        }
    );

}


/* ---------------------------------------------------------
   INITIAL HISTORY
--------------------------------------------------------- */

showHistory();

</script>

</body>
</html>
"""
html_code += r"""

<!--
The application is intentionally implemented entirely
inside the browser.

This means:

1. Voice playback happens on the user's device.
2. Speech speed can be changed.
3. Speech volume can be changed.
4. The browser's available voices can be selected.
5. Voice playback does not require pyttsx3.
6. The typing test works without an internet connection
   after the Streamlit page has loaded.
-->

"""

# ------------------------------------------------------------
# DISPLAY THE COMPLETE APPLICATION
# ------------------------------------------------------------

components.html(
    html_code,
    height=1250,
    scrolling=True
)
