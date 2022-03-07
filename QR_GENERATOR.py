##################################################################################
# Required Python Packages
##################################################################################

import qrcode

##################################################################################
# Method Name   : Make Method
# Description   : Generates Quick Response Of Given Link / String
# Input         : Give Any Link / String
# Output        : It Generates Quick Response (QR CODE) 
# Author        : Omkar Rajendra Godase
# Date          : 01/03/2022  
##################################################################################

img = qrcode.make("https://github.com/omkargodase/Python")

##################################################################################
# Method Name   : Save Method
# Description   : This Method Saves QR at given Location
# Input         : File Path 
# Author        : Omkar Rajendra Godase
# Date          : 01/03/2022  
##################################################################################

img.save('C:\\Users\\Omii\\Desktop\\OmiiQR.png')

##################################################################################
# Method Name   : Show Method
# Description   : This Method Shows Generated QR By Our Code
# Author        : Omkar Rajendra Godase
# Date          : 01/03/2022  
##################################################################################
img.show()