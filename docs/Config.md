# Config
In this file, I will explain all that is necessary to configure the yt-dlp-helper.

!!! In this version, it is not yet possible to specify a download location for the videos !!!

## The config file
### Its location
The config file is stored at different locations depending on your os

- Windows: `C:/Users/YourUsername/AppData/Roaming/yt-dlp-helper/config.json`
- Linux: `/home/YourUsername/.yt-dlp-helper`

If there is no such file at this location, the program will create a new one that is identical to the
`default_config.json` found in `.meta` directory.
As the extension already implies is the config file written as json.

### Its options
In the current version, there are three keys in the config file: `"language"`, `"useGlobalYt-dlpConfig"` and
`"localYt-dlpConfigName"`.

The first one obviously defines the language that the program uses for its texts.
As of now, it does nothing as multiple languages are not supported yet.

The second key can have `true` or `false` as value. It defines whether the standard configuration file for yt-dlp
should be used.
If you don't know what that is or where it is stored I would recommend you leaving it as `false` and or to read yt-dlps
documentation on GitHub.

The last key defines the path and name of the config file used for yt-dlp.
On default, it is stored in the programs `.meta` directory and is called `default.conf`.
You can change this path to relative or absolute paths of config files that should either have no extension or should
end with `.conf`.
When you have set the option from before to `true`, this will have no effect.