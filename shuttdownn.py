def shutdown(user_input):
    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry")

answer = input("Do you want to shut down? ")
shutdown(answer)