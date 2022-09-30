# yt-dlp-helper

 A program that helps you to use yt-dlp

## Setup

The setup for the yt-dlp-helper is easy, all you need to do is download the repository and edit the conifg.json file so that it contains the right path to your yt-dlp installation. For that you have to input the letter of the drive your yt-dlp is installed on as well as the path of the installation. Don't forget that you have to replace every Backslash (\) with two Backslashes (\\).

Like the last paragraph indicates yt-dlp must already be installed on your system or else the program won't work.

The program is so built that you should configure your yt-dlp with a yt.dlp config file as  the program will simply use the .\yt-dlp command to download videos/playlists without using further arguments.

## Config

The program can and must be configured through the config.json file that is in the programs root directory.

The config.json file can however be put into another dictionary. When the program is started the next time after changing the location of the config.json file you have to input the path of it. The config.json files path will than be saved to C:\Users\YourUsername\AppData\Roaming\yt-dlp-helper\alternate-config-path and loaded from there in the future. That means if you want to change the path of the config.json file again you have to either delete the in AppData stored file or edit it.

## Why should I use yt-dlp-helper

yt-dlp-helper brings you two decisive advantages when using yt-dlp:

    1. You can add multiple videos/playlist in a queue, a feature that yt-dlp has not on it's own
    2. You don't have to open the directory yt-dlp is installed in then starting powershell and inputting command + video/playlist url manually but can simply start yt-dlp-helper and input the URL

## Contact

If you have problems, ideas or questions you can contact me in German or English via email (email adress: dersportlichemetzger@gmail.com)
