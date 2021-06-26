import os
import shutil
def sort_using_extention(file_path,request):
    global path
    src = file_path
    print("inside func")
    try:
        if(request=="mp3"):
            path = file_path + "/music"
            os.mkdir(file_path + "/music")
        elif(request == "mp4"):
            path = file_path + "/video"
            os.mkdir(file_path + "/video")
        elif (request == "pptx"):
            path = file_path + "/ppts"
            os.mkdir(file_path + "/ppts")
        elif (request == "txt"):
            path = file_path + "/text"
            print("hii")
            os.mkdir(file_path + "/text")
        elif (request == "jpg" or request == "jpeg" or request == "png"):
            path = file_path + "/image"
            os.mkdir(file_path + "/image")
        elif (request == "doc" or request == "docx"):
            path = file_path + "/document"
            os.mkdir(file_path + "/document")
        elif (request == "pdf" ):
            path = file_path + "/pdf"
            os.mkdir(file_path + "/pdf")
        elif (request == "xlsx" ):
            path = file_path + "/excel"
            os.mkdir(file_path + "/excel")
    except FileExistsError:
        print("file exits")

    for files in os.listdir(src):
        fextension = files.split(sep=".")
        try:
            if(fextension[len(fextension)-1] == request):
                print(f'{src}/{fextension[0]}.{fextension[len(fextension)-1]}')
                print(path)
                shutil.move(str(f'{src}/{fextension[0]}.{fextension[len(fextension)-1]}'), path)
        except IndexError:
            continue
