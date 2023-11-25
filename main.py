from transformers import pipeline 
import pyttsx3
from PyPDF2 import PdfReader
from  psutil import cpu_percent
from playsound import playsound
import re 
import sys
import os  


def cpu_use():
   """ check cpu usage """
   cpu_usage = cpu_percent(interval=1)
   return int(cpu_usage)

def remove_non_printable(input_string:str) -> str:
   printable_pattern = re.compile(r'^ -~]+')
   cleaned_string = printable_pattern.sub('',input_string)
   return cleaned_string 


def extract_text_from_pdf(filename:str)->str:
   """ Extract text from pdf files"""
   text=''
   with open(filename,'rb') as file: 
      pdf_reader = PdfReader(file)
      for page in pdf_reader.pages:
         
         text += page.extract_text()
         
   filter_text = remove_non_printable(text)
   return filter_text

 
def split_text(text:str)->list[str]:
   """ Split text in chunks"""
   # maximum size of each chunk split 
   max_chunk_size = 4000
   chunks = []
   current_chunk = ""
   #split the string using . delimeter 
   
   for sentence in text.split("."):
      # if stored sentence and new sentence length is less then max_chun size
      if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
      else:
            # append the current_chunk
            chunks.append(current_chunk.strip())
            
            # reintialize the current_chunk to sentence.
            current_chunk = sentence + "."
            
   # if any of strings chunks left then append 
   if current_chunk:
      chunks.append(current_chunk.strip())
   # return the stored string chunks
   return chunks


def genrate_summary(text:str, aim="summarization", model="facebook/bart-large-cnn")->str:
   """ Generate summary using hugging face model"""
   input_chunks=split_text(text)
   output_chunks=[]
   
   if len(input_chunks) > 30:
      return "input limit overflow"
   
   # call the llm model using pipeline
   summarizer = pipeline( aim , model)
   # loop through each chunk the pass it to llm mode it will return sumarize 
   # form of input text
   for i , chunk in enumerate(input_chunks):
      print(i)
      response = summarizer(chunk,do_sample=False)
      summary=response[0]['summary_text']
      output_chunks.append(summary.strip())
      
      # check cpu uses if cpu use is greater then 95 means it so power consuming
      # for cpu to do these llm tasks 
      cpu_limit = cpu_use()
      # if > 95 quit the program and return whatever text we have 
      if cpu_limit > 95:
         print("Cpu is exceded it's limit")
         return "".join(output_chunks)
   # if every thing goes find give full sumarray text 
   return "".join(output_chunks)


# it will convert text into speech 
def pytt_txt_speech(summary:str)->bool:
   """ convert text to speech using pyttsx3"""
   try:
      speaker=pyttsx3.init()
      voices = speaker.getProperty('voice')
      speaker.setProperty('voice', voices) #changing index changes voices but ony 0 and 1 are working here
      speaker.setProperty('rate', 160)    # Speed percent (can go over 100)
      speaker.setProperty('volume', 0.5)
      speaker.say(summary)
      #time.sleep(0.2)
      speaker.runAndWait()
      return True 
   except Exception as e:
      print(e)
      return False

def gtt_txt_speech(summary:str,filename="summary.mp3")->bool:
   """ Convert text to speech using gtts"""
   try:
      myobj = gTTS(text=summary , lang='en', slow=False)
      myobj.save(filename)
      playsound(filename)
      return True 
   except Exception as e:
      print(e)
      return False 

def main():
   argument = sys.arg
   len_arg = len(argument)
   if len(len_arg) == 2:
      path = argument[1].strip()
      if os.path.exists(path):
         # extracted text from pdf file
         text=extract_text_from_pdf(filename)
         
         #genrated summary using hugging face model
         summary=genrate_summary(text)
         # convert text to speech
         if not pytt_text_speech(summary):
            gtt_txt_speech(summary)
            
if __name__ == "__main__":
   main()

## Done ....


