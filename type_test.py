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
    grid-template-columns: 1fr 1fr 1fr;
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

.word-card {
    border-color: #20b486;
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

/*
   ALL THREE START BUTTONS NOW USE THE SAME STYLE.
   No separate voice or word start colors.
*/

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
    white-space: pre-line;
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

@media (max-width: 1050px) {

    .mode-container {
        grid-template-columns: 1fr;
    }

}

@media (max-width: 850px) {

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

<!-- NORMAL MODE -->

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

<option value="30">
30 seconds
</option>

<option value="60" selected>
60 seconds
</option>

<option value="120">
120 seconds
</option>

<option value="passage">
Complete Passage
</option>

</select>

</div>

<button id="normalStart">
Start Normal Test
</button>

</div>


<!-- VOICE MODE -->

<div class="mode-card voice-card">

<h2>🔊 Voice-Assisted Mode</h2>

<p>
The complete passage will automatically be read aloud
when you start the test. Adjust the voice settings below.
</p>

<div class="setting">

<label for="voiceSelect">
Voice
</label>

<select id="voiceSelect">
<option>
Loading voices...
</option>
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
    value="0.7"
>

<span
    id="rateValue"
    class="value-display">
0.7x
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

<option value="30">
30 seconds
</option>

<option value="60" selected>
60 seconds
</option>

<option value="120">
120 seconds
</option>

<option value="passage">
Complete Passage
</option>

</select>

</div>

<button id="voiceStart">
Start Voice Test
</button>

</div>


<!-- WORD BY WORD MODE -->

<div class="mode-card word-card">

<h2>🗣️ Word-by-Word Voice</h2>

<p>
The tester reads one word at a time. As you approach
the final three letters of the current word, the next
word is spoken automatically.
</p>

<div class="setting">

<label for="wordDuration">
Test Duration
</label>

<select id="wordDuration">

<option value="30">
30 seconds
</option>

<option value="60" selected>
60 seconds
</option>

</select>

</div>

<button id="wordStart">
Start Word-by-Word Test
</button>

</div>

</div>

</div>


<!-- TEST AREA -->

<div id="testArea" class="hidden">

<div class="test-header">

<div>

<div id="testTitle" class="test-title">
Typing Test
</div>

<div id="status" class="status" aria-live="polite">
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

<div id="liveWpm" class="stat-value">
0
</div>

<div class="stat-label">
WPM
</div>

</div>


<div class="stat">

<div id="liveAccuracy" class="stat-value">
100%
</div>

<div class="stat-label">
Accuracy
</div>

</div>


<div class="stat">

<div id="liveCorrectChars" class="stat-value">
0
</div>

<div class="stat-label">
Correct Characters
</div>

</div>


<div class="stat">

<div id="liveIncorrectChars" class="stat-value">
0
</div>

<div class="stat-label">
Incorrect Characters
</div>

</div>


<div class="stat">

<div id="liveErrors" class="stat-value">
0
</div>

<div class="stat-label">
Errors
</div>

</div>


<div class="stat">

<div id="liveTime" class="stat-value">
0s
</div>

<div class="stat-label">
Time
</div>

</div>

</div>


<div class="controls">

<button id="pauseButton" class="secondary">
Pause
</button>

<button id="replayButton" class="hidden">
🔊 Replay
</button>

<button id="finishButton" class="success">
Finish Test
</button>

<button id="restartButton" class="danger">
Restart
</button>

</div>


<div id="message" aria-live="polite">
Your statistics will update while you type.
</div>

</div>


<!-- RESULTS -->

<div id="results" class="hidden">

<h2 class="results-title">
🎉 Test Results
</h2>

<div class="result-grid">

<div class="result-card">

<div id="resultWpm" class="result-number">
0
</div>

<div class="result-name">
WPM
</div>

</div>


<div class="result-card">

<div id="resultAccuracy" class="result-number">
0%
</div>

<div class="result-name">
Accuracy
</div>

</div>


<div class="result-card">

<div id="resultCorrectChars" class="result-number">
0
</div>

<div class="result-name">
Correct Characters
</div>

</div>


<div class="result-card">

<div id="resultIncorrectChars" class="result-number">
0
</div>

<div class="result-name">
Incorrect Characters
</div>

</div>


<div class="result-card">

<div id="resultErrors" class="result-number">
0
</div>

<div class="result-name">
Errors
</div>

</div>


<div class="result-card">

<div id="resultCorrectWords" class="result-number">
0
</div>

<div class="result-name">
Correct Words
</div>

</div>


<div class="result-card">

<div id="resultTime" class="result-number">
0s
</div>

<div class="result-name">
Time
</div>

</div>


<div class="result-card">

<div id="resultTotalChars" class="result-number">
0
</div>

<div class="result-name">
Typed Characters
</div>

</div>

</div>


<div class="controls">

<button id="anotherTest" class="success">
Try Another Test
</button>

</div>


<div class="history">

<h3>
Recent Test History
</h3>

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

/* =========================================================
   PASSAGE DATA
   ========================================================= */

const passageLines = [

"Technology has changed the way people learn, work, communicate, and solve problems.",

"With the right tools, information can be organized and shared quickly.",

"Learning to type accurately is an important computer skill.",

"Regular practice can improve speed, confidence, concentration, and productivity.",

"Artificial intelligence can help people analyze information and recognize useful patterns.",

"Modern software allows people to solve complex problems more efficiently.",

"Good communication requires patience, attention, and clear expression.",

"Listening carefully can help people understand different ideas and perspectives.",

"Every successful project begins with a clear goal and a practical plan.",

"Breaking a large task into smaller steps makes it easier to complete.",

"Computers are powerful tools for education, creativity, and research.",

"Students can use technology to write programs, create presentations, and explore ideas.",

"Accessibility makes technology easier to use for everyone.",

"Screen readers, speech output, and keyboard navigation can remove barriers.",

"Practice is one of the most effective ways to improve a skill.",

"Small improvements made consistently can produce significant results over time.",

"The internet provides access to an enormous amount of information.",

"Important information should always be checked against trustworthy sources.",

"Modern factories use sensors and software to monitor machines and production.",

"Data can help engineers identify problems before they become serious.",

"Data analysis helps organizations understand what is happening in their systems.",

"Good analysis combines accurate data, appropriate methods, and careful interpretation.",

"Programming teaches people to break complex problems into logical steps.",

"A well-designed program is easier to understand, test, maintain, and improve.",

"Time management can make difficult tasks feel more manageable.",

"Setting priorities can improve focus when several tasks need attention.",

"Reading regularly can strengthen vocabulary and comprehension.",

"It also exposes people to different ideas, writing styles, and experiences.",

"Problem solving involves identifying a problem and evaluating possible solutions.",

"Good decisions are easier when people understand their choices and consequences."

];


/* =========================================================
   VARIABLES
   ========================================================= */

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


/*
   Word-by-word variables.

   IMPORTANT:
   Instead of trying to guess which word the user is
   currently typing, we store the exact start and end
   position of EVERY word in the complete passage.

   This fixes the 60-second / 8-line problem.
*/

let wordList = [];

let currentWordIndex = 0;

let lastWordTriggerIndex = -1;

let wordModeStarted = false;


/* =========================================================
   ELEMENT REFERENCES
   ========================================================= */

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

const wordStart =
    document.getElementById("wordStart");

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

const wordDuration =
    document.getElementById("wordDuration");


/* =========================================================
   PASSAGE LENGTH
   ========================================================= */

function getRequiredLineCount(duration) {

    if (duration === "30") {
        return 4;
    }

    if (duration === "60") {
        return 8;
    }

    /*
       These remain for Normal Mode and
       Voice-Assisted Mode.
    */

    if (duration === "120") {
        return 15;
    }

    return 15;
}


/* =========================================================
   CREATE NEW PASSAGE
   ========================================================= */

function getNewPassage(duration) {

    const requiredLines =
        getRequiredLineCount(duration);

    let available =
        [...passageLines];


    /*
       Prevent the first line of the previous passage
       from immediately appearing again.
    */

    if (
        currentPassageIndex >= 0 &&
        available.length > requiredLines
    ) {

        const previousFirstLine =
            currentPassage
                .split("\n")[0];

        available =
            available.filter(
                function(line) {

                    return line !==
                        previousFirstLine;

                }
            );

    }


    /*
       Fisher-Yates shuffle.
    */

    for (
        let i = available.length - 1;
        i > 0;
        i--
    ) {

        const j =
            Math.floor(
                Math.random() * (i + 1)
            );

        [
            available[i],
            available[j]
        ] =
        [
            available[j],
            available[i]
        ];

    }


    const selectedLines =
        available.slice(
            0,
            requiredLines
        );


    currentPassage =
        selectedLines.join("\n");


    currentPassageIndex++;

    return currentPassage;
}


/* =========================================================
   VOICE LIST
   ========================================================= */

function loadVoices() {

    if (!speechAvailable) {

        voiceSelect.innerHTML =
            "<option>Speech not supported</option>";

        voiceStart.disabled = true;

        wordStart.disabled = true;

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


    voices.forEach(
        function(voice, index) {

            const option =
                document.createElement("option");

            option.value = index;

            option.textContent =
                voice.name +
                " (" +
                voice.lang +
                ")";

            voiceSelect.appendChild(option);

        }
    );

}


if (speechAvailable) {

    loadVoices();

    window.speechSynthesis.onvoiceschanged =
        loadVoices;

}


/* =========================================================
   VOICE SETTINGS
   ========================================================= */

speechRate.addEventListener(
    "input",
    function() {

        rateValue.textContent =
            speechRate.value + "x";

    }
);


speechVolume.addEventListener(
    "input",
    function() {

        volumeValue.textContent =
            Math.round(
                speechVolume.value * 100
            ) + "%";

    }
);


/* =========================================================
   GET SELECTED VOICE
   ========================================================= */

function getSelectedVoice() {

    if (!speechAvailable) {
        return null;
    }

    const voices =
        window.speechSynthesis.getVoices();

    const selectedIndex =
        parseInt(
            voiceSelect.value
        );

    if (
        !isNaN(selectedIndex) &&
        voices[selectedIndex]
    ) {

        return voices[selectedIndex];

    }

    return null;
}


/* =========================================================
   SPEAK COMPLETE PASSAGE
   ========================================================= */

function speakPassage() {

    if (
        !speechAvailable ||
        !currentPassage
    ) {

        return;

    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            currentPassage
        );


    const selectedVoice =
        getSelectedVoice();


    if (selectedVoice) {
        utterance.voice =
            selectedVoice;
    }


    utterance.rate =
        parseFloat(
            speechRate.value
        );


    utterance.volume =
        parseFloat(
            speechVolume.value
        );


    currentUtterance =
        utterance;


    window.speechSynthesis.speak(
        utterance
    );

}


/* =========================================================
   BUILD WORD POSITION LIST
   ========================================================= */

/*
   This is the important fix.

   Every word receives:

   - its word number
   - its exact position in the passage
   - its exact ending position

   Newlines are included naturally because the positions
   come directly from the actual passage string.
*/

function buildWordList() {

    wordList = [];

    const regex =
        /\S+/g;

    let match;


    while (
        (match = regex.exec(currentPassage))
        !== null
    ) {

        wordList.push({

            word:
                match[0],

            start:
                match.index,

            end:
                match.index +
                match[0].length

        });

    }


    currentWordIndex = 0;

    lastWordTriggerIndex = -1;

}


/* =========================================================
   SPEAK ONE WORD
   ========================================================= */

function speakWordAt(index) {

    if (
        !speechAvailable ||
        index < 0 ||
        index >= wordList.length
    ) {

        return;

    }


    const word =
        wordList[index].word;


    /*
       Do not speak the same word repeatedly.
    */

    if (
        index <= lastWordTriggerIndex
    ) {

        return;

    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            word
        );


    const selectedVoice =
        getSelectedVoice();


    if (selectedVoice) {

        utterance.voice =
            selectedVoice;

    }


    utterance.rate =
        parseFloat(
            speechRate.value
        );


    utterance.volume =
        parseFloat(
            speechVolume.value
        );


    currentUtterance =
        utterance;


    window.speechSynthesis.speak(
        utterance
    );


    /*
       Mark this word as announced.
    */

    lastWordTriggerIndex =
        index;

}


/* =========================================================
   INITIALIZE WORD MODE
   ========================================================= */

function initializeWordMode() {

    buildWordList();


    wordModeStarted = true;


    /*
       Speak the first word immediately.
    */

    if (
        wordList.length > 0
    ) {

        window.speechSynthesis.cancel();


        const firstWord =
            wordList[0].word;


        const utterance =
            new SpeechSynthesisUtterance(
                firstWord
            );


        const selectedVoice =
            getSelectedVoice();


        if (selectedVoice) {

            utterance.voice =
                selectedVoice;

        }


        utterance.rate =
            parseFloat(
                speechRate.value
            );


        utterance.volume =
            parseFloat(
                speechVolume.value
            );


        currentUtterance =
            utterance;


        window.speechSynthesis.speak(
            utterance
        );


        lastWordTriggerIndex = 0;

    }

}


/* =========================================================
   WORD-BY-WORD SPEECH PROCESSING
   ========================================================= */

function updateWordByWordSpeech() {

    if (
        !wordModeStarted ||
        wordList.length === 0 ||
        testPaused
    ) {

        return;

    }


    const typedLength =
        typingArea.value.length;


    /*
       Find the word that corresponds to the current
       typing position.

       Because the complete passage is used here, this
       continues correctly through ALL 8 lines.
    */

    let activeWordIndex =
        wordList.length - 1;


    for (
        let i = 0;
        i < wordList.length;
        i++
    ) {

        if (
            typedLength <=
            wordList[i].end
        ) {

            activeWordIndex = i;

            break;

        }

    }


    currentWordIndex =
        activeWordIndex;


    /*
       Trigger the NEXT word when the user reaches
       the final three characters of the current word.

       Example:
       "computer" has 8 letters.
       Next word is triggered at character 5,
       leaving approximately 3 letters.
    */

    const currentWord =
        wordList[activeWordIndex];


    if (!currentWord) {
        return;
    }


    const triggerPosition =
        Math.max(
            currentWord.start + 1,
            currentWord.end - 3
        );


    if (
        typedLength >= triggerPosition &&
        activeWordIndex + 1 < wordList.length &&
        lastWordTriggerIndex <= activeWordIndex
    ) {

        speakWordAt(
            activeWordIndex + 1
        );

    }

}


/* =========================================================
   RESET EVERYTHING
   ========================================================= */

function resetTestState() {

    if (speechAvailable) {

        window.speechSynthesis.cancel();

    }


    clearInterval(
        timerInterval
    );

    timerInterval = null;


    testRunning = false;

    testPaused = false;

    startTime = 0;

    pausedStarted = 0;

    totalPausedTime = 0;


    wordList = [];

    currentWordIndex = 0;

    lastWordTriggerIndex = -1;

    wordModeStarted = false;


    typingArea.value = "";

    typingArea.disabled = false;


    pauseButton.textContent =
        "Pause";


    statusElement.textContent =
        "Ready";


    messageElement.textContent =
        "Your statistics will update while you type.";


    resetLiveStats();

}


/* =========================================================
   RESET LIVE STATISTICS
   ========================================================= */

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


/* =========================================================
   ELAPSED TIME
   ========================================================= */

function getElapsedSeconds() {

    if (!startTime) {
        return 0;
    }


    const now =
        performance.now();


    let elapsed =
        now -
        startTime -
        totalPausedTime;


    if (
        testPaused &&
        pausedStarted > 0
    ) {

        elapsed -=
            now -
            pausedStarted;

    }


    return Math.max(
        elapsed / 1000,
        0
    );

}


/* =========================================================
   TIMER
   ========================================================= */

function startTimer() {

    clearInterval(
        timerInterval
    );


    timerInterval =
        setInterval(
            function() {

                if (
                    !testRunning ||
                    testPaused
                ) {

                    return;

                }


                const elapsed =
                    getElapsedSeconds();


                document.getElementById(
                    "liveTime"
                ).textContent =
                    Math.floor(
                        elapsed
                    ) + "s";


                updateLiveStats();


                /*
                   Automatic finish for timed tests.
                */

                if (
                    selectedDuration !==
                    "passage"
                ) {

                    const durationSeconds =
                        parseInt(
                            selectedDuration
                        );


                    if (
                        elapsed >=
                        durationSeconds
                    ) {

                        finishTest();

                    }

                }

            },
            100
        );

}

"""

html_code += r"""

/* =========================================================
   START TEST
   ========================================================= */

function startTest(mode) {

    resetTestState();


    currentMode =
        mode;


    /*
       Get duration according to the selected mode.
    */

    if (
        mode === "normal"
    ) {

        selectedDuration =
            normalDuration.value;

    }

    else if (
        mode === "voice"
    ) {

        selectedDuration =
            voiceDuration.value;

    }

    else if (
        mode === "word"
    ) {

        selectedDuration =
            wordDuration.value;

    }


    /*
       Generate the correct number of lines.

       Normal:
       30 = 4
       60 = 8
       120 = 15
       Passage = 15

       Voice:
       same as Normal

       Word:
       30 = 4
       60 = 8
    */

    currentPassage =
        getNewPassage(
            selectedDuration
        );


    passageElement.textContent =
        currentPassage;


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


    /*
       Test title.
    */

    if (
        mode === "normal"
    ) {

        document.getElementById(
            "testTitle"
        ).textContent =
            "⌨️ Normal Typing Test";

        statusElement.textContent =
            "Normal Typing Test";

    }

    else if (
        mode === "voice"
    ) {

        document.getElementById(
            "testTitle"
        ).textContent =
            "🔊 Voice-Assisted Typing Test";

        statusElement.textContent =
            "Voice-Assisted Test";

    }

    else {

        document.getElementById(
            "testTitle"
        ).textContent =
            "🗣️ Word-by-Word Voice Test";

        statusElement.textContent =
            "Word-by-Word Voice Test";

    }


    messageElement.textContent =
        "Start typing the passage.";


    /*
       Replay is available for both voice modes.
    */

    replayButton.classList.toggle(
        "hidden",
        mode === "normal"
    );


    resetLiveStats();


    startTimer();


    /*
       Start voice behavior.
    */

    if (
        mode === "voice"
    ) {

        speakPassage();

    }


    if (
        mode === "word"
    ) {

        initializeWordMode();

    }


    typingArea.focus();

}


/* =========================================================
   CALCULATE STATISTICS
   ========================================================= */

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

        }

        else {

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


    if (
        totalChecked > 0
    ) {

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
        ? (
            correctChars / 5
          ) / minutes
        : 0;


    const typedWords =
        typed.trim() === ""
        ? []
        : typed.trim().split(/\s+/);


    const passageWords =
        currentPassage
            .replace(/\n/g, " ")
            .trim()
            .split(/\s+/);


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

        wpm:
            Math.round(
                wpm
            ),

        accuracy:
            Math.round(
                accuracy * 10
            ) / 10,

        correctChars:
            correctChars,

        incorrectChars:
            incorrectChars,

        errors:
            incorrectChars,

        correctWords:
            correctWords,

        time:
            Math.floor(
                elapsed
            ),

        totalChars:
            totalTyped

    };

}


/* =========================================================
   UPDATE LIVE STATISTICS
   ========================================================= */

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
        stats.accuracy +
        "%";


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


/* =========================================================
   TYPING INPUT
   ========================================================= */

typingArea.addEventListener(
    "input",
    function() {

        if (!testRunning) {

            return;

        }


        updateLiveStats();


        /*
           Word-by-word speech.

           This now uses the exact positions of all words
           in the entire passage.
        */

        if (
            currentMode === "word"
        ) {

            updateWordByWordSpeech();

        }


        /*
           Complete Passage mode is still retained
           for Normal and Voice-Assisted modes.
        */

        if (
            selectedDuration === "passage" &&
            typingArea.value.length >=
            currentPassage.length
        ) {

            finishTest();

        }

    }
);


/* =========================================================
   PAUSE / RESUME
   ========================================================= */

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


        if (speechAvailable) {

            window.speechSynthesis.pause();

        }


        typingArea.disabled = true;

    }

    else {

        const now =
            performance.now();


        totalPausedTime +=
            now -
            pausedStarted;


        pausedStarted = 0;

        testPaused = false;


        pauseButton.textContent =
            "Pause";


        if (
            currentMode === "normal"
        ) {

            statusElement.textContent =
                "Normal Typing Test";

        }

        else if (
            currentMode === "voice"
        ) {

            statusElement.textContent =
                "Voice-Assisted Test";

        }

        else {

            statusElement.textContent =
                "Word-by-Word Voice Test";

        }


        messageElement.textContent =
            "Test resumed.";


        if (speechAvailable) {

            window.speechSynthesis.resume();

        }


        typingArea.disabled = false;

        typingArea.focus();

    }

}


/* =========================================================
   FINISH TEST
   ========================================================= */

function finishTest() {

    if (!testRunning) {

        return;

    }


    testRunning = false;


    clearInterval(
        timerInterval
    );


    timerInterval = null;


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
        stats.accuracy +
        "%";


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
        stats.time +
        "s";


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


    saveHistory(
        stats
    );


    showHistory();

}

"""

html_code += r"""

/* =========================================================
   REPLAY BUTTON
   ========================================================= */

replayButton.addEventListener(
    "click",
    function() {

        if (
            currentMode === "voice" &&
            currentPassage
        ) {

            speakPassage();

        }


        if (
            currentMode === "word" &&
            wordList.length > 0
        ) {

            /*
               Replay the currently active word.
            */

            if (
                speechAvailable
            ) {

                window.speechSynthesis.cancel();

                const word =
                    wordList[currentWordIndex]
                        ? wordList[currentWordIndex].word
                        : wordList[0].word;


                const utterance =
                    new SpeechSynthesisUtterance(
                        word
                    );


                const selectedVoice =
                    getSelectedVoice();


                if (selectedVoice) {

                    utterance.voice =
                        selectedVoice;

                }


                utterance.rate =
                    parseFloat(
                        speechRate.value
                    );


                utterance.volume =
                    parseFloat(
                        speechVolume.value
                    );


                currentUtterance =
                    utterance;


                window.speechSynthesis.speak(
                    utterance
                );

            }

        }

    }
);


/* =========================================================
   NORMAL START
   ========================================================= */

normalStart.addEventListener(
    "click",
    function() {

        startTest(
            "normal"
        );

    }
);


/* =========================================================
   VOICE START
   ========================================================= */

voiceStart.addEventListener(
    "click",
    function() {

        startTest(
            "voice"
        );

    }
);


/* =========================================================
   WORD-BY-WORD START
   ========================================================= */

wordStart.addEventListener(
    "click",
    function() {

        startTest(
            "word"
        );

    }
);


/* =========================================================
   PAUSE BUTTON
   ========================================================= */

pauseButton.addEventListener(
    "click",
    function() {

        togglePause();

    }
);


/* =========================================================
   FINISH BUTTON
   ========================================================= */

finishButton.addEventListener(
    "click",
    function() {

        finishTest();

    }
);


/* =========================================================
   RESTART BUTTON
   ========================================================= */

restartButton.addEventListener(
    "click",
    function() {

        resetTestState();


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


/* =========================================================
   TRY ANOTHER TEST
   ========================================================= */

anotherTest.addEventListener(
    "click",
    function() {

        resetTestState();


        results.classList.add(
            "hidden"
        );


        testArea.classList.add(
            "hidden"
        );


        openingScreen.classList.remove(
            "hidden"
        );


        currentPassage = "";

        passageElement.textContent = "";


        typingArea.value = "";

        typingArea.disabled = false;


        normalDuration.focus();

    }
);


/* =========================================================
   HISTORY
   ========================================================= */

function getHistory() {

    try {

        return JSON.parse(
            localStorage.getItem(
                "accessibleTypingHistory"
            )
        ) || [];

    }

    catch (error) {

        return [];

    }

}


/* =========================================================
   SAVE HISTORY
   ========================================================= */

function saveHistory(stats) {

    const history =
        getHistory();


    let modeName =
        "Normal";


    if (
        currentMode === "voice"
    ) {

        modeName =
            "Voice";

    }


    if (
        currentMode === "word"
    ) {

        modeName =
            "Word-by-Word Voice";

    }


    history.unshift({

        mode:
            modeName,

        wpm:
            stats.wpm,

        accuracy:
            stats.accuracy,

        time:
            stats.time

    });


    const limited =
        history.slice(
            0,
            10
        );


    try {

        localStorage.setItem(
            "accessibleTypingHistory",
            JSON.stringify(
                limited
            )
        );

    }

    catch (error) {

        console.log(
            "History could not be saved."
        );

    }

}


/* =========================================================
   SHOW HISTORY
   ========================================================= */

function showHistory() {

    const history =
        getHistory();


    const body =
        document.getElementById(
            "historyBody"
        );


    body.innerHTML = "";


    if (
        history.length === 0
    ) {

        const row =
            document.createElement(
                "tr"
            );


        row.innerHTML =
            "<td colspan='4'>No previous tests.</td>";


        body.appendChild(
            row
        );


        return;

    }


    history.forEach(
        function(item) {

            const row =
                document.createElement(
                    "tr"
                );


            row.innerHTML =

                "<td>" +
                item.mode +
                "</td>" +

                "<td>" +
                item.wpm +
                "</td>" +

                "<td>" +
                item.accuracy +
                "%" +
                "</td>" +

                "<td>" +
                item.time +
                "s" +
                "</td>";


            body.appendChild(
                row
            );

        }
    );

}


/* =========================================================
   INITIAL HISTORY
   ========================================================= */

showHistory();


</script>

</body>

</html>
"""


# ============================================================
# DISPLAY COMPLETE APPLICATION
# ============================================================

components.html(
    html_code,
    height=1400,
    scrolling=True
)
