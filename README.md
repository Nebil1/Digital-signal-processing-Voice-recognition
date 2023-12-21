# Digital-signal-processing-Voice-recognition
python voice recognition system

![image](https://github.com/Nebil1/Digital-signal-processing-Voice-recognition/assets/99560401/112e2701-a5d5-4e8a-a57c-2f5062b273bc)

                                              Objective

 General Objective:
The general objective of this project is to develop a method to implement a voice recognition system using python. 

 Specific Objectives:
1. Investigate the most commonly used techniques and parameters for voice recognition. 
2. Design and develop an algorithm for voice recognition.
3.  Validate the developed algorithm in terms of performance and accuracy.
4. Implement the algorithm in an application that allows users to interact with the system.


Methodology

The methodology for this project will involve the use of both theoretical analysis and practical implementation to demonstrate the effectiveness of speech recognition module. The methodology for this project can be broken down into the following steps:

1. **Data collection**: The first step in developing a voice recognition system is to collect a large dataset of speech samples. This dataset should include a wide range of voices, accents, and languages to ensure the system can accurately recognize speech from a diverse population.
2. **Pre-processing**: Once the data is collected, it needs to be preprocessed to prepare it for analysis. This involves cleaning and normalizing the data, removing any irrelevant information, and ensuring that the data is in a suitable format for analysis.
3. **Model Selection**: Many different libraries can be used for voice recognition, including neural Speech recognition, PyAudio, Pocket Sphinx and some others. The most appropriate model will depend on the size and complexity of the dataset, as well as the specific requirements of the project.
4. **Model testing**: The model needs to be tested on a separate dataset to evaluate its accuracy and performance. This testing phase should include both quantitative metrics, such as accuracy and precision, as well as qualitative evaluations, such as listening to transcriptions and identifying errors.
5. **Model Refinement**: Based on the results of the testing phase, the model may need to be refined and retrained. This can involve adjusting the model parameters, collecting additional data, or modifying the feature extraction process.
Simulation and discussion

Step 1: Installing and importing the necessary libraries
                  
 ```                 
import sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
 ```


 Step 2:  Getting a reference to a pyttsx3.Engine instance

  An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3Engine instance. During construction, the engine initializes a pyttsx3.driver.DriverProxy object responsible for loading a speech engine driver implementation from the pyttsx3.drivers module. After construction, an application uses the engine object to register and unregister event callbacks; produce and stop speech; get and set speech engine properties; and start and stop event loops.
```
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
```

 Step 3:  defining different types of functions necessary for the implementation.

Our functions enables us to break down or decompose a problem into smaller chunks, each of which performs a particular task.

 speak(audio):This method returns the voice version of any string that is provided as argument.

 wishMe():This method returns what the code has to reply in the first place when it begin running. like getting the exact time when the program start running and it reply gretting message according to the time.
takeCommand(): This is the place where all the magics comes into the place,the Speech_recognitionmodule will play its role. The three builtin functions of the Speech_recognition module: Recognizer(), Microphone() and Recognize_google()will play a significant roles.This function returns the recognized speech as query.
performCommand():This function  performs the required thing after it takes the query tha we got from takeCommand() method as an argument.It checks differentifelse statements and perform the one that matches the query that we got from our takeCommand() function.
sendMessage(value): This function sends the text to telegram group that is given as an argument.
randomGenerator():This function generates random integer between 0 and 4 inclusively , and returns the string version of it.
Step 4: The built in method ***”main”*** will finish our steps as it is an entry point of our python code when it starts running.
```
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        performCommand(query)
```

Conclusion

In conclusion, voice recognition technology has come a long way in recent years and has become an increasingly important tool in our daily lives. From our phones and computers to our cars and home appliances, voice recognition allows us to interact with technology more naturally and intuitively. However, while the technology has made great strides, there is still much work to be done in terms of accuracy, accessibility, and inclusivity.

One of the main challenges facing voice recognition is overcoming the limitations of current algorithms and models. As machine learning and artificial intelligence continue to evolve, we can expect to see significant improvements in accuracy and reliability. In addition, efforts to improve accessibility and inclusivity are crucial to ensuring that everyone can benefit from this technology, regardless of age, language, or ability.

Despite these challenges, the potential benefits of voice recognition technology are clear. By enabling hands-free operation, improving accessibility for those with disabilities, and streamlining communication and interaction with technology, voice recognition has the potential to transform the way we live, work, and communicate. As we continue to explore the possibilities of this technology, it is important to remain mindful of its limitations and work towards developing solutions that are both effective and inclusive.


