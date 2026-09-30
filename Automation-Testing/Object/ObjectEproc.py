from playwright.sync_api import Page, expect

class Peproc_v1 : 

    def __init__(self, page : Page) :
        self.page = page
        self.username = page.get_by_role("textbox",name="username")
        self.password = page.get_by_role("textbox",name="password")
        self.button_login = page.locator('button[data-title="Login"]')
        self.kode_otp = page.locator(".token-input")
        self.button_pilih = page.get_by_role("button",name="Pilih")

    def open_url(self) :
        self.page.goto("https://secure-ho-d01.*********/login")
        expect(self.page).to_have_url("https://secure-ho-d01.*********/login")

    def fill_account(self,username,password) :
        self.username.fill(username)
        self.password.fill(password)
        expect(self.button_login).to_be_enabled()
        self.button_login.click()

    def fill_otp(self,otp) : 
        for a, kode in enumerate(otp):
            self.kode_otp.nth(a).fill(kode)

    def role_option(self,role) :
        expect(self.page).to_have_url("https://secure-ho-d01.*********/role")
        self.page.get_by_role("radio",name=role).check()

    def role_option_2(self) : 
        expect(self.page).to_have_url("https://secure-ho-d01.*********/role")
        self.page.locator('input[value="SSC"]').click()

    def click_pilih(self) :
        self.button_pilih.click()

    def permohonan_paket_tambah(self) :
        self.page.get_by_text("Permohonan Paket").click()
        self.page.get_by_role("button",name="Tambah").click()

    def form_permohonan_paket(self) :
        ## Permohonan Paket
        self.page.locator("#reqNotaDinas").fill("ND-2026-11-PLND")
        self.page.locator("#reqNomorPPA").fill("80000011")
        self.page.locator("#reqPelaksanaAngg").select_option("singleyear")
        self.page.locator("#reqTanggal").locator("..").locator("input.combo-text").fill("09-09-2026")
        self.page.locator("#reqTipePr").select_option("investasi")
        self.page.locator("#reqNamaPaket").fill("Pekerjaan Testing Ke - 11")
        self.page.locator("#reqWaktu").fill("120")
        self.page.locator("#reqJnsWaktu").select_option("hari kerja")
        self.page.locator("#reqIjinUsaha").locator("..").locator("span.combo").locator(".combo-arrow-wadah").click()
        self.page.locator(".combobox-item").get_by_text("Pekerjaan Konstruksi",exact=True).click()
        self.page.locator("#reqMetodePengadaan").locator("..").locator("span.combo").locator(".combo-arrow-wadah").click()
        self.page.get_by_text("Penunjukan Langsung", exact=True).click()
        self.page.locator("#reqKeterangan").fill("Testing")

        ## Daftar Item
        self.page.locator('input[id="reqLinkFile[]3"]').set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")
        self.page.locator('input[id="reqLinkFile[]4"]').set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")
        self.page.locator('input[id="reqLinkFile[]6"]').set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")

        ## Rincian Pekerjaan
        self.page.locator("#refresh-data-button").click()
        self.page.locator('input[name="reqItem[]"]').fill("Testing Budget")
        self.page.locator('input[name="reqSatuan[]"]').fill("LS")
        self.page.locator('input[name="reqQuantity[]"]').fill("10")
        self.page.locator('input[name="reqOE[]"]').fill("50000000")
        self.page.get_by_role("button",name="Simpan").click()  

        ## Posting Permohonan Paket
        self.page.get_by_role("gridcell",name='80000011').click()
        self.page.locator("#btnPosting").click()
        self.page.get_by_role("button",name="Ya").click()
        expect(self.page.get_by_text("Info")).to_be_visible()
        self.page.get_by_role("button",name="OK").click()


    def tunjuk_pic_ssc (self) : 
        ## Menu PR
        self.page.get_by_role("link",name="PR").click()
        self.page.get_by_role("link",name="Assign Purchase Request ").click()

        ## Btn Tunjuk PIC
        self.page.get_by_role("gridcell",name="Pekerjaan Testing Ke - 1").click()
        self.page.locator("#btnTunjukPIC").click()

        ## Form Tunjuk PIC
        frame = self.page.frame_locator("iframe.modal-tmp")
        frame.locator('input[comboname="reqPic"] + span.combo .combo-arrow-wadah').click()
        combo = frame.locator(".combo-p")
        print("combo:", combo.count())
        frame.locator(".combo-p:visible .tree-title").filter(has_text="Kantor Pusat").click()
        frame.locator("#ff").get_by_role("button", name="Simpan").click()

    def purchase_req (self) : 
        self.page.locator('a.menu-link.menu-toggle[href="javascript:;"]').filter(has_text="Purchase Request").click()
        self.page.locator('a[href="app/index/purchase_request"]').click()

    def tambah_pengguna (self) :
        self.page.get_by_role("gridcell",name="	Pekerjaan Testing 7").click()
        self.page.get_by_role("link",name="Tambah Pengguna").click()
        self.page.get_by_role("link",name="Hapus dari daftar pengguna").click()
        self.page.locator(".btnAdd").click()
        self.page.get_by_placeholder("Ketikan Nama atau NIPP min 3 digit").fill("*******")
        self.page.locator('td[field="USER_LOGIN"]').filter(has_text="******").dblclick()