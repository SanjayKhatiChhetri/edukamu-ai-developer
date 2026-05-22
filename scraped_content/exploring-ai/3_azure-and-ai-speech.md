## Azure and AI Speech

In not-so-distant future, your morning routine might be significantly different from what you’re used to. Actually, it might not be that much different, but it will certainly be more personalized for your taste. Let’s use our imagination once again…

The day begins with a personalized wake-up call from a smart assistant, utilizing Natural Language Processing to understand the user's preferences. As the individual get up, AI-driven sensors in the bedroom assess sleep quality, providing insights for optimal adjustments.

Moving into the kitchen, a smart coffee maker, integrated with AI, anticipates the user's caffeine needs based on historical data and weather conditions. Simultaneously, an NLP-powered virtual assistant provides a dynamic briefing on the day's schedule, considering traffic updates and reminders.

The bathroom experience is elevated with AI-infused mirrors offering personalized skincare recommendations and health insights. As the user gets dressed, a smart wardrobe suggests outfit options based on the day's agenda and current fashion trends, employing machine learning algorithms…

These are but a few examples on how NLP and other AI technologies can enhance our lives. It’s, of course, up to the user to choose which services they’ll eventually want to enable, but one thing is certain: Microsoft Azure is the go-to tool for developing them all.

It’s time to get acquainted with Microsoft Azure’s AI Speech capabilities.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to AI Speech
</edukamu-collapse-hidden-title>

AI speech capabilities enable us to manage home and auto systems with voice instructions, get answers from computers for spoken questions, generate captions from audio, and much more.

To enable this kind of interaction, the AI system must support two capabilities:
* **Speech recognition** - the ability to detect and interpret spoken input
* **Speech synthesis** - the ability to generate spoken output

**Azure AI Speech** provides speech to text and text to speech capabilities through speech recognition and synthesis. You can use prebuilt and custom Speech service models for a variety of tasks, from transcribing audio to text with high accuracy, to identifying speakers in conversations, creating custom voices, and more.

### Speech Recognition and Synthesis

**Speech recognition** takes the spoken word and converts it into data that can be processed - often by transcribing it into text. The spoken words can be in the form of a recorded voice in an audio file, or live audio from a microphone. Speech patterns are analyzed in the audio to determine recognizable patterns that are mapped to words. To accomplish this, the software typically uses multiple models, including:
* An *acoustic* model that converts the audio signal into phonemes (representations of specific sounds).
* A *language* model that maps phonemes to words, usually using a statistical algorithm that predicts the most probable sequence of words based on the phonemes.

The recognized words are typically converted to text, which you can use for various purposes, such as:
* Providing closed captions for recorded or live videos
* Creating a transcript of a phone call or meeting
* Automated note dictation
* Determining intended user input for further processing

**Speech synthesis** is concerned with vocalizing data, usually by converting text to speech. A speech synthesis solution typically requires the following information:
* The text to be spoken
* The voice to be used to vocalize the speech

To synthesize speech, the system typically *tokenizes* the text to break it down into individual words, and assigns phonetic sounds to each word. It then breaks the phonetic transcription into *prosodic* units (such as phrases, clauses, or sentences) to create phonemes that will be converted to audio format. These phonemes are then synthesized as audio and can be assigned a particular voice, speaking rate, pitch, and volume.

You can use the output of speech synthesis for many purposes, including:
* Generating spoken responses to user input
* Creating voice menus for telephone systems
* Reading email or text messages aloud in hands-free scenarios
* Broadcasting announcements in public locations, such as railway stations or airports

By the way, have you already encountered such services in your day-to-day life? In many areas, AI-enabled technologies are already (in early 2024) widely in use.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Microsoft Azure offers both speech recognition and speech synthesis capabilities through Azure AI Speech service, which includes the following application programming interfaces (APIs):
* The **Speech to text** API
* The **Text to speech** API

Next, we’ll find out a bit more about these services.

In case you’ve forgotten what APIs are, here’s a hint: They are like bridges connecting services.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Speech to Text API
</edukamu-collapse-hidden-title>

To use Azure AI Speech in an application, you must create an appropriate resource in your Azure subscription. You can choose to create either of the following types of resource:
* A **Speech** resource - choose this resource type if you only plan to use Azure AI Speech, or if you want to manage access and billing for the resource separately from other services.
* An **Azure AI services** resource - choose this resource type if you plan to use Azure AI Speech in combination with other Azure AI services, and you want to manage access and billing for these services together.

### Speech to Text (API)

You can use Azure AI Speech to text API to perform real-time or batch transcription of audio into a text format. The audio source for transcription can be a real-time audio stream from a microphone or an audio file.

The model that is used by the Speech to text API, is based on the Universal Language Model that was trained by Microsoft. The data for the model is Microsoft-owned and deployed to Microsoft Azure. The model is optimized for two scenarios, conversational and dictation. You can also create and train your own custom models including acoustics, language, and pronunciation if the pre-built models from Microsoft do not provide what you need.

### Real-time Transcription

Real-time speech to text allows you to transcribe text in audio streams. You can use real-time transcription for presentations, demos, or any other scenario where a person is speaking.

In order for real-time transcription to work, your application will need to be listening for incoming audio from a microphone, or other audio input source such as an audio file. Your application code streams the audio to the service, which returns the transcribed text.

### Batch Transcription

Not all speech to text scenarios are real time. You might have audio recordings stored on a file share, a remote server, or even on Azure storage. You can point to audio files with a shared access signature (SAS) URI and asynchronously receive transcription results.

Batch transcription should be run in an asynchronous manner because the batch jobs are scheduled on a best-effort basis. Normally a job will start executing within minutes of the request but there is no estimate for when a job changes into the running state.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Text to Speech (API)
</edukamu-collapse-hidden-title>

The text to speech API enables you to convert text input to audible speech, which can either be played directly through a computer speaker or written to an audio file.

### Speech Synthesis Voices

When you use the text to speech API, you can specify the voice to be used to vocalize the text. This capability offers you the flexibility to personalize your speech synthesis solution and give it a specific character.

The service includes multiple pre-defined voices with support for multiple languages and regional pronunciation, including standard voices as well as neural voices that leverage neural networks to overcome common limitations in speech synthesis with regard to intonation, resulting in a more natural sounding voice. You can also develop custom voices and use them with the text to speech API.

### Supported Languages

Both the speech to text and text to speech APIs support a variety of languages. You can use the links below to find details about the supported languages:
* Speech to text languages.
* Text to speech languages.

If you have an Azure subscription, you can use Speech Studio to explore the capabilities of Azure AI Language's Question Answering feature.

Launch the exercise and follow the instructions.

<edukamu-button url="https://go.microsoft.com/fwlink/?linkid=2250148">Launch Exercise (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br>


Speech recognition is concerned with taking the spoken word and converting it into text, while speech synthesis is the process of converting text to audible speech. Both of these tasks are supported by Azure AI Speech.

During this micro degree, we’ll get to work with Azure AI Speech as well. Don’t forget that you can always explore the platform on your own, if you have an active Azure subscription!

It’s time for the last exercise of this unit.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure AI Speech
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll.yaml" id="wm63ocx3z4t40u9b"/>
<br>
<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll-2.yaml" id="nzan8xs98hwoq7ey"/>
<br>
<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll-3.yaml" id="1ffi98nh519u0mt6"/>
<br>
<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll-4.yaml" id="va466s1nte8dj15h"/>
<br>
<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll-5.yaml" id="2n42vq783g0mkj5i"/>
<br>
<edukamu-text-poll url="/exercises/module3/azure-and-ai-text-poll-6.yaml" id="pys9145zn8pcp06n"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/azure-and-ai-speech?question=wm63ocx3z4t40u9b">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


It’s evening, and our individual is about to enter their apartment after a productive day at work. Returning home, the AI-enhanced evening routine unfolds. Smart home devices anticipate preferences, adjusting lighting, temperature, and entertainment choices. AI-driven cooking assistants propose recipes based on dietary preferences and available ingredients, simplifying meal planning.

As bedtime approaches, AI-powered sleep aids create a serene atmosphere, adjusting lighting and playing calming sounds to enhance relaxation. Sleep patterns are monitored throughout the night, contributing to the continuous improvement of the AI's understanding of the user's well-being.

In this example, describing a daily routine enhanced by AI and NLP capabilities, the technologies seamlessly integrate into daily life, offering personalized, efficient, and intuitive experiences at every step.

But wait… Such a routine sounds a tad passive, doesn’t it? Is AI really here just to adjust temperatures and react to our immediate needs? Of course not! In fact, it’s already capable of much more! In a single word, the key ability here is to *generate* instead of just reacting, which is exactly what Generative AI does.

Congratulations for reaching the end of the third unit! Feel free to move on to the fourth one, in which we’ll focus on generative AI. But don’t forget to rest and recap!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
