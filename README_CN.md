# AppIconCraft

一个用于从1024x1024的图标生成iOS和Android App Icon Asset的Python工具。

## 功能特点

- **零依赖**: 使用macOS原生的`sips`命令，无需安装Pillow等依赖
- 支持iOS和Android双平台图标生成
- 完整的iOS图标尺寸支持（iPhone、iPad、Apple Watch、Mac）
- 完整的Android图标尺寸支持（常规、圆形、自适应、通知图标）
- 高质量图像缩放
- 自动生成配置文件（iOS的Contents.json、Android的XML文件）

## 系统要求

- macOS系统（使用原生sips命令）
- Python 3.6+

## 使用方法

### 生成iOS和Android图标（默认）
```bash
python appiconcraft.py input_icon.png
```

### 只生成iOS图标
```bash
python appiconcraft.py input_icon.png -p ios
```

### 只生成Android图标
```bash
python appiconcraft.py input_icon.png -p android
```

### 指定输出目录
```bash
python appiconcraft.py input_icon.png -p ios -o MyApp.appiconset
```

## iOS生成的图标尺寸

- **iPhone App Icons**: 60pt @2x, @3x
- **iPad App Icons**: 76pt @1x, @2x; 83.5pt @2x
- **Settings Icons**: 29pt @1x, @2x, @3x
- **Spotlight Icons**: 40pt @1x, @2x, @3x
- **Notification Icons**: 20pt @1x, @2x, @3x
- **Apple Watch Icons**: 24pt-108pt 各种尺寸
- **Mac App Icons**: 16pt-512pt 各种尺寸
- **iOS Marketing Icon**: 1024pt @1x

## Android生成的图标尺寸

- **App Icons**: mdpi(48px) - xxxhdpi(192px)
- **Round Icons**: mdpi(48px) - xxxhdpi(192px)
- **Adaptive Icons**: mdpi(108px) - xxxhdpi(432px)
- **Notification Icons**: mdpi(24px) - xxxhdpi(96px)
- **Google Play Store Icon**: 512px

## 输出结构

### iOS输出
工具会创建一个`.appiconset`文件夹，包含：
- 所有尺寸的PNG图标文件
- Contents.json配置文件

### Android输出
工具会创建一个`android-icons`文件夹，包含：
- 按密度分类的文件夹（mipmap-mdpi, mipmap-hdpi等）
- 各种类型的图标文件（ic_launcher.png, ic_launcher_round.png等）
- Adaptive Icon XML配置文件
- 颜色资源文件

生成的文件可以直接用于各自的开发环境中。

## 注意事项

- 输入图标建议是1024x1024像素的PNG文件
- 工具会自动保持图标的宽高比
- 使用macOS原生的sips命令确保高质量缩放