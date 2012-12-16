import time
enter_your_pin = Pattern("enter_your_pin.png").similar(0.26)

images = [Pattern("0.png").similar(0.59),"1.png","2.png",Pattern("3.png").similar(0.63),"4.png",Pattern("5.png").similar(0.59),"6.png","7.png","8.png","9.png"]

click(enter_your_pin)

for index1, first in enumerate(images):
    for index2, second in enumerate(images):
        for index3, third in enumerate(images):
            for index4, fourth in enumerate(images):
                click(first)
                time.sleep(1)
                click(second)
                time.sleep(1)
                click(third)
                time.sleep(1)
                click(fourth)
                time.sleep(1)
                if (exists(enter_your_pin)):
                    print("WRONG PASSWORD: " + str(index1) + str(index2) + str(index3) + str(index4))
                else:
                    print("FOUND PASSWORD: " + str(index1) + str(index2) + str(index3) + str(index4))
                    exit(0)
                