from playwright.sync_api import Page, expect
from Object.ObjectEproc import Peproc_v1
from Object.ObjectEkatalog import Ekatalog_v1

def test_ekatalog(page:Page):
    page.bring_to_front()
    eproc = Peproc_v1(page)
    ektlg = Ekatalog_v1(page)

    ## Login
    eproc.open_url()
    eproc.fill_account("************","*******")
    eproc.fill_otp("123456")

    ## EKatalog Page 
    ektlg.open_ekatalog_all()
    ektlg.menu_pesanan_penyedia()
    ektlg.confirmation_product()
    ektlg.form_confirm_product()

    page.pause()

    