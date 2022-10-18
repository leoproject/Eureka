import os


user = os.getenv('USER')
root_dir = '/home/{}/Downloads/'.format(user)
image_dir = os.path.join(root_dir,'images/')
documents_dir =  os.path.join(root_dir,'documents/')
others_dir = os.path.join(root_dir,'others/')
software_dir = os.path.join(root_dir,'softwares/')
ebooks_dir = os.path.join(root_dir,'ebooks/')
log_dir = os.path.join(root_dir,'Log/')


paths = [image_dir, documents_dir, others_dir, software_dir, ebooks_dir,log_dir]

for path in paths:
    isExist = os.path.exists(path)
    if not(isExist):
        folder = path.split('/')[-2]
        os.mkdir(path)
        if folder == 'Log':
            with open(path+'Log.txt', 'a') as f:
                f.write('Organize logs:')
    else:
        pass