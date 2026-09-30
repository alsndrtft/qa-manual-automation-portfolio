from playwright.sync_api import Page, expect
from Object.ObjectEproc import Peproc_v1
from Object.ObjectEkatalog import Ekatalog_v1

def test_ekatalog(page:Page):
    page.bring_to_front()
    eproc = Peproc_v1(page)
    ektlg = Ekatalog_v1(page)

    ## Login
    eproc.open_url()
    eproc.fill_account("*********","*********")
    eproc.fill_otp("123456")
    eproc.role_option("FUNGSIONAL / PENGGUNA")
    eproc.click_pilih()

    ## Penerimaan Produk (Ekatalog)
    ektlg.open_ekatalog_all()
    ektlg.received_product()
    ektlg.item_good_receipt()
    ektlg.approval_penerimaan_product()

    page.pause()