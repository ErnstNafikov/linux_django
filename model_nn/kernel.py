from backend_api.models import *
import math

def start(I,H,Out):
    for w in WeightNN.objects.all().order_by('id'):
        if w.id == 11:
            sum = w.w0
            sum += w.w1 * H[0]
            sum += w.w2 * H[1]
            sum += w.w3 * H[2]
            sum += w.w4 * H[3]
            sum += w.w5 * H[4]
            sum += w.w6 * H[5]
            sum += w.w7 * H[6]
            sum += w.w8 * H[7]
            sum += w.w9 * H[8]
            sum += w.w10 * H[9]
            Out.append(1 /(1 + math.exp( -sum )))
        else:
            sum = w.w0
            sum += w.w1 * I.flg_contry_usr
            sum += w.w2 * I.flg_contry_card
            sum += w.w3 * I.flg_contry_lng
            sum += w.w4 * I.flg_big_tr
            sum += w.w5 * I.flg_small_tr
            sum += w.w6 * I.flg_chg_card
            sum += w.w7 * I.flg_chg_contry
            sum += w.w8 * I.flg_nigth
            sum += w.w9 * I.flg_rep_tr
            sum += w.w10 * I.flg_bank_decl
            H.append(1 /(1 + math.exp( -sum )))
        
            
def W_dW(I,H,Out):
    Od = (I.flg_fraud-Out[0])*((1-Out[0])*Out[0])
    Hd = []
    Ow = WeightNN.objects.get(id = 11)
    Hd.append(((1-H[0])*H[0])*(Ow.w1*Od))
    Hd.append(((1-H[1])*H[1])*(Ow.w2*Od))
    Hd.append(((1-H[2])*H[2])*(Ow.w3*Od))
    Hd.append(((1-H[3])*H[3])*(Ow.w4*Od))
    Hd.append(((1-H[4])*H[4])*(Ow.w5*Od))
    Hd.append(((1-H[5])*H[5])*(Ow.w6*Od))
    Hd.append(((1-H[6])*H[6])*(Ow.w7*Od))
    Hd.append(((1-H[7])*H[7])*(Ow.w8*Od))
    Hd.append(((1-H[8])*H[8])*(Ow.w9*Od))
    Hd.append(((1-H[9])*H[9])*(Ow.w10*Od))
    E = 0.7
    A = 0.3
    for w in WeightNN.objects.all().order_by('id'):
        b = BiasNN.objects.get(id = w.id)
        if w.id == 11:
            b.w0 = E*Od + b.w0*A
            b.w1 = E*Od*H[0] + b.w1*A
            b.w2 = E*Od*H[1] + b.w2*A
            b.w3 = E*Od*H[2] + b.w3*A
            b.w4 = E*Od*H[3] + b.w4*A
            b.w5 = E*Od*H[4] + b.w5*A
            b.w6 = E*Od*H[5] + b.w6*A
            b.w7 = E*Od*H[6] + b.w7*A
            b.w8 = E*Od*H[7] + b.w8*A
            b.w9 = E*Od*H[8] + b.w9*A
            b.w10 = E*Od*H[9] + b.w10*A
            b.save()
        else:
            b.w0 = E*Hd[w.id - 1] + b.w0*A
            b.w1 = E*Hd[w.id - 1]*I.flg_contry_usr + b.w1*A
            b.w2 = E*Hd[w.id - 1]*I.flg_contry_card + b.w2*A
            b.w3 = E*Hd[w.id - 1]*I.flg_contry_lng + b.w3*A
            b.w4 = E*Hd[w.id - 1]*I.flg_big_tr + b.w4*A
            b.w5 = E*Hd[w.id - 1]*I.flg_small_tr + b.w5*A
            b.w6 = E*Hd[w.id - 1]*I.flg_chg_card + b.w6*A
            b.w7 = E*Hd[w.id - 1]*I.flg_chg_contry + b.w7*A
            b.w8 = E*Hd[w.id - 1]*I.flg_nigth + b.w8*A
            b.w9 = E*Hd[w.id - 1]*I.flg_rep_tr + b.w9*A
            b.w10 = E*Hd[w.id - 1]*I.flg_bank_decl + b.w10*A
            b.save()
        w.w0 = w.w0 + b.w0
        w.w1 = w.w1 + b.w1
        w.w2 = w.w2 + b.w2
        w.w3 = w.w3 + b.w3
        w.w4 = w.w4 + b.w4
        w.w5 = w.w5 + b.w5
        w.w6 = w.w6 + b.w6
        w.w7 = w.w7 + b.w7
        w.w8 = w.w8 + b.w8
        w.w9 = w.w9 + b.w9
        w.w10 = w.w10 + b.w10
        w.save()

def training(n):
    for indx in range(int(n)):
        new_log = Log(log = 'epoch:' + str(indx))
        new_log.save()
        k = 0
        sum_a = 0
        sum_e = 0
        sum_e2 = 0
        for I in DataSet.objects.all().order_by('id'): #.filter(flg_fraud = 1)
            H = []
            Out = []
            start(I,H,Out)
            err = int((I.flg_fraud-Out[0])*(I.flg_fraud-Out[0])*100)
            sum_a+=err
            if err > 10:
                W_dW(I,H,Out)
                H = []
                Out = []
                start(I,H,Out)
                err2 = int((I.flg_fraud-Out[0])*(I.flg_fraud-Out[0])*100)
                #new_log = Log(log = 'iteration:' + str(I.id) + '(' + str(err) + ',' + str(err2) + ')')
                #new_log.save()
                sum_e+=err
                sum_e2+=err2
                k+=1
            else:
                new_log = Log(log = 'iteration:' + str(I.id) + '(' + str(err) + ')')
                #new_log.save()
        new_log = Log(log = 'errors:' + str(k) + ',' + str(int(sum_a/364)) + ',' + str(int(sum_e/k)) + ',' + str(int(sum_e2/k)))
        new_log.save()
    
def resp(I):
    H = []
    Out = []
    start(I,H,Out)
    return int(Out[0]*100)
