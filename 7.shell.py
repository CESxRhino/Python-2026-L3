import os
import shlex as sh
import subprocess
import sys
def exec_pipeline(commands):
    processes = []
    prev_stdout = None
    for i,cmd_line in enumerate(commands):
        args = sh.split(cmd_line.strip())
        if not args:
            continue
        first = (i == 0)
        last = (i == len(commands) - 1)  
        stdin = None if first else prev_stdout
        stdout = None if last else prev_stdout
        try:
            proc = subprocess.Popen(
                args,
                stdin=stdin,
                stdout=stdout,
                stderr=None,
            )
            processes.append(proc)
            if prev_stdout:
                prev_stdout.close()
            prev_stdout = proc.stdout
        except FileNotFoundError:
            print("NOT FOUND" + args[0])
        except Exception as e:
            print(f"shell : error : {e}")
            return
    for proc in processes:
        proc.wait()
def exec_comm(cmd_str):
    stdin_file = None
    stdout_file = None
    stdin_fd = None
    stdout_fd = None
    tokens = sh.split(cmd_str.strip())
    clean_tokens = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok == "<":
            if i + 1 < len(tokens):
                stdin_file = tokens[i + 1]
                i += 2
            else:
                print("shell: syntax error near unexpected token 'newline'")
                return
        elif tok == ">":
            if i + 1 < len(tokens):
                stdout_file = tokens[i + 1]
                i += 2
            else:
                print("shell: syntax error near unexpected token 'newline'")
                return
        else:
            clean_tokens.append(tok)
            i = i + 1         
    if not clean_tokens:
        return

    if clean_tokens[0] == "cd":
        tar_dir = clean_tokens[1] if len(clean_tokens) > 1 else os.path.expanduser("~")
        try:
            os.chdir(tar_dir)
        except Exception as e:
            print(f"cd:{e}")
        return
    try:
        if stdin_file:
            stdin_fd = open(stdin_file,'r')   
        if stdout_file:
            stdout_fd = open(stdout_file,'w')

        proc = subprocess.Popen(
            clean_tokens,
            stdin=stdin_fd,
            stdout=stdout_fd,
            stderr=None,
        )
        proc.wait()
    except FileNotFoundError:
        print(f"shell: command not found: {clean_tokens[0]}")
    except Exception as e:
        print(f"shell: error: {e}")
    finally:
        if stdin_fd:
            stdin_fd.close()
        if stdout_fd:
            stdout_fd.close()
while True:
    try:
        current_dir = os.path.basename(os.getcwd()) or "/"
        cmd_line = input(f"py-shell [{current_dir}]$ ").strip()
        if not cmd_line:
            continue

        if cmd_line in ("exit", "quit"):
            print("Exiting shell...")
            break
        if "|" in cmd_line:
            commands = cmd_line.split("|")
            exec_pipeline(commands)
        else:
            exec_comm(cmd_line)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting shell...")
        break