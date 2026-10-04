import json
import glob
import pandas as pd

audio_files = sorted(glob.glob("Streaming_History_Audio_*.json"))

for name in audio_files:
    with open(name, encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    new_name = name.replace(".json", ".csv")
    df.to_csv(new_name, index=False, encoding="utf-8")
    print(f"Converted: {name} -> {new_name}")