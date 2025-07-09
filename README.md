# Forkmanager

Powerfull cli project manager based on python.

## Table Of Contents

- [Forkmanager](#forkmanager)
  - [Table of Contents](#table-of-contents)
     - [Winget](#winget)
     - [Apt](#apt)
  - [Usage](#usage)
    - [Create Project](#create-project)
        - [Create](#create)
        - [Init](#init)
      - [Build Project](#build-project)

## Installation

### Winget
Install via Winget (Windows powershell)
```powershell
winget install forkmanager
```
---

### Apt
Install via Apt (Ubuntu & Debian)
```
apt install forkmanager
```

## Usage

Using forkmanager is easy!

### Create Project
You can create project in .forkmanager or current directory

#### Create
to create project call
```powershell
fm create [name]
```
#### Init
To init project in current directory call
```
fm init
```
Be careful with this! project code can be deleted when you init project!

### Build Project

You can build your project!

```
fm build --pyinstaller
```
