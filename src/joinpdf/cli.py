import fitz
from argparse import ArgumentParser, Namespace
from typing import Iterable
from tqdm import tqdm

def validate_filename(path: str):
    if not path.lower().endswith("pdf"):
        raise NotImplementedError("This CLI only supports files with .pdf extension.")

def getargs() -> Namespace:
    parser = ArgumentParser(
            description="A simple cli that merge multiple PDF files."
            )
    parser.add_argument("--input", type=str, nargs="*", help="Path for the pdf files to merge.")
    parser.add_argument("--output", type=str, help="Output file.", default="output.pdf")
    return parser.parse_args()

class PdfMerger:
    def __init__(self, filenames: Iterable[str], save_path: str):
        self.filenames = tqdm(filenames)
        self.output = fitz.open()
        self.save_path = save_path

    def load_pdf(self, filename: str):
        with fitz.open(filename) as pdf:
            for page in pdf:
                self.output.insert_pdf(pdf, from_page=page.number, to_page=page.number)

    def load(self):
        for filename in self.filenames:
            self.load_pdf(filename)
        self.output.save(self.save_path)

def cli():
    args = getargs()
    *map(validate_filename, args.input),
    validate_filename(args.output)
    merger = PdfMerger(filenames=args.input, save_path=args.output)
    merger.load()
