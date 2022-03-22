import requests
import shutil
import zipfile


# create zip with files
def write_zip():
    with zipfile.ZipFile('files1.zip', 'w') as my_zip:
        my_zip.write('test.txt')
        my_zip.write('test.png')


# create zip file compressed
def write_compressed_zip():
    with zipfile.ZipFile('files_compressed.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write('test.txt')
        my_zip.write('test.png')


# extract all files
def get_zip_info():
    with zipfile.ZipFile('files.zip', 'r') as my_zip:
        print(my_zip.getinfo(name='test.txt'))
        print(my_zip.infolist())


# read names of the files
def read_zip_file_names():
    with zipfile.ZipFile('files.zip', 'r') as my_zip:
        print(my_zip.namelist())


# extract all files
def extract_zip_files():
    with zipfile.ZipFile('files.zip', 'r') as my_zip:
        my_zip.extractall('files')


# extract specific files
def extract_specific_zip_file():
    with zipfile.ZipFile('files.zip', 'r') as my_zip:
        my_zip.extract('test.png')


# shutil usage for ZIP
# Write ZIP file
def write_zip_shutil():
    shutil.make_archive(base_name='another', format='zip', base_dir='files')


# Write ZIP file
def write_gz_tar_shutil():
    shutil.make_archive(base_name='another', format='gztar', base_dir='files')


# Extract ZIP file
def extract_zip_shutil():
    shutil.unpack_archive(filename='another.zip', extract_dir='another1')


# Download and use ZIP file
def download_zip_file():
    r = requests.get('https://github.com/mroleh/soloLearnPython/archive/refs/heads/master.zip')

    with open('data.zip', 'wb') as file:
        file.write(r.content)

    with zipfile.ZipFile('data.zip', 'r') as data_zip:
        print(data_zip.namelist())
        # data_zip.extractall()
        data_zip.extractall('test_project')


if __name__ == '__main__':
    write_zip()
    # write_compressed_zip()
    # get_zip_info()
    # read_zip_file_names()
    # extract_zip_files()
    # extract_specific_zip_file()
    # write_zip_shutil()
    # write_gz_tar_shutil()
    # extract_zip_shutil()
    # download_zip_file()
