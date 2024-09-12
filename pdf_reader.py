import pyttsx3
import PyPDF2
from gtts import gTTS
import os


# TextToAudio class has the functionalities to read the file or to save the audio file based on the pdf file
class TextToAudio:
    def __init__(self,file) -> None:
        self.file = file
        
    # extract text is used to extract the text frm the pdf file
    def extract_text(self) -> list[str]:
        
        # text is used to store the extracted text from the pdf file
        text = []
        if os.path.exists(self.file) and os.path.getsize(self.file) > 0:
            with open(self.file,"rb") as file:
                reader = PyPDF2.PdfReader(file)
                no_of_pages = len(reader.pages)
            
                for page_number in range(no_of_pages):
                    lines = reader.pages[page_number].extract_text()
                    text.append(lines)
        else:
            return ["file not found or it is an empty file" ]   
          
        return text
               
    # read_aloud function can read the pdf file  
    def read_aloud(self) -> None:
    
        text = self.extract_text()
        engine = pyttsx3.init()
        for line in text:
            text = line
            engine.say(text)
            engine.runAndWait()
            
    # save save the audio file of the given pdf file    
    def save_audio_file(self) -> None:
        
        text = self.extract_text()
        combined_text = " ".join(text)
        speech = gTTS(text=combined_text, lang="en", slow=False)
        speech.save(self.file+".mp3")
        print(f"audio file has been saved as {self.file}.mp3")
        
        
        
if __name__ == "__main__":
    
    file = input("enter the pdf file to read")
    if ".pdf" not in file:
        print("This is not a valid pdf file extension")
    else:
        audio = TextToAudio("Data science roadmap 2024.pdf")
        choice = input("What do you want perform \n 1.read file \n 2.save it as an audio file")
        if choice == "1":
            audio.read_aloud()
        elif choice == "2":
            audio.save_audio_file()
        else:
            print("please enter the valid operation")



            
            
            


