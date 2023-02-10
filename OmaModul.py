from math import *
from pickle import FALSE, TRUE
from random import *
from OmaModul import *
def arithmetic(arv1:float,tehe:str,arv2:float)->any:
    """
    """
    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus=arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2
    elif tehe=="/":
        if arv2==0:
            vastus="DIVO"
        else:
            vasts=arv1/arv2
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
def is_year_leap(aasta: int)->bool:
    """
    """
    if aasta%4==0:
        t=True 
    else:
        t=False 
    return t