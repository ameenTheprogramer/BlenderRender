import os
import subprocess
import gdown
import sys

# Constants
OUTPUT_PATH = '/content/result/####'
BLENDER_PARENT_DIR = '/content/'
BLEND_FILE_NAME = 'BOUNCE4.blend'
BLEND_FILE_PATH = os.path.join('/content/', BLEND_FILE_NAME)
BLEND_FILE_ID =  sys.argv[2]
GDRIVE_URL_ID = BLEND_FILE_ID  # Optional if using Google Drive link
BLEND_FILE_LINK = f'https://drive.google.com/uc?id={GDRIVE_URL_ID}'  # Optional if using Google Drive link
BLENDER_TAR_LINK = 'https://download.blender.org/release/Blender4.0/blender-4.0.1-linux-x64.tar.xz'
BLENDER_TAR_PATH = os.path.join(BLENDER_PARENT_DIR, 'blender-4.0.1-linux-x64.tar.xz')
BLENDER_DIRECTORY = '/content/blender-4.0.1-linux-x64/'
BLENDER_EXECUTABLE_PATH = os.path.join(BLENDER_DIRECTORY, 'blender')

# START_FRAMES =  sys.argv[3]
# END_FRAMES =  sys.argv[4]





# Function to parse parameters
def parse_params(param_string):
    params = {}
    for param in param_string:
        key, value = param.split('=')
        params[key] = value
    return params
if len(sys.argv) > 1:
    # Accessing parameters
    params_string = sys.argv[1]  # Get the string "apple=true"
    params = parse_params(params_string.split(','))  # Split by ',' and parse key-value pairs

    # Now you can access parameters like a dictionary
    if 'DRIVE_MOUNT' in params and params['DRIVE_MOUNT'] == 'true':
        from google.colab import drive
        drive.mount('/content/drive')
        print("Google Drive has been mounted.")
    else:
        print("DRIVE_MOUNT = FALSE , google drive not mounting")
else:
    print("DRIVE_MOUNT params not passed ,  google drive not mounting")




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

# def run_blender():
#     subprocess.run([BLENDER_EXECUTABLE_PATH, '-b', BLEND_FILE_PATH, '-noaudio', '-E', 'CYCLES', '-o', OUTPUT_PATH, '-s', START_FRAMES, '-e', END_FRAMES, '-a', '-F', 'PNG', '--', '--cycles-device', 'CUDA'])

if __name__ == "__main__":
    
    download_blend_file()
    download_blender_tar()
    create_blender_directory()
    install_blender()
    run_blender()
