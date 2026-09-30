from playwright.sync_api import Page, expect
from ObjectEproc import Peproc_v1
from ObjectEkatalog import Ekatalog_v1

def test_ekatalog(page:Page):
    eproc = Peproc_v1(page)
    ektlg = Ekatalog_v1(page)

    eproc.open_url()
    
    eproc.fill_account("*******","*********")

    eproc.fill_otp("123456")

    eproc.role_option("FUNGSIONAL / PENGGUNA")
    eproc.click_pilih()
    
    ektlg.open_ekatalog()
    ektlg.cost_center()
    ektlg.gl_account()
    ektlg.plant()
    ektlg.quantity(2)
    ektlg.check_out()
    # page.wait_for_timeout(10000)