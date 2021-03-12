import os, shutil
from tinytag import TinyTag, TinyTagException


def extractor():
    # print("Start")
    path = "/Users/martintownley/Desktop/id3Test"
    os.chdir(path)
    tracks = []
    # print(os.listdir(path))
    for files in os.scandir(path):

        if not files.path.endswith((".mp3", ".m4a", ".flac", ".alac", ".wav")):
            print("Incorrect file type")
        else:
            name = files.name
            tracks.append(name)  # stick name in tracks array
            temp_track = TinyTag.get(path + "/" + name)
            temp_artist = temp_track.artist
            temp_album = temp_track.album

            # unknown artist folder creation
            if (temp_track.artist == "") or (temp_track.artist == None):
                print("Track %s has no artist metadata" % name)
                # create unknown artist folder, and check if one already exists
                temp_artist = "Unknown Artist"
                try:
                    # runs first
                    os.makedirs(temp_artist)
                except FileExistsError:
                    # runs if exception happens in try block
                    """
                    joining gives full path,
                    meaning shutil will overwrite
                    existing files w. same name
                    """
                    # fullSrcPath = os.path.join(path, name)
                    # fullDstPath = os.path.join(temp_artist, name)
                    try:
                        shutil.move(name, temp_artist)
                        print("existyError")
                    except shutil.Error:  # dest path exists
                        print("SHUTILERROR")
                        # here we rename it
                        base, ext = os.path.splitext(name)
                        newName = base + "(1)" + ext
                        os.rename(name, newName)
                        shutil.move(newName, temp_artist)
                        # shutil.move(name, temp_artist)

                else:
                    # executes if try block succeeds
                    # move file into folder
                    """
                    joining gives full path,
                    meaning shutil will overwrite
                    existing files w. same name
                    """
                    # fullSrcPath = os.path.join(path, name)
                    # fullDstPath = os.path.join(temp_artist, name)
                    # shutil.move(name, temp_artist)
                    print("existyError")

                finally:
                    # path = path + "/" + temp_artist
                    # os.chdir(path)
                    print("always runs")

            # else, make artist folder from artist name
            else:
                try:
                    os.makedirs(temp_artist)
                except FileExistsError:
                    # runs if exception happens in try block
                    """
                    joining gives full path,
                    meaning shutil will overwrite
                    existing files w. same name
                    """
                    print("existyError")
                    # fullSrcPath = os.path.join(path, name)
                    # fullDstPath = os.path.join(temp_artist, name)
                    # shutil.move(name, temp_artist)
                else:
                    # executes if try block succeeds
                    # move file into folder
                    """
                    joining gives full path,
                    meaning shutil will overwrite
                    existing files w. same name
                    """
                    print("existyError")
                    # fullSrcPath = os.path.join(path, name)
                    # fullDstPath = os.path.join(temp_artist, name)
                    # shutil.move(name, temp_artist)

    # print(tracks)
    # print(temp_artist)
    # os.chdir(path)
    # check
    # if (temp_track.artist == "") or (temp_track.artist == None):
    # print("Song %s has no artist info" % name)
    # print("  ")
    # create unknown artist folder, and put it in there.
    # but catch error saying that "Unknown Artist" already exists
    # if it does, don't create the folder, just move the file straigh
    # into the existing one.
    # try:
    # temp_artist = "Unknown Artist"
    # os.makedirs(temp_artist)
    # shutil.move(files, temp_artist)
    # except FileExistsError:
    # print("Directory %s exists already" % temp_artist)
    # print(" ")
    # shutil.move(name, temp_artist)

    # else:

    # print(temp_artist)

    # try:
    # os.makedirs(temp_artist)
    # except FileNotFoundError:
    # print("No artist info for %s." % )
    # except FileExistsError:
    # print("Directory exists already")


extractor()
##########
def createAndMove():
    path = "/Users/martintownley/Desktop/direcTest/"
    os.chdir(path)
    # NewFolder = "TestFolder"

    # os.makedirs(NewFolder)
    src = path
    dest = path + "/" + "TestFolder"
    os.chdir(src)  # change to src directory

    for (root, dirs, files) in os.walk(src):
        print(files)
        for xfile in files:
            shutil.move(xfile, dest)


# createAndMove()
