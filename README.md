<h1 align="center">
  <br>
  <a><img src="https://icons-for-free.com/iconfiles/png/512/super+tiny+icons+python-1324450764865983278.png" alt="Markdownify" width="200"></a>
  <br>
  Project DaVinci
  <br>
</h1>

<h4 align="center">A simple Python script that encrypts, decrypts, and embeds strings in images using steganography.</h4>

<!-- 
<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>
-->

![Image](https://res.cloudinary.com/maltob03/image/upload/v1684598956/Screenshot_2023-05-20_alle_18.02.22_gezcxt.png)
##How it works

The Python script provides a complete solution for string encryption, decryption, and steganography. Using a symmetric encryption algorithm, it allows users to encrypt a text string into an encrypted message, and later, decrypt it to obtain the original string.

In addition the script allows users to hide a text string within an image. The user can specify the path to the source image and the text string to be hidden. The steganography algorithm will replace the least significant bits of the image pixels with the bits of the text string, so that the string is hidden within the image. The modified image is then saved to a new file.


## Key Features

* String encryption
* String decryption
* Steganography (Crypto) 
* Steganography (Decrypto) 



## How To Use

What you need to run this script:

1. Python 3
2. Pip

To be sure that you have both Python3 and Pip installed run in your terminal one by one


```
python3 -V //The output should be something like: Python 3.11.3

pip -V //The output should be something like: pip 23.1.2
```

Then you need to install some dependencias

```
pip install cryptocode
```
```
pip install pillow
```

**Run the script**

Open the terminal and move to the script folder.

Once in the terminal the directory is the same of the script run:

```
python3 script_name.py //Note that script_name is a placeholder
```








