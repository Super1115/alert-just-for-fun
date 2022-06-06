from playsound import playsound
import gtts 

msg = input("Alert Message:")
read_msg = gtts.gTTS(msg)
read_msg.save("Alert_Message.mp3")


for i in range(10):
    playsound("Alert_Message.mp3")
    playsound("alert.wav")
