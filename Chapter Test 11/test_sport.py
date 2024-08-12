from undersökning import AnonymUndersökning

def test_samla_singel_svar():
    fråga = "Vad för sport började du spela först?"
    sport_undersökning = AnonymUndersökning(fråga)
    sport_undersökning.samla_svaren('Handboll')
    assert 'Handboll' in sport_undersökning.svaren

def test_samla_tre_svaren():
    fråga = "Vad för sport började du spela först?"
    sport_undersökning = AnonymUndersökning(fråga)
    svaren = ['Handboll', 'Fotboll', 'Tennis']
    for svar in svaren:
        sport_undersökning.samla_svaren(svar)

    for svar in svaren:
        assert svar in sport_undersökning.svaren

    