import logging
import os
from pathlib import Path
from zipfile import ZipFile

logging.basicConfig(level=logging.INFO)


class ZipExtractor:
    count = 0

    def __init__(self, path):
        self.directory_iterator(path)

    def extract_zip(self, path):
        with ZipFile(path, 'r') as zObject:
            zObject.extractall(path=path.replace(".zip", ""))
            logging.info(f"Extracted zip at location:: {path}")
            self.count += 1

    def check_and_extract_zip(self, filename):
        # Check if the file is zip file
        if ".zip" in filename:
            filename_wo_ext = filename.replace(".zip", "")
            # Check if the zip is not extracted already then only extract it
            if not Path(filename_wo_ext).is_dir():
                # extract_zip function will handle the extraction further
                self.extract_zip(filename)

    def directory_iterator(self, directory):
        # Iterate through directory
        for filename in os.listdir(directory):
            # get the name of all the files inside directory
            filename = os.path.join(directory, filename)
            self.check_and_extract_zip(filename)
            self.directory_iterator(filename) if os.path.isdir(filename) else None


if __name__ == '__main__':
    logging.info("Staring the Extraction Process")
    obj = ZipExtractor(r"C:\Learning\python DSA Course")
    logging.info(f"Extraction Completed:: Extracted {obj.count} zips")
