with open("saved_info/infos", "r") as file:
    a = file.readlines()
a=[line.strip() for line in a]
info={
    "path":"",
    "username":"",
    "password":""
}
for line in a:
    temp=[line.split("=")[1] for line in a]
    info["path"]=temp[0]
    info["username"]=temp[1]
    info["password"]=temp[2]