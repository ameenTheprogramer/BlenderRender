import os
import subprocess
import gdown

# Constants
OUTPUT_PATH = '/content/result/####'
BLENDER_PARENT_DIR = '/content/'
BLEND_FILE_NAME = 'BOUNCE4.blend'
BLEND_FILE_PATH = os.path.join('/content/', BLEND_FILE_NAME)
GDRIVE_URL_ID = '1JbPdX41zBwg7c6ByHfhO1Zn-5Y8tnSM3'  # Optional if using Google Drive link
BLEND_FILE_LINK = f'https://drive.google.com/uc?id={GDRIVE_URL_ID}'  # Optional if using Google Drive link
BLENDER_TAR_LINK = 'https://download.blender.org/release/Blender4.0/blender-4.0.1-linux-x64.tar.xz'
BLENDER_TAR_PATH = os.path.join(BLENDER_PARENT_DIR, 'blender-4.0.1-linux-x64.tar.xz')
BLENDER_DIRECTORY = '/content/blender-4.0.1-linux-x64/'
BLENDER_EXECUTABLE_PATH = os.path.join(BLENDER_DIRECTORY, 'blender')


def download_blend_file():
    if not os.path.exists(BLEND_FILE_PATH):
        print("Blend file not found. Downloading...")
        # Download your blend file using appropriate method
        gdown.download(BLEND_FILE_LINK, BLEND_FILE_PATH)
        print("Blend file downloaded successfully.")
    else:
        print("Blend file already exists. Skipping download.")

def download_blender_tar():
    if not os.path.exists(BLENDER_TAR_PATH):
        print("Blender tar file not found. Downloading...")
        gdown.download(BLENDER_TAR_LINK, BLENDER_TAR_PATH)
        print("Blender tar file downloaded successfully.")
    else:
        print("Blender tar file already exists. Skipping download.")

def create_blender_directory():
    if not os.path.exists(BLENDER_DIRECTORY):
        os.makedirs(BLENDER_DIRECTORY)
        print(f"Created folder: {BLENDER_DIRECTORY}")

def install_blender():
    subprocess.run(['tar', 'xf', BLENDER_TAR_PATH, '-C', BLENDER_PARENT_DIR])

def run_blender():
    subprocess.run([BLENDER_EXECUTABLE_PATH, '-b', BLEND_FILE_PATH, '-noaudio', '-E', 'CYCLES', '-o', OUTPUT_PATH, '-s', '0', '-e', '40', '-a', '-F', 'PNG', '--', '--cycles-device', 'CUDA'])

if __name__ == "__main__":
    download_blend_file()
    download_blender_tar()
    create_blender_directory()
    install_blender()
    run_blender()
