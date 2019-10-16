# 1. Deti do 10 let vcetne jezdi zadarmo
# 2. Mladez do 18 vcetne let jezdi za polovinu
# 3. Seniori od 65 let vcetne jezdi za tretinu
# 4. Ostatni jezdi za plnou cenu
# 5. Zaporny vek musi skoncit vyjimkou ValueError

#Toto je dulezite pro testovani toho, zda funkce skonci vyjimkou: with pytest.raises(ValueError):
import pytest
from oddeleni_testu_reseni import spocitej_slevu_jizdneho

def test_dospely_za_plnou_cenu():
    assert spocitej_slevu_jizdneho(30.0, 35) == 30.0

def test_mladez_za_polovinu():
    assert spocitej_slevu_jizdneho(30.0, 16) == 15.0

def test_senior_za_tretinu():
    assert spocitej_slevu_jizdneho(30.0, 70) == 10.0

def test_deti_zadarmo():
    assert spocitej_slevu_jizdneho(30.0, 5) == 0.0

def test_mladez_za_polovinu_hranicni_vek():
    assert spocitej_slevu_jizdneho(30.0, 18) == 15.0

def test_zaporny_vek_konci_vyjimkou():
    with pytest.raises(ValueError):
        spocitej_slevu_jizdneho(30.0, -666)

def test_zaporna_cena_konci_vyjimkou():
    with pytest.raises(ValueError):
        spocitej_slevu_jizdneho(-30.0, 12)

def test_seniori_zdarma():
    assert spocitej_slevu_jizdneho(30.0, 100) == 0

#Ukol
#Pridej test: Deti do deseti let jezdi zadarmo (za 0)
#Pridej test: Zaporny vek skonci vyjimkou ValueError
#Pridej test: Vek 18 se pocita stale jako Mladez (Jezdi za polovinu)

#Bonusove ukoly:
# Pridej podminku, ze zaporna zakladni cena skonci vyjimkou ValueError a pridej test, ktery to overi
# Pridej podminku, ze od 80 let vcetne je jizda zdarma a pridej test, ktery to overi


