import wget

file_url = input("Enter the URL of the file to download: ")
file_name = wget.download(file_url)