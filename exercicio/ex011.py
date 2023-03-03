frutas = ["Banana", "Maca", "Pera", "Uva","Jamelão"]

fruta_pedida = input("Qual é a fruta que deseja consultar ?")

if(fruta_pedida in frutas):
    print('Sim, temos a fruta.')
else:
    print('Não temos a fruta')

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]

print(min(precos))
print(max(precos))