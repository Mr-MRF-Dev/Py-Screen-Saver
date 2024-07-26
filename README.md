# 🖥️ Py Screen Saver

[![GitHub License](https://img.shields.io/github/license/Mr-MRF-Dev/Py-Screen-Saver)](/LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple screen saver application using Python's Tkinter library. This app displays a clock at the center of the screen when activated.

![Screenshot](/images/screenshot.jpg)

## 📥 Installation

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
    
3. Install [tkinter](https://docs.python.org/3/library/tkinter.html) and [pyinstaller](https://pypi.org/project/pyinstaller/) ( by using [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) )

    ```bash
    pip install -r requirements.txt
    ```

4. Create `exe` File

   ```bash
   cd src
   ```

   ```bash
   pyinstaller --noconfirm --onefile --windowed  .\main.py
   ```

6. Change File Format to `scr`

    ```bash
    cd dist
    ```

    ```bash
    ren main.exe main.scr
    ```

7. Move the file to `C:/windows/system32` **(Administrator access is required)**

    ```bash
    mv main.scr C:/windows/system32
    ```

8. Install the new screen saver (with registry):

    ```bash
     reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d C:\Windows\system32\main.scr /f
    ```

    > reg add flags: `/v` \<Valuename\>, `/t` \<Type\>, `/d` \<Data\>, `/f` Adds the registry entry without prompting for confirmation.
    > [More about reg command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg)

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
