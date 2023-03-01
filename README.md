# joinpdf
---

A simple cli that merge multiple PDF files.

## Installation

You can install this package via `pip`:

```shell
pip install joinpdf
```

## Usage

To view the help:

```sh
joinpdf --help
```

Suppose you have the following structure:

```sh
.
├── file0.pdf
├── file10.pdf
├── file1.pdf
├── file2.pdf
├── file3.pdf
├── file4.pdf
├── file5.pdf
├── file6.pdf
├── file7.pdf
├── file8.pdf
└── file9.pdf
```

You can merge two files using:

```sh
joinpdf --input file1.pdf file2.pdf --output catfile.pdf
```

You can merge as many files as you want:

```sh
joinpdf --input file*.pdf --output catfile.pdf
```
