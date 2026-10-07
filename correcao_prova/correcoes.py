prov_com = 0
prov_fin = 0
cla_serv = ''
ind_sit = 0

if prov_com == 1 or prov_com == 10 or prov_com == 150 or prov_com == 160 or prov_com == 170 or prov_com == 180:
    if prov_fin == 35 or prov_fin == 36 or prov_fin == 38 or prov_fin == 40 or prov_fin == 42:
        ind_sit = 2
    else:
        ind_sit = 1
    if prov_com == 1 and (prov_fin == 36 or prov_fin == 38) or (cla_serv == 'LIRA' and ind_sit != 2):
        print('SITUAÇÃO 1')
    else:
        if (cla_serv == 'LTCA' or cla_serv == 'LTCA' or cla_serv == 'TUPC' or cla_serv == 'TUPM' or cla_serv == 'DDRD') and (prov_com == 15 or prov_com == 16 or prov_com == 17):
            print('SITUAÇÃO 2')
        else:
            print('SITUAÇÃO 3')
else:
    if prov_fin == 35 or prov_fin == 36 or prov_fin == 38 or prov_fin == 40 or prov_fin == 42:
        print('SITUAÇÃO 4')
    else:
        if prov_fin != 36 and prov_fin != 38 and (cla_serv == 'TUPC' or cla_serv == 'TUPM'):
            print('SITUAÇÃO 5')
        else:
            print('SITUAÇÃO 6')
