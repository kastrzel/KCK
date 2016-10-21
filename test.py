import aiml
k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml")
while True:
    print(k.respond(input("Enter your message >> ")))