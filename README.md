<img src="https://dl.dropboxusercontent.com/s/izd26d6nc4r28yg/Insight_Logo.png?dl=0"
     alt="Insight Logo"
     style="margin-left: auto; margin-right: auto; display: block;" />

**Website URL**: https://insight-app.azurewebsites.net
<br>
**mp3 audio file used in the demo (Franklin Roosevelt's First Inaugurial Address)**: https://drive.google.com/file/d/1e6LBN94uKS0QAN2vE14BgNcNaUtzs1XG/view?usp=sharing
<br>
**Demo Video**: https://youtu.be/D54Mww7hRBc

This application was developed with the Python Flask web framework and is hosted on Azure.

Utilizing the [**Symbl.ai API**](https://symbl.ai/), text can extracted from the user's audio file to the built-in text editor on the webpage. The user can also view augmented reality 3D model's directly in their browser (powered by the [**Echo 3D API**](https://www.echo3d.co/) and [**Google Scene Viewer**](https://developers.google.com/ar/develop/java/scene-viewer).

##  Important :exclamation:
On the Notes page, it takes some time to upload audio files and it varies based on the length of the audio file. With a short audio file such as the demo audio file on GitHub (~30 seconds), I recommend allowing around 1 minute to upload. This is due to the processing time with the Symbl API to extract text from the audio file.

**Accepted Audio Formats**: .wav, .mp3, .mpeg