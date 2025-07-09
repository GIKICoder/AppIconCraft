# AppIconCraft

A Python tool for generating iOS and Android App Icon Assets from a 1024x1024 icon image.

- [中文文档](README_CN.md)

## Features

- **Zero Dependencies**: Uses macOS native `sips` command, no need to install Pillow or other dependencies
- Supports both iOS and Android platform icon generation
- Complete iOS icon size support (iPhone, iPad, Apple Watch, Mac)
- Complete Android icon size support (regular, round, adaptive, notification icons)
- High-quality image scaling
- Automatic configuration file generation (iOS Contents.json, Android XML files)

## System Requirements

- macOS (uses native sips command)
- Python 3.6+

## Usage

### Generate iOS and Android icons (default)
```bash
python appiconcraft.py input_icon.png
```

### Generate iOS icons only
```bash
python appiconcraft.py input_icon.png -p ios
```

### Generate Android icons only
```bash
python appiconcraft.py input_icon.png -p android
```

### Specify output directory
```bash
python appiconcraft.py input_icon.png -p ios -o MyApp.appiconset
```

## iOS Generated Icon Sizes

- **iPhone App Icons**: 60pt @2x, @3x
- **iPad App Icons**: 76pt @1x, @2x; 83.5pt @2x
- **Settings Icons**: 29pt @1x, @2x, @3x
- **Spotlight Icons**: 40pt @1x, @2x, @3x
- **Notification Icons**: 20pt @1x, @2x, @3x
- **Apple Watch Icons**: 24pt-108pt various sizes
- **Mac App Icons**: 16pt-512pt various sizes
- **iOS Marketing Icon**: 1024pt @1x

## Android Generated Icon Sizes

- **App Icons**: mdpi(48px) - xxxhdpi(192px)
- **Round Icons**: mdpi(48px) - xxxhdpi(192px)
- **Adaptive Icons**: mdpi(108px) - xxxhdpi(432px)
- **Notification Icons**: mdpi(24px) - xxxhdpi(96px)
- **Google Play Store Icon**: 512px

## Output Structure

### iOS Output
The tool creates an `.appiconset` folder containing:
- All size PNG icon files
- Contents.json configuration file

### Android Output
The tool creates an `android-icons` folder containing:
- Density-categorized folders (mipmap-mdpi, mipmap-hdpi, etc.)
- Various types of icon files (ic_launcher.png, ic_launcher_round.png, etc.)
- Adaptive Icon XML configuration files
- Color resource files

Generated files can be directly used in their respective development environments.

## Notes

- Input icon should preferably be a 1024x1024 pixel PNG file
- The tool automatically maintains the icon's aspect ratio
- Uses macOS native sips command to ensure high-quality scaling




