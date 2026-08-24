import whisper
import json
import os
model = whisper.load_model("small")

audios = os.listdir("audios")
for audio in audios:
    print(audio)
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)
        # result = model.transcribe(audio =f"audios/{audios}.mp3",
        result = model.transcribe(audio =f"audios/sample.mp3",

                                  language = "hi",
                                  task = "translate",
                                  word_timestamps = False)

        chunks = []
        for segment in result["segments"]:
            chunk = {
            "number": number,
            "title": title,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"],
       
            }
            chunks.append(chunk)

        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}    
        os.makedirs("jsons", exist_ok=True)
        with open(f"jsons/{audio}.json", "w") as f:
                json.dump(chunks_with_metadata, f)

            