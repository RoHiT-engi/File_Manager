import os
def new_file_creation(request,dir_path,file_name):
    if(request == "text"):
        open(f'{dir_path}/{file_name}.txt','w+')
        os.startfile(f'{dir_path}/{file_name}.txt')
    elif(request == "ppt"):
        open(f'{dir_path}/{file_name}.pptx', 'w+')
        os.startfile(f'{dir_path}/{file_name}.pptx')
    elif (request == "Word"):
        open(f'{dir_path}/{file_name}.docx', 'w+')
        os.startfile(f'{dir_path}/{file_name}.docx')
    elif (request == "Excel"):
        open(f'{dir_path}/{file_name}.xlsx', 'w+')
        os.startfile(f'{dir_path}/{file_name}.xlsx')
    elif (request == "bitmap image"):
        open(f'{dir_path}/{file_name}.bmp', 'w+')
        os.startfile(f'{dir_path}/{file_name}.bmp')
    elif (request == "New Folder"):
        os.mkdir(f'{dir_path}/{file_name}')
        os.startfile(f'{dir_path}/{file_name}')
    elif (request == "ZIP"):
        open(f'{dir_path}/{file_name}.zip', 'w+')
        os.startfile(f'{dir_path}/{file_name}.zip')