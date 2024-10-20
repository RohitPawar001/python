import os
import logging

# name of the folder to create
path = "new_logging_folder"
# creates the path if not exist
os.makedirs(path,exist_ok=True)
# creates the file into the created folder and save the path of the file into the file_path variable
file_path = os.path.join(path,"ret.txt")

logging.basicConfig(filename=file_path, # file to store the loggin info
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", #format of log message
                    level=logging.INFO) # level of logging

if __name__ == "__main__":
    logging.info("logging is done")

