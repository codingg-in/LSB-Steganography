# LSB Steganography
A simple Least Significant Bit Steganography program written in python.

## Introduction

This program has two functions: Stenographic LSB encoding and decoding.
Encoding embeds a secret message in form of image in the last significant bits of a cover image.
Decoding extracts a secret image from an steganographic image using LSB.

The number of bits for steganography is fixed to 1 for the minimum visibility of secret message.

    EX: The LSB of 11011010 is 0.

A larger number of bits specified means a higher steganographic capacity. However,
it also means a more visible secret hence it is fixed to 1.

## Usage

##### Encoding
    Syntax: python steganography.py -e < input_image > < output_image > < message >

    > Embed a secret image into a cover image using LSB

        Positional Arguments:
                input_image                 :    path to input image
                output_image                :    path to output image
                message                     :    Enter your message that needs to be hidden

##### Decoding
    Syntax : python steganography.py -d < steganographed_image > < output_image >

    > Embed a secret image into a cover image using LSB

        Positional Arguments:
                steganographed_image        :    path of the steganographed image
                output_image                :    path to output image

>**NOTE** : Add the extension for the outfile except the .jpg/. jpeg format.

### Usage Examples:
    Encoding Example: Hide 'message' into the image 'cover.png' located in the 'image' folder
                      Command: 'python steganography.py -e image/cover.png output.png message'
                      The program will run and create the file 'output.png'
                      'output.png' will look like 'cover.png' but contain secret message 'message'
<br/>

    Decoding Example: To extract secret message hidden in 'output.png' in the 'image' folder
                      Command: 'python steganography.py -d image/output.png message_output.png'
                      The program will run and create the file 'message_output.png'
                      'message_output.png' file will be containing the secret message.

## Dependencies 

This program depends on Python3 Pillow.

##### Installation Using Pip:
    sudo apt-get install python3-pip
    sudo pip3 install Pillow
