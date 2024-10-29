# from captcha import captcha 
# from PIL import Image 

# from captcha.image import ImageCaptcha
# from PIL import Image

# # Create an instance of the ImageCaptcha class
# image_captcha = ImageCaptcha(width=280, height=90)

# # Define the CAPTCHA text
# captcha_text = "1234"

# # Generate the CAPTCHA image
# captcha_image = image_captcha.generate_image(captcha_text)

# # Save the image to a file (optional)
# captcha_image.save("captcha.png")

# # Display the image
# captcha_image.show()

# import sys
# print(sys.path)

from captcha.image import ImageCaptcha

# Create an instance of the ImageCaptcha class
image_captcha = ImageCaptcha(width=280, height=90)

# Define the CAPTCHA text
captcha_text = "1234"

# Generate the CAPTCHA image
captcha_image = image_captcha.generate_image(captcha_text)

# Save the image to a file
captcha_image.save("captcha_test.png")

# Display the image
captcha_image.show()

print("Captcha image created and displayed successfully!")
