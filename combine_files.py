import os

if os.path.isfile("./output.txt"):
  os.remove("./output.txt")


for root, dirs, files in os.walk(".", topdown=True):
  if ".pythonlibs" in dirs:
    dirs.remove(".pythonlibs")
  if ".cache" in dirs:
    dirs.remove(".cache")
  for name in files:
    if name.endswith((".py", ".json")) and name != "combine_files.py":
      try:
        with open(os.path.join(root,name), "r", encoding='utf-8') as input_file:
          content = input_file.read()
        with open("output.txt", "a", encoding='utf-8') as output_file:
          output_file.write("\n\n ----------------------------------------------------------------------------------------------------- \n\n")
          output_file.write(f"Filename: {os.path.relpath(os.path.join(root,name), ".")}\n\n")
          output_file.write(content)
      except FileNotFoundError:
        print("File not found!")
      except Exception as e:
        print(f"An error was thrown.  The error is {e}")