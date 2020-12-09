import argparse
from os import sep
from utils.finder import google
from utils.directory.create import new_directory
from utils.file.download import download_file
from utils.file.parser import meta_parser, file_parser
from utils.banner import show_banner


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', help="Target to search",required=True)
    parser.add_argument('-l','--limit', help="Limit of documents to search", type=int, required=True)
    args = parser.parse_args()
    show_banner()
    directory = "results" + sep + args.target
    new_directory(directory)

    links = google.search(args.target, args.limit)
    print(f"Total links: {len(links)}")
    metadata_files = download_file(links, args.target, directory)
    if metadata_files:
        meta_parser(metadata_files)
        file_parser(directory, "google.txt", metadata_files)


