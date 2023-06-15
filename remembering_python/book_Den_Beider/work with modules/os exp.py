import os


# os name
print(os.name)  # posix
os_info = os.uname()
print(os_info)
# posix.uname_result(
    # sysname='Linux', 
    # nodename='giocatory', 
    # release='5.15.0-73-generic', 
    # version='#80-Ubuntu SMP Mon May 15 15:18:26 UTC 2023', 
    # machine='x86_64'
    # )
print(os_info[0])  # Linux

# environment variable dictionary. Changeable (environment variables can be added and removed)
env_list = os.environ
env_list["INSIDE_NEMO_PYTHON"] = "/bin/python3"
print(*env_list, sep="; ")
# SHELL; SESSION_MANAGER; QT_ACCESSIBILITY; COLORTERM; XDG_CONFIG_DIRS; XDG_SESSION_PATH; 
# TERM_PROGRAM_VERSION; GNOME_DESKTOP_SESSION_ID; CONDA_EXE; _CE_M; LANGUAGE; SSH_AUTH_SOCK; 
# CINNAMON_VERSION; DESKTOP_SESSION; GTK_MODULES; XDG_SEAT; PWD; XDG_SESSION_DESKTOP; LOGNAME; 
# QT_QPA_PLATFORMTHEME; XDG_SESSION_TYPE; GPG_AGENT_INFO; XAUTHORITY; VSCODE_GIT_ASKPASS_NODE; 
# XDG_GREETER_DATA_DIR; GJS_DEBUG_TOPICS; GDM_LANG; INSIDE_NEMO_PYTHON; 
# HOME; LANG; LS_COLORS; XDG_CURRENT_DESKTOP; GIT_ASKPASS; XDG_SEAT_PATH; CHROME_DESKTOP; 
# GJS_DEBUG_OUTPUT; VSCODE_GIT_ASKPASS_EXTRA_ARGS; LESSCLOSE; 
# XDG_SESSION_CLASS; TERM; _CE_CONDA; GTK_OVERLAY_SCROLLING; LESSOPEN; 
# USER; VSCODE_GIT_IPC_HANDLE; CONDA_SHLVL; DISPLAY; SHLVL; XDG_VTNR; 
# XDG_SESSION_ID; CONDA_PYTHON_EXE; XDG_RUNTIME_DIR; VSCODE_GIT_ASKPASS_MAIN; 
# GTK3_MODULES; XDG_DATA_DIRS; GDK_BACKEND; PATH; GDMSESSION; ORIGINAL_XDG_CURRENT_DESKTOP; 
# DBUS_SESSION_BUS_ADDRESS; GIO_LAUNCHED_DESKTOP_FILE_PID; GIO_LAUNCHED_DESKTOP_FILE; TERM_PROGRAM;
print()
print(env_list["SHELL"])  # /bin/bash
print(env_list["INSIDE_NEMO_PYTHON"])

# login user
name = os.getlogin()
print(name)  # gio*****

print(os.getpid())  # 87282