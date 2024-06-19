import requests
import os

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, 'wb') as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)
    print("File downloaded successfully!")

def get_unique_file_name(path, tinh, lop, nam):
    base_name = f'{tinh} - {lop} - {nam}'
    name_file = f'{base_name}.pdf'
    i = 1
    while os.path.exists(os.path.join(path, name_file)):
        name_file = f'{base_name} ({i}).pdf'
        i += 1
    return name_file

if __name__ == '__main__':
    # Thay 'your_drive_link' bằng liên kết Google Drive thực tế của bạn
    drive_link = 'https://drive.google.com/open?id=19j5YtfftCLLeOfEh99GdqOpUOTCFI8sp'
    file_id = drive_link.split('id=')[1]
    destination_path = 'abc.pdf'

    download_file_from_google_drive(file_id, destination_path)
