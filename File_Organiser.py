#File organiser script allows users to sort, rename by date, delete & archive by date, search for and filter files.

import os
import shutil
import time

#Function for converting bytes to a more readable form
def format_size(bytes_size):
    if bytes_size < 1024:
        return str(int(bytes_size)) + " Bytes"
    elif 1024 <= bytes_size < (1024**2):
        return str(int(bytes_size/1024))+ " KB"
    elif (1024**2) <= bytes_size < (1024**3):
        return str(int(bytes_size/(1024**2))) + " MB"
    elif (1024**3) <= bytes_size < (1024**4):
        return str(int(bytes_size/(1024**3))) + " GB"

print ("Here is what this program can do:")

while True:
    print ("")
    print ("To sort files in to folders by file type, type '1'")
    print ("To rename files to their modification dates, type '2'")
    print ("To delete files by date, type '3'")
    print ("To archive files by date, type '4'")
    print ("To search for files by name, type '5'")
    print ("To filter files by type, date or size, type '6'")
    print ("To exit, type '7'")
    print ("")
    task = input("Which would you like to do? ")
    if task == "1":
        while True:
            try:
                path = input("Enter the path of the files you want to organise by type: ")
                #Retreiving files in directory
                files_list = os.listdir(path)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print (str(e))
        # FILE SORTING (type)
        file_types = ['image files', 'text files', 'video files']
        #Making the directories if they aren't present
        for loop in range(0,3):
            try:
                if not os.path.exists(os.path.join(path, file_types[loop])):
                    os.makedirs(os.path.join(path, file_types[loop]))
            except PermissionError:
                print ("No permission to make directory")
            except Exception as e:
                print ("Failed to created directory: " + file_types[loop] + ":")
                print (str(e))

        for file in files_list:
            if ".jpg".upper() in file.upper() and not os.path.exists(os.path.join(path, "image files", file)):
                try:
                    shutil.move(os.path.join(path, file),os.path.join(path, "image files", file))
                    #Moving the files to the new directory
                    print ("File: " + file + " moved to: 'image files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print ("There was a problem moving file: " + str(file) + ":")
                    print (str(e))
            elif ".png".upper() in file.upper() and not os.path.exists(os.path.join(path, "image files", file)):
                #Same idea as before
                try:
                    shutil.move(os.path.join(path, file), os.path.join(path, "image files", file))
                    print("File: " + file + " moved to: 'image files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print ("There was a problem moving file: " + str(file) + ":")
                    print (str(e))
            elif ".jpeg".upper() in file.upper() and not os.path.exists(os.path.join(path, "image files", file)):
                try:
                    shutil.move(os.path.join(path, file), os.path.join(path, "image files", file))
                    print("File: " + file + " moved to: 'image files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print("There was a problem moving file: " + str(file) + ":")
                    print(str(e))
            elif ".txt".upper() in file.upper() and not os.path.exists(os.path.join(path, "text files", file)):
                try:
                    shutil.move(os.path.join(path, file) ,os.path.join(path, "text files", file))
                    print("File: " + file + " moved to: 'text files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print("There was a problem moving file: " + str(file) + ":")
                    print(str(e))
            elif ".mov".upper() in file.upper() and not os.path.exists(os.path.join(path, "video files", file)):
                try:
                    shutil.move(os.path.join(path, file) ,os.path.join(path, "video files", file))
                    print("File: " + file + " moved to: 'video files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print("There was a problem moving file: " + str(file) + ":")
                    print(str(e))
            elif ".avi".upper() in file.upper() and not os.path.exists(os.path.join(path, "video files", file)):
                try:
                    shutil.move(os.path.join(path, file), os.path.join(path, "video files", file))
                    print("File: " + file + " moved to: 'video files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print("There was a problem moving file: " + str(file) + ":")
                    print(str(e))
            elif ".mp4".upper() in file.upper() and not os.path.exists(os.path.join(path, "video files", file)):
                try:
                    shutil.move(os.path.join(path, file) ,os.path.join(path, "video files", file))
                    print("File: " + file + " moved to: 'video files'")
                except PermissionError:
                    print ("No permission to move file: " + str(file))
                except Exception as e:
                    print ("There was a problem moving file: " + str(file) + ":")
                    print (str(e))
            else:
                print ("file: " + file + " not moved.")

    elif task == "2":
        while True:
            try:
                path = input("Enter the path of the files you want to rename by date: ")
                files_list = os.listdir(path)
                #Retreiving files in directory again (same for each task)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print(str(e))
        # FILE RENAMING (date)
        for file in files_list:
            repeats = 0
            #Getting a full path including the file as you can't get date modified time otherwise
            full_path = os.path.join(path, file)
            #Retreiving time since date modified from file in seconds
            modification_time = os.path.getmtime(full_path)
            #Converting the seconds to a more readable format
            readable_time = time.strftime("%Y-%d-%m_%H-%M", time.localtime(modification_time))
            new_file_name = readable_time + os.path.splitext(file)[1]
            #Ensuring no conflict with files modified at the same time
            while os.path.exists(os.path.join(path, new_file_name)):
                repeats = repeats + 1
                new_file_name = readable_time + "(" + str(repeats) + ")" + os.path.splitext(file)[1]
                print ("File date collision detected. Renaming " + file + " to " + new_file_name)
            try:
                os.rename(full_path, (os.path.join(path, new_file_name)))
                print ("File: " + str(file) + " renamed to: " + str(new_file_name))
            except PermissionError:
                print ("No permission to rename: " + str(file) + " to: " + str(new_file_name))
            except Exception as e:
                print ("Unable to rename file: " + str(file) + ".")
                print (str(e))

    elif task == "3":
        while True:
            try:
                path = input("Enter the path of the files you want to delete by date: ")
                files_list = os.listdir(path)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print(str(e))
        # FILE DELETION (date)
        while True:
            try:
                age_threshold = input("Enter the modification age of files you want to delete in days: ")
                #Not allowing values less than 0
                if float(age_threshold) < 0:
                    print ("Please enter an age more than 0 days.")
                    continue
                else:
                    current_time = time.time()
                    files_deleted = False
                    counter = 0
                    for file in files_list:
                        #Getting a full path including the file as you can't get date modified otherwise
                        full_path = os.path.join(path, file)
                        #Retreiving time since date modified
                        modification_time = os.path.getmtime(full_path)
                        #Age of file converted to days
                        file_age = ((current_time - modification_time)/(24*3600))
                        if file_age > float(age_threshold) and os.path.isfile(full_path):
                            try:
                                #Deleting the file with error handling
                                os.remove(full_path)
                                #Rounding to 1dp to improve readability
                                printable_age = round(file_age, 1)
                                print ("deleting file: " + str(file) + " time since modified: " + str(printable_age) + " days")
                                counter = counter + 1
                                files_deleted = True
                            except PermissionError:
                                print ("No permission to delete file: " + str(file))
                            except Exception as e:
                                print ("Unable to delete file: " + str(file) + ".")
                                print (str(e))
                        elif file_age <= float(age_threshold):
                            print ("file " + str(file) + " not deleted as it was not modified more than " + age_threshold + " days ago.")
                        else:
                            print ("Folder " + str(file) + " not deleted.")
                    if files_deleted == True:
                        print (str(counter) + " files deleted.")

                    if not files_deleted:
                        print ("There were no files modified longer than " + age_threshold + " days ago, so none were deleted.")
                break
            except ValueError:
                print ("Please enter a valid number.")
                continue

    elif task == "4":
        while True:
            try:
                path = input("Enter the path of the files you want to archive by date: ")
                files_list = os.listdir(path)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print(str(e))
        # FILE ARCHIVING (date)
        while True:
            try:
                age_threshold = input("Enter the modification age of files you want to archive in days: ")
                if float(age_threshold) < 0:
                    print ("Please enter an age more than 0 days.")
                    continue
                else:
                    current_time = time.time()
                    files_archived = False
                    counter = 0
                    for file in files_list:
                        full_path = os.path.join(path, file)
                        modification_time = os.path.getmtime(full_path)
                        file_age = ((current_time - modification_time)/(24*3600))
                        if file_age > float(age_threshold):
                            try:
                                #Same idea as deletion, just making a new directory now instead
                                if not os.path.exists(os.path.join(path, "Archive")):
                                    os.makedirs((os.path.join(path, "Archive")))
                                #Rounding age to improve readability again
                                printable_age = round(file_age, 1)
                                print("Archiving file: " + str(file) + " time since modified: " + str(printable_age) + " days")
                                #Moving to newly made directory
                                shutil.move(full_path, os.path.join(path, "Archive"))
                                counter = counter + 1
                                files_archived = True
                            except PermissionError:
                                print ("No permission to make directory or move " + file + "to directory: " + os.path.join(path, "Archive"))
                            except Exception as e:
                                print ("Failure to archive: " + file)
                                print (str(e))
                        elif file_age <= float(age_threshold):
                            print ("file " + str(file) + " not archived as it was not modified longer than " + age_threshold + " days ago.")
                        else:
                            print ("Folder " + str(file) + " not archived.")
                    if files_archived == True:
                        print (str(counter) + " files archived.")
                    if not files_archived:
                        print ("There were no files modified longer than " + age_threshold + " days ago, so none were archived.")
                break
            except ValueError:
                print ("Please enter a valid number.")
                continue

    elif task == "5":
        while True:
            try:
                path = input("Enter the path of the files you want to search through: ")
                files_list = os.listdir(path)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print(str(e))
        # SEARCH (file names)
        search = input("Enter the file name you want to search for: ").upper()
        files_listed = False
        print ("Here are the results:")
        for file in files_list:
            #Accounting for caps
            if search in (str(file)).upper():
                files_listed = True
                full_path = os.path.join(path, file)
                try:
                    #Retreiving modification time and converting to more readable format to display
                    modification_time = os.path.getmtime(full_path)
                    readable_time = time.strftime('%Y-%d-%m_%H-%M', time.localtime(modification_time))
                    #Displaying file modification time as well as file extension
                    print ("File name: " + os.path.splitext(file)[0] + "   Type: " + os.path.splitext(file)[1] + "   Modified: " + str(readable_time))
                except PermissionError:
                    print ("Unable to access data for file: " + str(file))
                except FileNotFoundError:
                    print ("File: " + str(file) + " not found.")
                except Exception as e:
                    print ("An error occurred while retrieving data for file: " + str(file))
                    print (str(e))
        if files_listed == False:
            print ("There were no files that contained "  + search + " in their name.")

    elif task == "6":
        while True:
            try:
                path = input("Enter the path of the files you want to filter through: ")
                files_list = os.listdir(path)
                break
            except FileNotFoundError:
                print("Please enter a valid path.")
                continue
            except PermissionError:
                print("No permission to access this path.")
                continue
            except Exception as e:
                print("Failed to access path: " + str(path) + ":")
                print(str(e))
        # Filter (type, date & size)
        print ("")
        print ("Here are the different filtering options:")
        print ("")
        print ("1) Date modified (old to new) (enter '1')")
        print ("2) Date modified (new to old) (enter '2')")
        print ("3) Size (small to big) (enter '3')")
        print ("4) Size (big to small) (enter '4')")
        print ("5) File type (enter '5')")
        print ("")
        while True:
            filter_option = input("Which way would you like to filer by? ").strip()
            if filter_option == "1":
                print("")
                #Creating a list to group file modification times and names when sorting
                files_with_modification_times = []
                for file in files_list:
                    full_path = os.path.join(path, file)
                    try:
                        modification_time = os.path.getmtime(full_path)
                        #Adding / appending all files and modification times tuples onto the list
                        files_with_modification_times.append((file, modification_time))
                    except PermissionError:
                        print ("Unable to get modification time of file: " + str(file))
                    except FileNotFoundError:
                        print ("Unable to access file: " + str(file))
                    except Exception as e:
                        print ("Failure to access file: " + str(file))
                        print (str(e))
                #Sorting files and modifications by their time since modified
                files_with_modification_times.sort(key=lambda x: x[1])
                for (file, modification_time) in files_with_modification_times:
                    full_path = os.path.join(path, file)
                    readable_time = time.strftime('%Y-%d-%m_%H-%M', time.localtime(modification_time))
                    #Printing name, type and time since modified in a readable format in order
                    print ("file: " + os.path.splitext(file)[0] + "  Type: " + os.path.splitext(file)[1] + "  Modified: " + str(readable_time))
                break
            elif filter_option == "2":
                print("")
                #This is the exact same logic as filter option 1 just with reverse sorting
                files_with_modification_times = []
                for file in files_list:
                    full_path = os.path.join(path, file)
                    try:
                        modification_time = os.path.getmtime(full_path)
                        files_with_modification_times.append((file, modification_time))
                    except PermissionError:
                        print ("Unable to get modification time of file: " + str(file))
                    except FileNotFoundError:
                        print ("Unable to access file: " + str(file))
                    except Exception as e:
                        print ("Failure to access file: " + str(file))
                        print (str(e))
                files_with_modification_times.sort(key=lambda x: x[1], reverse = True)
                for (file, modification_time) in files_with_modification_times:
                    full_path = os.path.join(path, file)
                    readable_time = time.strftime('%Y-%d-%m_%H-%M', time.localtime(modification_time))
                    print ("file: " + os.path.splitext(file)[0] + "  Type: " + os.path.splitext(file)[1] + "  Modified: " + str(readable_time))
                break
            elif filter_option == "3":
                print("")
                #Creating a list again but with sizes
                files_with_sizes = []
                for file in files_list:
                    full_path = os.path.join(path, file)
                    try:
                        #Retreiving file size
                        file_size = os.path.getsize(full_path)
                        #Adding tuples to the list
                        files_with_sizes.append((file, file_size))
                    except PermissionError:
                        print ("Unable to retrieve size of file: " + str(file))
                    except FileNotFoundError:
                        print ("Unable to access file: " + str(file))
                    except Exception as e:
                        print ("Unable to access file: " + str(file))
                        print (str(e))
                files_with_sizes.sort(key=lambda x: x[1])
                for (file, file_size) in files_with_sizes:
                    full_path = os.path.join(path, file)
                    print ("file: " + os.path.splitext(file)[0] + "  Type: " + os.path.splitext(file)[1] + "  Size: " + str(format_size(file_size)))
                break
            elif filter_option == "4":
                print ("")
                #Same as previous logic but with reverse sorting
                files_with_sizes = []
                for file in files_list:
                    full_path = os.path.join(path, file)
                    try:
                        file_size = os.path.getsize(full_path)
                        files_with_sizes.append((file, file_size))
                    except PermissionError:
                        print ("Unable to retrieve size of file: " + str(file))
                    except FileNotFoundError:
                        print ("Unable to access file: " + str(file))
                    except Exception as e:
                        print ("Unable to access file: " + str(file))
                        print (str(e))
                files_with_sizes.sort(key=lambda x: x[1], reverse = True)
                for (file, file_size) in files_with_sizes:
                    full_path = os.path.join(path, file)
                    print ("file: " + os.path.splitext(file)[0] + "  Type: " + os.path.splitext(file)[1] + "  Size: " + str(format_size(file_size)))
                break
            elif filter_option == "5":
                types_found = False
                while True:
                    type = input("What file extension type do you want to filter for? (e.g. '.txt' for text files): ").strip().lower()
                    #Omitting improper file extensions
                    if not type.startswith(".") or len(type) < 2:
                        print ("Please enter a valid file extension. (must start with a '.' and be at least 2 characters long)")
                        continue
                    for file in files_list:
                        #Only printing files with correct extensions
                        if file.lower().endswith(type):
                            print (file)
                            types_found = True
                    #Message for if file of a certain types aren't found
                    if types_found == True:
                        break
                    elif types_found == False:
                        print("There were no files with the extension: " + type + ".")
                        break
                break
            else:
                print ("Please enter a valid filtering option.")
                continue

    elif task == "7":
        #Providing an option to exit the program with a confirmation
        while True:
            confirm = input("Are you sure you would like to exit? (y/n): ")
            if confirm == "y":
                print ("Program ended.")
                exit()
            elif confirm == "n":
                break
            else:
                print ("please enter a valid answer.")

    else:
        #Stopping invalid options
        print ("Please enter a valid option.")