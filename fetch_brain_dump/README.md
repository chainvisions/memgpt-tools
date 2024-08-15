# fetch_brain_dump

This tool is used for fetching the text from a "brain dump" section in an [Obsidian](https://obsidian.md) daily note.

It'll pretty much grab whatever's text is in that section. I use it primarily for creating todos using the text fetched from it.

## Usage

Change these lines in accordance to your Obsidian daily note:

```
    VAULT_FOLDER = "<folder here>"
```

and

```
    brain_dump_pattern = r'## 🧠 Brain Dump\n(.*?)(?=\n##|\Z)'
```