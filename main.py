import os
import subprocess
from threading import Thread
from pyrogram import Client
import time

api_id = 11405252
api_hash = "b1a1fc3dc52ccc91781f33522255a880"
bot_token2 = "6593397412:AAFmJ8Hj9jnZuvLs_rLcu63bQwCp0EV829w"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token2)

up = {"ytdl": False, 'Total': 0}

links = [
   # "https://youtube.com/playlist?list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl&si=w7qSDmBdsGWslf4u"
    "https://www.pornhub.com/playlist/85569291"
]

def ytdlpp(link):
    command = (
        'yt-dlp --downloader aria2c --match-filter "duration>180"'
        ' --max-downloads 200 -N 10 -o "%(title)s.%(ext)s" -f "(mp4)[height=?720]"'
        ' --write-thumbnail --embed-metadata ' + link
    )
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Download Completed {link}")
    time.sleep(120)
    up["ytdl"] = True
async def main():
    async with app:
        for link in links:
            dl = Thread(target=ytdlpp, args=(link,))
            dl.start()
            upl = True
            while upl:
                print(f"Downloading {link}")
                sts = await app.send_message(-1002034630043, f"Downloading {link}")
                time.sleep(6)
                while upl:
                    for filename in os.listdir():
                        if filename.endswith(".mp4"):
                            try:
                                command1 = f'vcsi "{filename}" -g 2x2 --metadata-position hidden -o "{filename.replace(".mp4",".png")}"'
                                result = subprocess.run(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                                await app.edit_message_text(-1002034630043, sts.id, f"Uploaded Videos:{up['Total']}\nUploading {filename}")
                                video = await app.send_video(-1002034630043, video=filename, caption=filename.replace(".mp4",""), thumb=filename.replace(".mp4",".png"), supports_streaming=True, progress=progress)
                                up['Total'] += 1
                                await app.edit_message_text(-1002034630043, sts.id, f"Uploaded Videos:{up['Total']}\nUploaded {filename}")
                                try:
                                    command2 = f'rm -f "{filename}" "{filename.replace(".mp4", ".png")}"' if os.name != 'nt' else f'del /Q "{filename}" "{filename.replace(".mp4", ".png")}"'
                                    result = subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                                    await app.edit_message_text(-1002034630043, sts.id, f"Uploaded Videos:{up['Total']}\nCleared {filename}")
                                except:
                                    pass
                            except Exception as e:
                                print(e)
                        if up["ytdl"] == True:
                            upl = False


print("Bot Started")
app.run(main())
