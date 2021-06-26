import pickle
import os.path
from typing import List, Any
from making_db import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from tkinter import messagebox
from tkinter import *
import os

class MyDrive():
    thisList = []

    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/drive']
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

    def list_files(self, folder_id):
        # Call the Drive v3 API

        query = f"parents= '{folder_id}'"
        results = self.service.files().list(
             q=query,
             fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        listing = Toplevel()
        listing.title('List of Files')
        listing.resizable(width=True, height=True)

        if not items:
            print('No files found.')
            listing.destroy()
            messagebox.showinfo('No File Found', 'No Files in Backup folder')

        else:
            print('Files:')
            for item in items:
                a = u'{0} ({1})'.format(item['name'], item['id'])
                lbl = Label(listing, text=a)
                lbl.pack()
            Button(listing, text='OK', command=listing.destroy).pack()
        listing.mainloop()



    def upload_file(self, filename, path, folder_id):
        media = MediaFileUpload(f"{path}/{filename}", resumable=True)

        response = self.service.files().list(
                                        q=f"name='{filename}' and parents='{folder_id}'",
                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=None).execute()
        if len(response['files']) == 0:
            file_metadata = {
                'name': filename,
                'parents': [folder_id]
            }
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"A new file was created {file.get('id')}")

        else:
            for file in response.get('files', []):
                # Process change

                update_file = self.service.files().update(
                    fileId=file.get('id'),
                    media_body=media,
                ).execute()
                print(f'Updated File')

    def download_file(self,):
        return


def main1(file_path,folder_id,request,zip_File_name):
    files = os.listdir(file_path)
    my_drive = MyDrive()

    if(request == 'upload'):
        if (folder_id!=""):
            MyDrive.thisList.append(folder_id)
        for item in files:
            my_drive.upload_file(item, file_path, MyDrive.thisList[len(MyDrive.thisList)-1])
        messagebox.showinfo('upload status', 'your file is uploaded to Drive succesfully')
    elif(request == 'list_files'):
        if (folder_id!=""):
            MyDrive.thisList.append(folder_id)
        record=put_in_back('get_folder_id',zip_File_name,'','','')
        print(record)
        if(record==[]):
            my_drive.list_files(folder_id)
        else :
            my_drive.list_files(record[0][0])

    else:
        if (folder_id!=""):
            MyDrive.thisList.append(folder_id)
        for item in files:
            if(item == zip_File_name):
                my_drive.upload_file(item, file_path, MyDrive.thisList[len(MyDrive.thisList)-1])
        messagebox.showinfo('upload status', 'your file is uploaded to Drive succesfully')

if __name__ == '__main__':
    main1()
