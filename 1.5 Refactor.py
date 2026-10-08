"""1.5 Refactor
        Checks the servers status and prints alerts for any server that's down

        It also reports if any down server requires attention or not
        """

servers = [
    {"hostname": "web01", "status": "up"},
    {"hostname": "db01", "status": "down"},
    {"hostname": "app01", "status": "up"},
    {"hostname": "dns01", "status": "down"}
]

def display_server_statuses(server_list):
   """Iterate through servers and print their operational status."""
   for server in server_list:
       hostname = servers["hostname"]
       status = servers ["status"]

       if status == "down":
           print(f"{hostname} is down")
       else:
           print(f"{hostname} is operational")


def main():
    display_server_statuses(servers)


if __name__ == "__main__":
    main()