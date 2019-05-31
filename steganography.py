import sys
from encoder import encoder
from decoder import decoder

def help():
    print('''
                                        Help
Encoding syntax : python steganography.py -e < input_image > < output_image > < message >
                  can use -encode instead of -e also
Decoding syntax : python steganography.py -d < steganographed_image > < output_image >
                  can use -decode instead of -d also
For help        : python steganography.py -h or python steganography.py -help
    *** make sure to add the extension for the outfile except the jpg(jpeg) format.
> Embed a secret message into a cover image using LSB
Positional Arguments ->
    input_image                 :    path to input image
    output_image                :    path to output image
    message                     :    Enter your message that needs to be hidden
> Extract a secret from a steganographic image using LSB on the red channel
Positional Arguments ->
    steganographed_image        :    path of the steganographed image
    output_image                :    path to the output image
A basic Python 3 Script
Dependencies ->
    sudo apt-get install python3-pip
    sudo pip3 install Pillow
        -> ( Pillow or PIL )    
    sudo pip3 install textwrap
        -> if textwrap is not available''')

if __name__ == '__main__':
    #help()
    #encoder("leftgg.png","aa.png", "AAA AAA ")
    #decoder("aa.png", "a.png")
    
    if (sys.argv[1] == '-e' or sys.argv[1] == '-encode') and len(sys.argv) > 4:
        input_image = sys.argv[2]
        output_image = sys.argv[3]
        message = sys.argv[4:]
        message = ' '.join(message)
        encoder(input_image, output_image, message)
    elif (sys.argv[1] == '-d' or sys.argv[1] == '-decode') and len(sys.argv) == 4:
        steg_image = sys.argv[2]
        output_image = sys.argv[3]
        decoder(steg_image, output_image)
    elif (sys.argv[1] == '-h' or sys.argv[1] == '-help') and len(sys.argv) < 3:
        help()
    else:
        print(sys.argv)
        print("steganography.py error : {} \nInvalid command !!! Try '-h' or '-help' ".format(sys.argv[3:]))
