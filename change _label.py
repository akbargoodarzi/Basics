import os

path_actual='file'

path_modifed='file_new'

if  not os.path.isdir(path_modifed):

    os.mkdir(path_modifed)
    
list_dir=os.listdir(path_actual)

for i in list_dir:

    with open(f'{path_actual}/{i}') as file:

        data=file.read()

        linesOfFile = data.splitlines()

        for lineNo in range(len(linesOfFile)):

            content=linesOfFile[lineNo].split(' ')

            label = content[0]

            if label  not in ['3','4'] :

                document=' '.join(content)+'\n'

                with open(f'{path_modifed}/{i}','+a') as filewrite:

                    filewrite.write(document)

            if label in ['3','4'] :

                document=' '.join(content)+'\n'

                document='2'+document[1:]

                with open(f'{path_modifed}/{i}','+a') as filewrite:

                    filewrite.write(document)
