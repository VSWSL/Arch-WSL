<div align="center">
  <a href="https://github.com/VSWSL/Arch-WSL">
    <img src="https://github.com/VSWSL/Arch-WSL/blob/main/ArchWSL-Appx/Assets/StoreLogo.scale-150.png?raw=true" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Arch WSL</h3>

  <p align="center">
    This is an unofficial Arch WSL based on the rootfs of arch docker images with a few packages installed to make your life easy
    <br />
    <a href="https://github.com/VSWSL/Arch-WSL#readme"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://apps.microsoft.com/store/detail/arch-wsl/9NPCP8DRCHSN">Download</a>
    ·
    <a href="https://github.com/VSWSL/Arch-WSL/issues">Report Bug</a>
    ·
    <a href="https://github.com/VSWSL/Arch-WSL/issues">Request Feature</a>
  </p>
</div>

<p align="center">
  <a herf="https://github.com/VSWSL/Arch-WSL/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/VSWSL/Arch-WSL" />
  </a>
  <a herf="https://github.com/VSWSL/Arch-WSL/network/members">
    <img src="https://img.shields.io/github/forks/VSWSL/Arch-WSL" />
  </a>
  <a herf="https://github.com/VSWSL/Arch-WSL/stargazers">
    <img src="https://img.shields.io/github/stars/VSWSL/Arch-WSL" />
  </a>
  <a herf="https://github.com/VSWSL/Arch-WSL/issues">
    <img src="https://img.shields.io/github/issues/VSWSL/Arch-WSL" />
  </a>
  <a herf="https://github.com/VSWSL/Arch-WSL/blob/master/LICENSE.md">
    <img src="https://img.shields.io/github/license/VSWSL/Arch-WSL" />
  </a>
</p>

![Screenshot 2023-01-21 121103](https://user-images.githubusercontent.com/52851879/213847753-896877d4-ac2a-4da4-9efc-3c30438f3f8b.png)

## Installation

- Make sure WSL is enabled in you system - https://learn.microsoft.com/en-us/windows/wsl/install

- You can install Arch WSL from [Microsoft Store](https://apps.microsoft.com/store/detail/arch-wsl/9NPCP8DRCHSN) ***OR*** if you don't want to use Microsoft Store then download the latest msix package from [Release Page](https://github.com/VSWSL/Arch-WSL/releases/latest)

***Note*** - to install manually from the msix package you need to install the .cer file first to the "Trusted Root Certificate Store" of the "local machine"

- After installation is complete from microsoft store or manual install when you open the app you will be presented with a screen to create a user account go ahead with it and complete the account creation to finish installation

![image](https://user-images.githubusercontent.com/52851879/211003117-5ce50ea6-4598-4bdf-8314-c9de65a9947b.png)

***Note*** - The password entering feild does not display your password but it still records it

## Build

### Prerequisites

- Visual Studio 2022
- Python

### Getting Started

- Fork and clone your fork of the Project

- Generate a test certificate:

  - In Visual Studio, open ArchWSL-Appx/MyDistro.appxmanifest
  - Select the Packaging tab
  - Select "Choose Certificate"
  - Click the Configure Certificate drop-down and select Create test certificate.

- Copy tar.gz containing your distro into the x64 folder at the root of the project and rename it to rootfs.tar.gz

***Note*** - You can get the rootfs.tar.gz file from the releases page 

- Then open a terminal window in the root of the project and type in the command

```sh
python build.py --target=build --config=debug --platform=x64
```

https://user-images.githubusercontent.com/52851879/211007722-3743c1a9-62a4-474c-b1be-f31c2ec4e25a.mov

### Root FS

- The main Root FS file this app is based on is at - https://github.com/VSWSL/Arch-WSL-RootFS

- It is based on Arch Docker Image with few tweaks and pre-installed dependencies
