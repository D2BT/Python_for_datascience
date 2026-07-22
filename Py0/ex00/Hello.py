ft_list = ["Hello", "tata!"]  #ordonné, itérable, modifiable, autorise les doublons
ft_tuple = ("Hello", "toto!") #ordonné, itérable, non modifiable, autorise les doublons
ft_set = {"Hello", "tutu!"} #non ordonné, itérable, modifiable, n'autorise pas les doublons
ft_dict = {"Hello" : "titi!"} #non ordonné, itérable, modifiable, n'autorise pas les doublons (la clé doit être unique)

ft_list[1]= "World"
ft_tuple = ("Hello", "France!")
ft_set.remove("tutu!")
ft_set.add("Mulhouse")
ft_dict["Hello"] = "42Mulhouse"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)