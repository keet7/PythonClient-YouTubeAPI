from googleapiclient.discovery import build

api_key = 'AIzaSyAfvlX6DvJfh-9x1fYUYKedGVcE3uabRVs'
#one way to keep the secrets safe is by creating 
#env variables
youtube = build('youtube', 'v3', developerKey=api_key)


request = youtube.channels().list(
  part='statistics',
  forUsername='KunalKushwaha'
)

response = request.execute()

print(response)