import os


user = os.getenv('USER')
root_dir = '/home/{}/Downloads/'.format(user)
image_dir = os.path.join(root_dir,'images/')
documents_dir =  os.path.join(root_dir,'documents/')
others_dir = os.path.join(root_dir,'others/')
software_dir = os.path.join(root_dir,'softwares/')
ebooks_dir = os.path.join(root_dir,'ebooks/')


paths = [image_dir, documents_dir, others_dir, software_dir, ebooks_dir, ebooks_dir]

for path in paths:
    isExist = os.path.exists(path)
    if not(isExist):
        os.mkdir(path)
    else:
        pass