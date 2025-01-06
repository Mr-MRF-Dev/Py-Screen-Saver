# 🖥️ Py Screen Saver

[![GitHub Release](https://img.shields.io/github/v/release/Mr-MRF-Dev/Py-Screen-Saver)](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/releases)
![GitHub repo size](https://img.shields.io/github/repo-size/Mr-MRF-Dev/Py-Screen-Saver)
[![Build & Release App 🚀](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/actions/workflows/build.yml/badge.svg)](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/actions/workflows/build.yml)
[![GitHub License](https://img.shields.io/github/license/Mr-MRF-Dev/Py-Screen-Saver)](/LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple screen saver application using Python's Tkinter library. This app displays a clock at the center of the screen when activated.

![Screenshot](/images/screenshot.jpg)

## 📥 Installation

you can download the latest version of the app from the [Releases](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/releases) page.

## 🛠 Getting Started

follow the instruction to install Screen Saver App on Windows OS:

1. Clone Code

    use [Git](https://git-scm.com/) on your system

    ```bash
    git clone https://github.com/Mr-MRF-Dev/Py-Screen-Saver.git
    ```

    or use [GitHub CLI](https://cli.github.com/)

    ```bash
    gh repo clone Mr-MRF-Dev/Py-Screen-Saver
    ```

2. Change your directory.

    ```bash
    cd Py-Screen-Saver
    ```

3. Install [tkinter](https://docs.python.org/3/library/tkinter.html) and [Nuitka](https://pypi.org/project/Nuitka/) ( by using [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) )

    ```bash
    pip install -r requirements.txt
    ```

4. Create `exe` File with Nuitka

   ```bash
   nuitka --mode=app --enable-plugin=tk-inter  src/main.py
   ```

5. Change File Format to `scr`

    ```bash
    ren main.exe Py-Screen-Saver-win.scr
    ```

6. Move the file to `C:/windows/system32` **(Administrator access is required)**

    ```bash
    mv Py-Screen-Saver-win.scr C:/windows/system32
    ```

7. Install the new screen saver (with registry):

    ```bash
     reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d C:\Windows\system32\Py-Screen-Saver-win.scr /f
    ```

    > reg add flags: `/v` \<Valuename\>, `/t` \<Type\>, `/d` \<Data\>, `/f` Adds the registry entry without prompting for confirmation.
    > [More about reg command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg)

    You can also right-click on the `.scr` file and select the "Install" option.

Done :)

## 💡 Tips

- To see all screen savers:

    ```bash
    dir c:\windows\system32\*scr
    ```

- You can adjust the duration of the screen timeout (600 sec):

    ```bash
    reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 600 /f
    ```

- Also, you don't need to rename the file to 'scr' extension. Instead, you can directly install the file with the 'exe' extension.

    ```bash
    reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d C:\Windows\system32\main.exe /f
    ```

## 🤝 Contributing

we welcome any contributions you may have. If you're interested in helping out, fork the repository and create an [Issue](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/issues) and [PR](https://github.com/Mr-MRF-Dev/Py-Screen-Saver/pulls).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.
