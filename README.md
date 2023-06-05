
# Code to Word converter

## Usage

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the converter

List out the folders and/or files you want to convert
and include in the final docx document:

```bash
python -m wordcodegen convert-source-files \
  -f /some/folder/with/source-files \
  -f /one/more/folder \
  -i /my/folder/concrete_file.py \
  -i /my/folder/one_more.c
```

The result will be in the `converted.docx`
