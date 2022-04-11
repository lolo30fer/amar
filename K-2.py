import instaloader

ppr=["drock_bc","sias_bc","loverk_bc","godofcar_bc","toki_bc","beisyk_bc","polesht_","gogol_bc"]
loader = instaloader.Instaloader()
loader.login('Eithan__1837_Kamdyn', 'allkosu55dos')

g=0

for i in ppr:
    profile = instaloader.Profile.from_username(loader.context,ppr[g])
    print(ppr[g])
    print("my=> ", profile.followees )
    print("your=> ",profile.followers)
    print("Number of Posts: ", profile.mediacount)
    print("=========================")
    g+=1
    #loader.Delete_all_cookie()