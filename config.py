if __name__ == "__main__":
    print("-"*20)

    token = input("please enter your Discord API Token\nToken: ")

    print("-"*20)

    channel_id = input("please enter the Channel ID of the Discord Channel you want to read\nChannel ID: ")

    with open("annbot/.env", "w") as file:
        file.write(f"TOKEN=\"{token}\"\nCHANNEL_ID=\"{channel_id}\"\n")

    print("\ndone!")
