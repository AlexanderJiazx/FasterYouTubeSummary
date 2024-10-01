from get_video_summary import get_video_summary
import os  

url = input("Insert the URL of the YouTube video: ")
api_key=os.environ.get("GROQ_API_KEY")
summary = get_video_summary(url, api_key, return_summary_only=False)
# return_summary_only=True
  
print(summary)