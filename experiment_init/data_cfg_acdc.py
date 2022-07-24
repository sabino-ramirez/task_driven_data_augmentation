import sys

def train_data(no_of_tr_imgs,comb_of_tr_imgs):
    #print('train data')
    if(no_of_tr_imgs=='tr5' and comb_of_tr_imgs=='c1'):
        labeled_id_list=["002","007","010","013","014"]
    #elif(no_of_tr_imgs=='tr5' and comb_of_tr_imgs=='c2'):
    #    labeled_id_list=["003","023","043","063","083"]
    #elif(no_of_tr_imgs=='tr15' and comb_of_tr_imgs=='c1'):
    #    labeled_id_list=["001","002","003","021","022","023",\
    #                     "041","042","043","061","062","063","081","082","083"]
    #elif(no_of_tr_imgs=='tr15' and comb_of_tr_imgs=='c2'):
    #    labeled_id_list=["005","006","013","025","026","033",\
    #                     "045","046","053","065","066","073","085","086","093"]
    #elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c1'):
    #    labeled_id_list=["002","022","042"]
    elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c1'):
        labeled_id_list=["007","008","013"]
    #elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c2'):
    #    labeled_id_list=["042","062","082"]
    #elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c3'):
    #    labeled_id_list=["022","042","082"]
    #elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c4'):
    #    labeled_id_list=["002","042","082"]
    #elif(no_of_tr_imgs=='tr3' and comb_of_tr_imgs=='c5'):
    #    labeled_id_list=["002","042","095"]
    #elif(no_of_tr_imgs=='tr1' and comb_of_tr_imgs=='c1'):
    #    labeled_id_list=["002"]
    #elif(no_of_tr_imgs=='tr1' and comb_of_tr_imgs=='c2'):
    #    labeled_id_list=["042"]
    #elif(no_of_tr_imgs=='tr1' and comb_of_tr_imgs=='c3'):
    #    labeled_id_list=["022"]
    #elif(no_of_tr_imgs=='tr1' and comb_of_tr_imgs=='c4'):
    #    labeled_id_list=["062"]
    #elif(no_of_tr_imgs=='tr1' and comb_of_tr_imgs=='c5'):
    #    labeled_id_list=["095"]
    #elif(no_of_tr_imgs=='tr40' and comb_of_tr_imgs=='c1'):
    #    labeled_id_list=["001","002","003","004","005","006","012","013",\
    #                "021","022","023","024","025","026","032","033",\
    #                "041","042","043","044","045","046","052","053",\
    #                "061","062","063","064","065","066","072","073",\
    #                "081","082","083","084","085","086","092","093"]
    else:
        print('Error! Select valid combination of training images')
        sys.exit()
    return labeled_id_list

def val_data():
    #print('valilation data')
    val_list=["003","014"]
    return val_list

def unlabeled_data():
    #print('unlabeled data')
    unlabeled_list=["001", "015", "004", "005"]
    return unlabeled_list

def test_data():
    #print('test data')
    test_list=["002", "006", "009", "010", "011", "012"]
    return test_list
