output = []
with open("./requirements.lock") as f:
    line = ""
    for l in f:
        l = l.strip()
        if l.startswith("#"):
            continue  # 주석은 건너뜀
        if not l:
            continue  # 빈줄 스킵
        if l.startswith("--hash") or l.startswith("# via"):
            line += " " + l
        else:
            if line:
                output.append(line)
            line = l
    if line:
        output.append(line)

with open("requirements.lock", "w") as f:
    f.write("\n".join(output) + "\n")