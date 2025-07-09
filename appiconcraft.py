#!/usr/bin/env python3
"""
AppIconCraft - A tool for generating iOS and Android App Icon Assets

This tool generates all required icon sizes for iOS and Android platforms
from a single 1024x1024 source image using macOS native sips command.

Author: AppIconCraft
Version: 1.0
"""

import os
import sys
import json
import argparse

class AppIconCraft:
    def __init__(self):
        self.ios_icon_sizes = [
            # iPhone App Icons
            {"size": 60, "scale": 2, "filename": "Icon-60@2x.png", "idiom": "iphone"},
            {"size": 60, "scale": 3, "filename": "Icon-60@3x.png", "idiom": "iphone"},
            
            # iPad App Icons
            {"size": 76, "scale": 1, "filename": "Icon-76.png", "idiom": "ipad"},
            {"size": 76, "scale": 2, "filename": "Icon-76@2x.png", "idiom": "ipad"},
            {"size": 83.5, "scale": 2, "filename": "Icon-83.5@2x.png", "idiom": "ipad"},
            
            # iOS Marketing Icon
            {"size": 1024, "scale": 1, "filename": "Icon-1024.png", "idiom": "ios-marketing"},
            
            # Settings Icons
            {"size": 29, "scale": 1, "filename": "Icon-29.png", "idiom": "ipad"},
            {"size": 29, "scale": 2, "filename": "Icon-29@2x.png", "idiom": "iphone"},
            {"size": 29, "scale": 2, "filename": "Icon-29@2x.png", "idiom": "ipad"},
            {"size": 29, "scale": 3, "filename": "Icon-29@3x.png", "idiom": "iphone"},
            
            # Spotlight Icons
            {"size": 40, "scale": 1, "filename": "Icon-40.png", "idiom": "ipad"},
            {"size": 40, "scale": 2, "filename": "Icon-40@2x.png", "idiom": "iphone"},
            {"size": 40, "scale": 2, "filename": "Icon-40@2x.png", "idiom": "ipad"},
            {"size": 40, "scale": 3, "filename": "Icon-40@3x.png", "idiom": "iphone"},
            
            # Notification Icons
            {"size": 20, "scale": 1, "filename": "Icon-20.png", "idiom": "ipad"},
            {"size": 20, "scale": 2, "filename": "Icon-20@2x.png", "idiom": "iphone"},
            {"size": 20, "scale": 2, "filename": "Icon-20@2x.png", "idiom": "ipad"},
            {"size": 20, "scale": 3, "filename": "Icon-20@3x.png", "idiom": "iphone"},
            
            # Apple Watch App Icons
            {"size": 24, "scale": 2, "filename": "Icon-24@2x.png", "idiom": "watch"},
            {"size": 27.5, "scale": 2, "filename": "Icon-27.5@2x.png", "idiom": "watch"},
            {"size": 29, "scale": 2, "filename": "Icon-29@2x.png", "idiom": "watch"},
            {"size": 29, "scale": 3, "filename": "Icon-29@3x.png", "idiom": "watch"},
            {"size": 40, "scale": 2, "filename": "Icon-40@2x.png", "idiom": "watch"},
            {"size": 44, "scale": 2, "filename": "Icon-44@2x.png", "idiom": "watch"},
            {"size": 50, "scale": 2, "filename": "Icon-50@2x.png", "idiom": "watch"},
            {"size": 86, "scale": 2, "filename": "Icon-86@2x.png", "idiom": "watch"},
            {"size": 98, "scale": 2, "filename": "Icon-98@2x.png", "idiom": "watch"},
            {"size": 108, "scale": 2, "filename": "Icon-108@2x.png", "idiom": "watch"},
            
            # Mac App Icons
            {"size": 16, "scale": 1, "filename": "Icon-16.png", "idiom": "mac"},
            {"size": 16, "scale": 2, "filename": "Icon-16@2x.png", "idiom": "mac"},
            {"size": 32, "scale": 1, "filename": "Icon-32.png", "idiom": "mac"},
            {"size": 32, "scale": 2, "filename": "Icon-32@2x.png", "idiom": "mac"},
            {"size": 128, "scale": 1, "filename": "Icon-128.png", "idiom": "mac"},
            {"size": 128, "scale": 2, "filename": "Icon-128@2x.png", "idiom": "mac"},
            {"size": 256, "scale": 1, "filename": "Icon-256.png", "idiom": "mac"},
            {"size": 256, "scale": 2, "filename": "Icon-256@2x.png", "idiom": "mac"},
            {"size": 512, "scale": 1, "filename": "Icon-512.png", "idiom": "mac"},
            {"size": 512, "scale": 2, "filename": "Icon-512@2x.png", "idiom": "mac"},
        ]
        
        self.android_icon_sizes = [
            # Android App Icons (mipmap densities)
            {"density": "mdpi", "size": 48, "filename": "ic_launcher.png", "folder": "mipmap-mdpi"},
            {"density": "hdpi", "size": 72, "filename": "ic_launcher.png", "folder": "mipmap-hdpi"},
            {"density": "xhdpi", "size": 96, "filename": "ic_launcher.png", "folder": "mipmap-xhdpi"},
            {"density": "xxhdpi", "size": 144, "filename": "ic_launcher.png", "folder": "mipmap-xxhdpi"},
            {"density": "xxxhdpi", "size": 192, "filename": "ic_launcher.png", "folder": "mipmap-xxxhdpi"},
            
            # Android Adaptive Icons (API 26+)
            {"density": "mdpi", "size": 108, "filename": "ic_launcher_foreground.png", "folder": "mipmap-mdpi"},
            {"density": "hdpi", "size": 162, "filename": "ic_launcher_foreground.png", "folder": "mipmap-hdpi"},
            {"density": "xhdpi", "size": 216, "filename": "ic_launcher_foreground.png", "folder": "mipmap-xhdpi"},
            {"density": "xxhdpi", "size": 324, "filename": "ic_launcher_foreground.png", "folder": "mipmap-xxhdpi"},
            {"density": "xxxhdpi", "size": 432, "filename": "ic_launcher_foreground.png", "folder": "mipmap-xxxhdpi"},
            
            # Android Round Icons
            {"density": "mdpi", "size": 48, "filename": "ic_launcher_round.png", "folder": "mipmap-mdpi"},
            {"density": "hdpi", "size": 72, "filename": "ic_launcher_round.png", "folder": "mipmap-hdpi"},
            {"density": "xhdpi", "size": 96, "filename": "ic_launcher_round.png", "folder": "mipmap-xhdpi"},
            {"density": "xxhdpi", "size": 144, "filename": "ic_launcher_round.png", "folder": "mipmap-xxhdpi"},
            {"density": "xxxhdpi", "size": 192, "filename": "ic_launcher_round.png", "folder": "mipmap-xxxhdpi"},
            
            # Notification Icons
            {"density": "mdpi", "size": 24, "filename": "ic_notification.png", "folder": "drawable-mdpi"},
            {"density": "hdpi", "size": 36, "filename": "ic_notification.png", "folder": "drawable-hdpi"},
            {"density": "xhdpi", "size": 48, "filename": "ic_notification.png", "folder": "drawable-xhdpi"},
            {"density": "xxhdpi", "size": 72, "filename": "ic_notification.png", "folder": "drawable-xxhdpi"},
            {"density": "xxxhdpi", "size": 96, "filename": "ic_notification.png", "folder": "drawable-xxxhdpi"},
            
            # Google Play Store Icon
            {"density": "web", "size": 512, "filename": "ic_launcher_web.png", "folder": "web"},
        ]
    
    def resize_image_with_sips(self, input_path, output_path, target_size):
        """使用macOS原生的sips命令进行图像缩放"""
        cmd = f'sips -z {target_size} {target_size} "{input_path}" --out "{output_path}"'
        return os.system(cmd) == 0
    
    def generate_ios_contents_json(self, output_dir):
        """生成iOS Contents.json文件"""
        contents = {
            "images": [],
            "info": {
                "author": "xcode",
                "version": 1
            }
        }
        
        for icon_info in self.ios_icon_sizes:
            contents["images"].append({
                "filename": icon_info["filename"],
                "idiom": icon_info["idiom"],
                "scale": f"{icon_info['scale']}x",
                "size": f"{icon_info['size']}x{icon_info['size']}"
            })
        
        with open(os.path.join(output_dir, "Contents.json"), "w") as f:
            json.dump(contents, f, indent=2)
    
    def generate_ios_icons(self, input_image_path, output_dir="AppIcon.appiconset"):
        """生成iOS App Icon"""
        # 创建输出目录
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 检查输入文件是否存在
        if not os.path.exists(input_image_path):
            print(f"错误: 输入文件 '{input_image_path}' 不存在")
            return False
        
        print(f"正在生成iOS App Icon...")
        print(f"AppIconCraft - 使用macOS原生sips命令生成高质量图标")
        
        # 生成所有尺寸的图标
        for icon_info in self.ios_icon_sizes:
            pixel_size = int(icon_info["size"] * icon_info["scale"])
            
            # 输出路径
            output_path = os.path.join(output_dir, icon_info["filename"])
            
            # 使用sips缩放图像
            if self.resize_image_with_sips(input_image_path, output_path, pixel_size):
                print(f"生成: {icon_info['filename']} ({pixel_size}x{pixel_size})")
            else:
                print(f"错误: 无法生成 {icon_info['filename']}")
                return False
        
        # 生成Contents.json文件
        self.generate_ios_contents_json(output_dir)
        print(f"生成: Contents.json")
        
        print(f"\n✅ iOS图标已生成到 {output_dir} 目录")
        return True
    
    def generate_android_icons(self, input_image_path, output_dir="android-icons"):
        """生成Android App Icon"""
        # 创建输出目录
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 检查输入文件是否存在
        if not os.path.exists(input_image_path):
            print(f"错误: 输入文件 '{input_image_path}' 不存在")
            return False
        
        print(f"正在生成Android App Icon...")
        print(f"AppIconCraft - 使用macOS原生sips命令生成高质量图标")
        
        # 生成所有尺寸的图标
        for icon_info in self.android_icon_sizes:
            # 创建文件夹
            folder_path = os.path.join(output_dir, icon_info["folder"])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # 输出路径
            output_path = os.path.join(folder_path, icon_info["filename"])
            
            # 使用sips缩放图像
            if self.resize_image_with_sips(input_image_path, output_path, icon_info["size"]):
                print(f"生成: {icon_info['folder']}/{icon_info['filename']} ({icon_info['size']}x{icon_info['size']})")
            else:
                print(f"错误: 无法生成 {icon_info['folder']}/{icon_info['filename']}")
                return False
        
        # 生成adaptive icon XML文件
        self.generate_adaptive_icon_xml(output_dir)
        
        print(f"\n✅ Android图标已生成到 {output_dir} 目录")
        return True
    
    def generate_adaptive_icon_xml(self, output_dir):
        """生成Android Adaptive Icon XML文件"""
        # 创建mipmap-anydpi-v26目录
        anydpi_dir = os.path.join(output_dir, "mipmap-anydpi-v26")
        if not os.path.exists(anydpi_dir):
            os.makedirs(anydpi_dir)
        
        # 创建values目录
        values_dir = os.path.join(output_dir, "values")
        if not os.path.exists(values_dir):
            os.makedirs(values_dir)
        
        # ic_launcher.xml
        launcher_xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>'''
        
        # ic_launcher_round.xml
        launcher_round_xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>'''
        
        # colors.xml
        colors_xml = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">#FFFFFF</color>
</resources>'''
        
        # 保存XML文件
        with open(os.path.join(anydpi_dir, "ic_launcher.xml"), "w") as f:
            f.write(launcher_xml)
        
        with open(os.path.join(anydpi_dir, "ic_launcher_round.xml"), "w") as f:
            f.write(launcher_round_xml)
        
        with open(os.path.join(values_dir, "colors.xml"), "w") as f:
            f.write(colors_xml)
        
        print("生成: Adaptive Icon XML文件")
    
    def generate_icons(self, input_image_path, platform="ios", output_dir=None):
        """生成指定平台的App Icon"""
        if platform == "ios":
            default_dir = "AppIcon.appiconset"
            output_dir = output_dir or default_dir
            return self.generate_ios_icons(input_image_path, output_dir)
        elif platform == "android":
            default_dir = "android-icons"
            output_dir = output_dir or default_dir
            return self.generate_android_icons(input_image_path, output_dir)
        elif platform == "both":
            ios_success = self.generate_ios_icons(input_image_path, "AppIcon.appiconset")
            android_success = self.generate_android_icons(input_image_path, "android-icons")
            return ios_success and android_success
        else:
            print(f"不支持的平台: {platform}")
            return False

def main():
    parser = argparse.ArgumentParser(
        description="AppIconCraft - 使用macOS原生sips命令生成iOS/Android App Icon",
        epilog="生成适配iOS和Android的所有尺寸App Icon"
    )
    parser.add_argument("input", help="输入的1024x1024图标文件路径")
    parser.add_argument("-p", "--platform", choices=["ios", "android", "both"], 
                       default="both", help="目标平台 (默认: both)")
    parser.add_argument("-o", "--output", 
                       help="输出目录名称 (默认: iOS用AppIcon.appiconset, Android用android-icons)")
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input):
        print(f"错误: 输入文件 '{args.input}' 不存在")
        sys.exit(1)
    
    # 检查是否在macOS上
    if sys.platform != "darwin":
        print("错误: AppIconCraft 仅支持macOS系统")
        sys.exit(1)
    
    print("=" * 50)
    print("AppIconCraft v1.0 - App Icon 生成工具")
    print("=" * 50)
    
    # 生成图标
    craft = AppIconCraft()
    success = craft.generate_icons(args.input, args.platform, args.output)
    
    if success:
        print("\n🎉 AppIconCraft 生成完成！")
    else:
        print("\n❌ AppIconCraft 生成失败！")
        sys.exit(1)

if __name__ == "__main__":
    main()
