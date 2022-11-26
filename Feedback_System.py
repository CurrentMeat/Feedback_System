mport csv
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
red   = GPIO.input(17)
amber = GPIO.input(27)
green = GPIO.input(22)

with open('Yeet.csv','a',newline='')as file:
    fieldnames = ['rollno','review']
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    while True:

        rollno = input("Please scan your barcode in your identity card :=>")
        print('Please confirm that this is your roll no :=> ',rollno)
        print('Please enter what you feel about our services, press the appropriate buttons RED for a bad review AMBER for a mediocre review GREEN for an excellent review:=>')
        if red:
            revpoint = 'BAD'
            print("Thank You for your response.We are sorry for any inconvenience caused and will try to improve our services.")
        elif amber:
            revpoint = 'OK'
            print("Thank You for your response.")
        elif green:
            revpoint = 'GOOD'
            print("Thank You for your response.We really appreciate it.")
        else:
            print("BOI USE THE BUTTONS YOU 1337 Hax0r ヽ(ｏ`皿′ｏ)ﾉ")
        print('Please confirm that this is your final feedback :=> ',revpoint)
        writer.writerow({'rollno': rollno,'review': revpoint})

