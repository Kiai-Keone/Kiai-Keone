InputFile = open("InputText", "r")
lines = InputFile.readlines()
InputFile.close()

OutputFile = open("OutputText", "w")
for line in reversed(lines):
    OutputFile.write(line)
OutputFile.close()
