import whisper
import json

model = whisper.load_model("small")
result = model.transcribe(audio ="audios/sample.mp3",
                          language = "hi",
                          task = "translate",
                          word_timestamps = False)
print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunk = {
        "id": segment["id"],
        "seek": segment["seek"],
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"],
       
    }
    chunks.append(chunk)
    print(chunks)

    with open("output.json", "w") as f:
        json.dump(chunks, f)
# with open("output.json", "w", encoding="utf-8") as f:
#     f.write(str(result))