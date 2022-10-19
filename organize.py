import os
import time
from shutil import move

user = os.getenv('USER')
root_dir = '/home/{}/Downloads/'.format(user)
image_dir = os.path.join(root_dir,'images/')
documents_dir =  os.path.join(root_dir,'documents/')
others_dir = os.path.join(root_dir,'others/')
software_dir = os.path.join(root_dir,'softwares/')
ebooks_dir = os.path.join(root_dir,'ebooks/')

doc_book = ('azw3','epub','mobi')
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')
compact_files = ('.zip','.rar')


def get_non_hidden_files_except_current_file(root_dir):
  return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

def log(file, dir):
    date_time = time.strftime("%Y,%m,%d,%H,%M,%S")
    print('file {} moved to {} at {}'.format(file, dir,date_time))


def move_files(files):
  for file in files:

    if file.endswith(doc_types):
      move(file, '{}/{}'.format(documents_dir, file))
      log(file,documents_dir)
    elif file.endswith(img_types):
      move(file, '{}/{}'.format(image_dir, file))
      log(file,image_dir)
    elif file.endswith(software_types):
      move(file, '{}/{}'.format(software_dir, file))
      log(file,software_dir)
    elif file.endswith(doc_book):
        move(file,'{}/{}'.format(ebooks_dir, file))
        log(file,ebooks_dir)
    elif file == "organize.py":
      pass
    else:
      move(file, '{}/{}'.format(others_dir, file))
      print('file {} moved to {}'.format(file, others_dir))

if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)