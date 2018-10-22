"""
LIST CREATOR
"""

#Make your input a string
def List(directory):
    initiallist = getfiles(directory)
    #This list has lots of directory attached.
    fstlist = []
    for i in initiallist:
        #removes the file paths
        if i[0:6] == 'starfi':
            fstlist.append(i.lstrip('starfiles/_').rstrip('.txt'))
        elif i[0:6] == '1ASour':
            if i == '1ASource/.DS_Store':
                pass
            else:
                fstlist.append(i.lstrip('1ASource/').rstrip('.png'))
        elif i[0:6] == '1APoll':
            if i == '1APolluted/.DS_Store':
                #.DS_Store is a Mac directory file that is hidden.   also it messes with code.
                pass
            else:
                fstlist.append(i.lstrip('1APolluted/').rstrip('.png'))            
        else:
            pass
    #Using os instead of \r\n or /r/nwindows and Mac are :/
    import os
    with open('%s.txt' % (directory), 'w') as file:
        for i in fstlist:
            file.write('%s' % (i) + os.linesep)
    return 'stored to file %s.' % (directory)

#print List('1ASource')

List('stars')