from playwright.sync_api import Page, expect
from Object.ObjectEproc import Peproc_v1

def test_eproc(page:Page):
    eproc = Peproc_v1(page)

    eproc.open_url()
    
    eproc.fill_account("*********","*********")

    eproc.fill_otp("123456")

    eproc.role_option("FUNGSIONAL / PENGGUNA")
    eproc.click_pilih()

    eproc.permohonan_paket_tambah()
    eproc.form_permohonan_paket() 

    page.pause()
    


    