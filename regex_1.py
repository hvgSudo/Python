import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appearance"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appearance"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appearance"))
print(re.findall(r"\w{5, 10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.findall(r"\w{,20}", "I really like strawberries"))
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
result = re.search(regex, "A completely different string that also has [34567]")
print(result[1])
result = re.search(regex, "99 elephants in the [jungle]")
print(result)
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in the [Jungle]"))
print(re.split(r"[.?!]", "One sentence. Aother one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Aother one? And the last one!"))
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email or go_nuts95@my.example.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace Ada"))
